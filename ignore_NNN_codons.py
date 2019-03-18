#Ignore NNN AAs

def ignore_nnn(string):
    '''ignore database codon entries with N
    Input: string(DNA seq) is read from text file
    Output: clean_string without N is passed through, codons with N is ignored
    '''
    clean_string=''
    
    for i in string:
        if i!='N' or 'n':
            clean_string.append(string)
        else:
            continue

    print(clean_string)

open_file()
ignore()
ignore_nnn='AKDJFHSFRHFCDO'
