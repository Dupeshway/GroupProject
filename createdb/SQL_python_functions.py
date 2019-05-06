#!/usr/bin/env python3
import pymysql.cursors

class sql_query:

        dbname   = "ly001"
        dbhost   = "ssh.cryst.bbk.ac.uk" #Replace ssh with hope when working from nomachine
        dbuser   = "ly001"   # Ask a demonstrator
        dbpass   = "7#b8tpkum"   # Ask a demonstrator
        port     = 3306
        db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)
        
        def db_query(output_type, input_type, input_value):
                """Retreive search query when given query parameters;
                output_type, input_type and input_value, provided by the webuser
                input= output_type, input_type, input_value
                query parameters for data retrieval
                output= output_value within the provided parameters
                """

                sql = "select "+output_type+" from CHROM8 where "+input_type+"='"+input_value+"'"
                cursor = db.cursor()
                data  = cursor.execute(sql)
                output_value   = cursor.fetchall()
                return output_value



        def db_summary(output_type):
                '''select (*)
                Returning entire record assoiciated with Accession no.
                '''
                sql="select "+output_type+" from CHROM8"
                cursor = db.cursor()
                data  = cursor.execute(sql)
                output_value   = cursor.fetchall()
                return output_value
