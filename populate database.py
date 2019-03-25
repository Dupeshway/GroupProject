import re

with open("/home/yobi/Documents/Bioinformatics/Biocomp2/chrom_CDS_8.txt", 'r') as f:
    file=f.read().splitlines()

for line in file:
    p = re.compile(r'Accession number *',i)
    acc_no = p.finditer(i)
    if acc_no:
        print(acc_no)
