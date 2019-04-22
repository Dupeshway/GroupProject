# GroupProject
YMCJ Biocomp2 Group project

----------------------------------------------------------------------------

Documentation: (creating your database)

Open mysql and run the following sql files:

1. CHROM8.sql (This will build your table)

2. Next populate your database by running the following files in mysql:

    i) acc_no_parse.sql (ACCESSION numbers)
    
    ii) gene_parse.sql (GENE_ID, indexed by Accession numbers, some records dont have Gene_id)
    
    iii) product_parse.sql (PRODUCT_NAME, Protein product name, some records dont have or use multiple)
    
    iii) parse_chrom_loc.sql (CHROM_LOC, Chromosome location, indexed by Accession number)
    
    iv) sql_dna_seq.sql (DNA_SEQUENCE: this is proving to be tougher to get working)

