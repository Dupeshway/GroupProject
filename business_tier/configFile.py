#!/usr/bin/env python3

# Parameters for get functions
dbArg1 = 'ACCESSION'
dbArg2 = 'CHROM_LOC'
dbArg3 = 'GENE_ID'
dbArg4 = 'PRODUCT_NAME'
dbArg5 = 'TRANSLATION'
dbArg6 = 'CDS_REGIONS'
dbArg7 = 'DNA_SEQUENCE'

# Characters for recognising start/end of cds regions
cds_start_char = '<'
cds_end_char  = '>'

# Characters for recognising restriction enzymes
ecoRI_forward = 'GAATTC'
ecoRI_reverse = 'CTTAAG'
ecoRI_char = '@'

bamHI_forward = 'GGATCC'
bamHI_reverse = 'CCTAGG'
bamHI_char = '$'

bsuMI_forward = 'CTCGAG'
bsuMI_reverse = 'GAGCTC'
bsuMI_char = '%'

# Parameter for codon length
codon_length = 3

# Dictionary of codon with associated amino acid code
aa_dict = {'TTT':'Phe(F)', 'TTC':'Phe(F)', 'TTA':'Leu(L)', 'TTG':'Leu(L)', \
     'TCT':'Ser(S)', 'TCC':'Ser(S)', 'TCA':'Ser(S)', 'TCG':'Ser(S)', \
     'TAT':'Tyr(Y)', 'TAC':'Tyr(Y)', 'TAA':'STOP', 'TAG':'STOP', \
     'TGT':'Cys(C)', 'TGC':'Cys(C)', 'TGA':'STOP', 'TGG':'Trp(W)', \
     'CTT':'Leu(L)', 'CTC':'Leu(L)', 'CTA':'Leu(L)', 'CTG':'Leu(L)',
     'CCT':'Pro(P)', 'CCC':'Pro(P)', 'CCA':'Pro(P)', 'CCG':'Pro(P)', \
     'CAT':'His(H)', 'CAC':'His(H)', 'CAA':'Gln(Q)', 'CAG':'Gln(Q)', \
     'CGT':'Arg(R)', 'CGC':'Arg(R)', 'CGA':'Arg(R)', 'CGG':'Arg(R)', \
     'ATT':'Ile(I)', 'ATC':'Ile(I)', 'ATA':'Ile(I)', 'ATG':'Met(M)-START', \
     'ACT':'Thr(T)', 'ACC':'Thr(T)', 'ACA':'Thr(T)', 'ACG':'Thr(T)', \
     'AAT':'Asn(N)', 'AAC':'Adn(N)', 'AAA':'Lys(K)', 'AAG':'Lys(K)', \
     'AGT':'Ser(S)', 'AGC':'Ser(S)', 'AGA':'Arg(R)', 'AGG':'Arg(R)', \
     'GTT':'Val(V)', 'GTC':'Val(V)', 'GTA':'Val(V)', 'GTG':'Val(V)', \
     'GCT':'Ala(A)', 'GCC':'Ala(A)', 'GCA':'Ala(A)', 'GCG':'Ala(A)', \
     'GAT':'Asp(D)', 'GAC':'Asp(D)', 'GAA':'Glu(E)', 'GAG':'Glu(E)', \
     'GGT':'Gly(G)', 'GGC':'Gly(G)', 'GGA':'Gly(G)', 'GGG':'Gly(G)'}
