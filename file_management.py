
class file_management:

    from config import config as cg

    def open_file(r_file):
        '''Input: text file of chromosome
        Output: string of each line from input file returned for parsing'''


        with open(r_file,'r') as f:
            data_strings = f.read().splitlines()
            return data_strings



    def write_file(r_file, w_file):
        '''Writes to the file parameter
        input 1: opens read file, defined in config, MUST BE SINGLE STRING
        input 2: writes to w_file, defined in config
        output: database written into file'''
        
        f = open(w_file,'w+')
        f.write(r_file)

