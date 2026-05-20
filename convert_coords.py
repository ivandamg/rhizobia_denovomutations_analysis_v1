import pandas as pd
import argparse
import sys

def get_gene_info(gff_file, replicon, gene_name):
    """Parses a GFF3 file to find the start, end, and strand of a specific gene."""
    try:
        with open(gff_file, 'r') as f:
            for line in f:
                if line.startswith("#"):
                    continue
                parts = line.strip().split('\t')
                if len(parts) < 9:
                    continue
                
                seqid = parts[0]
                feature_type = parts[2]
                start = int(parts[3])
                end = int(parts[4])
                strand = parts[6]
                attributes = parts[8]
                
                # Match the exact replicon and search for the gene name in attributes
                if seqid == replicon and gene_name in attributes and feature_type in ["gene", "CDS"]:
                    return start, end, strand
    except Exception as e:
        print(f"Error reading GFF file: {e}")
        sys.exit(1)
        
    return None, None, None

def convert_coordinates(input_table, gff_file, replicon, gene_name, output_table):
    # 1. Fetch Gene Metadata
    start, end, strand = get_gene_info(gff_file, replicon, gene_name)
    if not start:
        print(f"Error: Gene '{gene_name}' not found on replicon '{replicon}' in GFF.")
        sys.exit(1)
        
    print(f"Found {gene_name} on {replicon}: Start={start}, End={end}, Strand={strand}")

    # 2. Robust Table Loading (Handles R-style missing headers)
    try:
        # Check the first two lines manually to detect column offsets
        with open(input_table, 'r') as f:
            header = f.readline().strip("\n").split('\t')
            row1 = f.readline().strip("\n").split('\t')
            
        if len(header) == len(row1) - 1:
            # R-style table: the first column is the index.
            df = pd.read_csv(input_table, sep='\t', index_col=0)
            df = df.reset_index()
            df.rename(columns={df.columns[0]: 'Variant_ID'}, inplace=True)
        else:
            # Standard table
            df = pd.read_csv(input_table, sep='\t')
            df.rename(columns={df.columns[0]: 'Variant_ID'}, inplace=True)
            
        # Force Variant_ID to string to prevent any future .split() AttributeErrors
        df['Variant_ID'] = df['Variant_ID'].astype(str)

    except Exception as e:
        print(f"Error reading input table: {e}")
        sys.exit(1)

    # 3. Calculate Gene Position
    def calculate_pos(variant_id):
        try:
            # Extract the genomic coordinate. str() ensures safety if IDs are just pure numbers
            replicon_pos = int(str(variant_id).split('_')[0])
            
            # Calculate coordinate relative to gene start (1-based)
            if strand == '+':
                return replicon_pos - start + 1
            elif strand == '-':
                return end - replicon_pos + 1
            else:
                return None
        except ValueError:
            return None # Failsafe for unexpected strings

    # Apply calculation to create the new column
    df['Gene_Position'] = df['Variant_ID'].apply(calculate_pos)

    # 4. Export Table
    # Reorder columns slightly to keep Variant_ID and Gene_Position next to each other
    cols = df.columns.tolist()
    cols = ['Variant_ID', 'Gene_Position'] + [c for c in cols if c not in ['Variant_ID', 'Gene_Position']]
    df = df[cols]

    df.to_csv(output_table, sep='\t', index=False)
    print(f"Successfully converted coordinates. Output saved to {output_table}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Replicon Coordinates to Gene Coordinates.")
    parser.add_argument("-i", "--input", required=True, help="Input variant table (tab-delimited)")
    parser.add_argument("-g", "--gff", required=True, help="Genome annotation file (GFF3)")
    parser.add_argument("-r", "--replicon", required=True, help="Name of the replicon (e.g., 'NC_003047.1')")
    parser.add_argument("-n", "--gene", required=True, help="Gene name to search in GFF attributes (e.g., 'rpoB')")
    parser.add_argument("-o", "--output", required=True, help="Output file name")
    
    args = parser.parse_args()
    
    convert_coordinates(args.input, args.gff, args.replicon, args.gene, args.output)