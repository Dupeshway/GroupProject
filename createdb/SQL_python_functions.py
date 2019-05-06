#!/usr/bin/env python3

class sql_query:


        def db_query(output_type, input_type, input_value):
                """Retreive search query when given query parameters;
                output_type, input_type and input_value, provided by the webuser
                input= output_type, input_type, input_value
                query parameters for data retrieval
                output= output_value within the provided parameters
                """

                sql = "select "+output_type+" from CHROM8 where "+input_type+"='"+input_value+"'"
                return sql



        def db_summary(accession_no):
                '''select (*)
                Returning entire record assoiciated with Accession no.
                '''
                sql="select * from CHROM8 where ACCESSION='"+accession_no+"'"
                return sql
