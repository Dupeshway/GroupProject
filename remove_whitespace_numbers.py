#remove spaces and numbers from DNA_seq

with open("/home/yobi/Documents/Bioinformatics/Biocomp2/dummy_dna.txt", 'r') as f:
    file=f.read()
for i in file:
    i.replace(' ','')
    file.append(i)
    
print(file)
