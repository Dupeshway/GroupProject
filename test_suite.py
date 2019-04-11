#TEST SUITE
'''only for testing functions'''

import re
from Bio import SeqIO as bseq
from config import config as cg
from file_management import file_management as fm
from parse_data import parsing as pg
from clean_strings import clean_data as cl



raw_data = fm.open_file(cg.r_file)
#opens r_file and reads into raw_data

clean_data=cl.join_strings(raw_data)
#joins all strings and reads into clean_data

fm.write_file(clean_data, cg.w_file)
#writes the clean_data into the w_file

