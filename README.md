# rhizobia_denovomutations_analysis_v1
analysis of mutations identified in argon experiment. we evaluated a population of rhizobia that included symbiotic and non-symbiotic strains. Fargozi et al., 



Analysis phylogeny and individual mutations in Argan experiment


# 1. convert_coords.py


# 2. rename_ns_strains.py



# 3. in_silico_mutagenesis.py


# 4. copy paste in_silico_mutagenesis into multifasta file rpoD_output_variants_with_gene_pos.txt





# 5. extract nucleotide position based on gene position file cyoB_output_variants_with_gene_pos

 
        ~/ZZ_Software/seqkit subseq -r 1257:1257 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1257_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1239:1239 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1239_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1233:1233 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1233_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1227:1227 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1227_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1188:1188 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1188_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1170:1170 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1170_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1143:1143 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1143_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1131:1131 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1131_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1119:1119 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1119_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1110:1110 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1110_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1107:1107 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1107_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1068:1068 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1068_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1066:1066 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1066_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1056:1056 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1056_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1053:1053 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1053_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1015:1015 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1015_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 1008:1008 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/1008_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 970:970 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/970_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 843:843 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/843_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 404:404 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/404_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 393:393 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/393_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 387:387 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/387_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 370:370 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/370_CyoB_Fargozi_Argon_MSA.fa
        ~/ZZ_Software/seqkit subseq -r 345:345 cyoB/finalFargozicyoBPhylo_Renamed.fasta | grep -v ">" > cyoB/345_CyoB_Fargozi_Argon_MSA.fa


# 6. get the names of each sequnece

    cat finalFargozicyoBPhylo_Renamed.fasta | grep ">" > Names_Fargozi_Argon_MSA.fa


# 7. make a df that contain the nucleotide for each position and a category variable. Symbiotic or not. 

Name	345	370	387	393	404	843	970	1008	1015	1053	1056	1066	1068	1107	1110	1119	1131	1143	1170	1188	1227	1233	1239	1257	Category
>VariablePositionArgonExp	A	A	G	G	T	T	G	C	A	T	G	G	C	C	A	G	C	T	T	T	C	T	T	C	Symbiotic
>ReferenceArgonExp	C	G	C	C	A	C	A	G	C	C	C	T	G	G	C	C	G	C	G	C	G	G	G	C	Symbiotic
>GCA_002197025.1 original_id=lcl|CP021795.1_cds_ASP55562.1_6247 pident=99.552	A	A	G	G	T	T	G	C	A	T	G	G	C	C	A	G	C	T	Symbiotic
>NS_GCA_001429285.1 original_id=lcl|LMJJ01000008.1_cds_KRD66041.1_1857 pident=83.498	C	G	C	C	A	T	A	G	C	C	G	G	C	G	T	G	C	Non-Symbiotic
>NS_GCA_001429125.1 original_id=lcl|LMII01000034.1_cds_KRC17243.1_4914 pident=84.097	C	G	C	T	A	T	A	C	C	T	C	G	C	C	G	G	C	Non-Symbiotic
>NS_GCA_001426365.1 original_id=lcl|LMEN01000034.1_cds_KQX44890.1_5053 pident=84.097	C	G	C	T	A	T	A	C	C	T	C	G	C	C	G	G	C	Non-Symbiotic
>GCA_002865105.1 original_id=lcl|NBUI01000068.1_cds_PLU34322.1_6658 pident=92.563	C	G	C	G	G	C	G	T	T	C	C	A	G	G	C	G	C	Symbiotic
>GCA_001651865.1 original_id=lcl|LPUX01000055.1_cds_OAP39880.1_2344 pident=91.213	G	A	G	G	T	C	G	C	A	C	C	G	C	A	C	G	C	Symbiotic
>GCA_000283895.1 original_id=lcl|HE616899.1_cds_CCE99799.1_5302 pident=90.155	G	A	C	G	T	C	G	C	A	C	C	G	C	G	C	G	C	T	Symbiotic



     NAME_FILE="Names_Fargozi_Argon_MSA.fa"
     FILES=$(ls [0-9]*_Fargozi_Argon_MSA.fa | sort -V)
     HEADER="Name"
     for f in $FILES; do     POS=$(echo "$f" | cut -d'_' -f1);     HEADER="$HEADER\t$POS"; done
     HEADER="$HEADER\tCategory"
     $HEADER
     paste "$NAME_FILE" $FILES <(awk '{if ($0 ~ /NS/) print "Non-Symbiotic"; else print "Symbiotic"}' "$NAME_FILE")
     echo -e "$HEADER" > msa_table.tsv
     head msa_table.tsv 
     paste "$NAME_FILE" $FILES <(awk '{if ($0 ~ /NS/) print "Non-Symbiotic"; else print "Symbiotic"}' "$NAME_FILE") >> msa_table.tsv




# 8. clean names in fasta file

    sed '/^>/ s/ .*//' finalFargozicyoBPhylo_Renamed.fasta > finalFargozicyoBPhylo.fasta

    sed 's/a/A/g' msa_table.tsv |sed 's/c/C/g' |sed 's/t/T/g' |sed 's/g/G/g' > msa_table2.tsv

# 9. modify header and argan treatments on msa_table2.tsv by hand.

# 10. make a multiple sequence alignement with previous final...fasta

     mafft finalFargozicyoBPhylo.fasta > Aligned_cyoB_complete_withArgonFriMut.fasta
