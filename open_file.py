# opening and reading the text file as strings

def open_file(file):
    '''reads in the file and prepares it for formatting
    input= text file
    output= reads the file and stores as strings ready to format
    '''

    with open("dummyfile.txt", "r") as f:
        file= f.read().splitlines()
        
        return: file
