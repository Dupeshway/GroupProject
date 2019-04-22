# GroupProject
YMCJ Biocomp2 Group project

----------------------------------------------------------------------------

Documentation: (creating your database)

Open mysql and run the following sql files:

1. CHROM8.sql (This will build your table)

2. Next populate your database by running the following files in mysql:

    i) acc_no_parse.sql (Accession numbers)
    
    ii) gene_parse.sql (GENE_id, indexed by Accession numbers, some records dont have Gene_id)
    
    iii) parse_chrom_loc.sql (Chromosome location, indexed by Accession number, some records dont have chromosome location)
    
    iv) sql_dna_seq.sql (DNA sequence: this is proving to be tougher to get working)

