import pandas as pd
import argparse
import sys

def get_complement(nuc):
    """Returns the complement of a DNA nucleotide."""
    comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return comp_dict.get(nuc.upper(), nuc.upper())

def apply_mutations(fasta_in, table_in, fasta_out):
    # 1. Read the Reference FASTA sequence
    try:
        with open(fasta_in, 'r') as f:
            lines = f.read().splitlines()
            
        header = lines[0]
        original_seq = "".join(lines[1:]).upper()
        seq_list = list(original_seq)
        
    except Exception as e:
        print(f"Error reading FASTA file: {e}")
        sys.exit(1)

    # 2. Read the Variant Table
    try:
        df = pd.read_csv(table_in, sep='\t')
    except Exception as e:
        print(f"Error reading Variant Table: {e}")
        sys.exit(1)

    print(f"Loaded reference sequence: {len(seq_list)} bp.")

    # 3. Auto-detect Strand based on coordinate sorting
    is_reverse = False
    if len(df) > 1:
        # If the first position is greater than the last position, it's descending (Reverse Strand)
        if df['Gene_Position'].iloc[0] > df['Gene_Position'].iloc[-1]:
            is_reverse = True
            
    if is_reverse:
        print("-> Auto-detected: Reverse Strand (-). Complementing expected and alternative alleles.")
    else:
        print("-> Auto-detected: Forward Strand (+).")

    mod_count = 0
    error_count = 0

    # 4. Iterate through mutations
    for index, row in df.iterrows():
        var_id = str(row['Variant_ID'])
        gene_pos = int(row['Gene_Position'])
        
        parts = var_id.split('_')
        if len(parts) < 3:
            continue
            
        ref_nuc = parts[1].upper()
        alt_nuc = parts[2].upper()
        
        # If on reverse strand, complement the VCF genomic alleles to match transcript sequence
        if is_reverse:
            ref_nuc = get_complement(ref_nuc)
            alt_nuc = get_complement(alt_nuc)
        
        idx = gene_pos - 1 # Convert to 0-based python index
        
        if idx >= len(seq_list) or idx < 0:
            print(f"Error: Position {gene_pos} out of bounds.")
            error_count += 1
            continue

        # 5. Verify and Mutate
        actual_nuc = seq_list[idx]
        
        if actual_nuc == ref_nuc:
            seq_list[idx] = alt_nuc
            print(f"Mutated Pos {gene_pos:>4}: {ref_nuc} -> {alt_nuc}")
            mod_count += 1
        else:
            print(f"FAIL at Pos {gene_pos:>4}: Expected '{ref_nuc}', but found '{actual_nuc}' in sequence. Skipping.")
            error_count += 1

    # 6. Reconstruct and export
    mutated_seq = "".join(seq_list)
    new_header = header + "_Mutated"
    
    with open(fasta_out, 'w') as fout:
        fout.write(new_header + "\n")
        for i in range(0, len(mutated_seq), 60):
            fout.write(mutated_seq[i:i+60] + "\n")
            
    print("-" * 40)
    print("Mutagenesis Complete.")
    print(f"Successfully applied: {mod_count} mutations.")
    print(f"Failed validations:   {error_count} mutations.")
    print(f"Output saved to:      {fasta_out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="In Silico Mutagenesis with Auto-Strand Detection.")
    parser.add_argument("-f", "--fasta", required=True, help="Input FASTA file")
    parser.add_argument("-t", "--table", required=True, help="Variant table with Gene_Position")
    parser.add_argument("-o", "--output", required=True, help="Output mutated FASTA")
    
    args = parser.parse_args()
    apply_mutations(args.fasta, args.table, args.output)