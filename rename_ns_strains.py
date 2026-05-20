import argparse
import sys
import os

def rename_fasta_headers(fasta_in, list_file, fasta_out):
    # 1. Load the list of non-symbiotic strains into a list
    if not os.path.exists(list_file):
        print(f"Error: The list file '{list_file}' was not found.")
        sys.exit(1)
        
    with open(list_file, 'r') as f:
        # Read lines, strip whitespace/newlines, and ignore empty lines
        ns_strains = [line.strip() for line in f if line.strip()]
        
    print(f"Loaded {len(ns_strains)} non-symbiotic accession IDs.")

    # 2. Process the FASTA file line by line
    mod_count = 0
    with open(fasta_in, 'r') as fin, open(fasta_out, 'w') as fout:
        for line in fin:
            if line.startswith(">"):
                # Check if any of the targeted GCA IDs are in this header
                for ns_id in ns_strains:
                    if ns_id in line:
                        # Replace the GCA ID with NS_GCA ID
                        line = line.replace(ns_id, f"NS_{ns_id}")
                        mod_count += 1
                        break # Move to the next line once modified
            
            # Write the line (modified header, unmodified header, or sequence)
            fout.write(line)
            
    print(f"Successfully modified {mod_count} headers.")
    print(f"Output saved to: {fasta_out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepend 'NS_' to specific FASTA headers.")
    parser.add_argument("-i", "--input", required=True, help="Input multi-FASTA file")
    parser.add_argument("-l", "--list", required=True, help="Text file with list of GCA accessions")
    parser.add_argument("-o", "--output", required=True, help="Output multi-FASTA file")
    
    args = parser.parse_args()
    rename_fasta_headers(args.input, args.list, args.output)