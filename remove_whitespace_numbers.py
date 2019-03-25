#remove spaces and numbers from DNA_seq

def clean_wspace(dna_seq):
    dna_seq = dna_seq.replace('\n', '')
    dna_seq = dna_seq.replace(' ', '')
    return(dna_seq)


def clean_nos(dna_seq):
    nos = ['0','1','2','3','4','5','6','7','8','9']
    dna_seq = dna_seq.replace(nos, '')
    return(dna_seq)
