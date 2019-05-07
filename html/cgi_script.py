#!/bin/env python3
import cgi

import cgitb
cgitb.enable()
import re

from getAccessionNumber import getAccessionNumber
from getGeneID import getGeneID
from getChrLocation import getChrLocation
from getProductName import getProductName

from doLocalCodonUsage import doLocalCodonUsage
from doTotCodonUsage import doTotCodonUsage

from doAminoAcidAndCDS import doAminoAcidAndCDS

from getDNA import getDNA
from doSelectCDS import doSelectCDS

from doRestrictionEnzymes import doRestrictionEnzymes

form = cgi.FieldStorage()
input_type = form["type"].value
input_value = form["query"].value

# POINT 2 of REQUIREMENTS - SEARCH BASED ON QUERY:
s = ''
t = ''
u = ''
w = ''

s = getAccessionNumber(input_type, input_value)
s=str(s)
clean_s=re.sub('[join(,)<>+{}]','', s)

t = getGeneID(input_type, input_value)
t=str(t)
clean_t=re.sub('[join(,)<>+{}]','', t)

u = getChrLocation(input_type, input_value)
u=str(u)
clean_u=re.sub('[join(,)<>+{}]','', u)

w = getProductName(input_type, input_value)
w=str(w)
clean_w=re.sub('[join(,)<>+{}]','', w)


# POINT 3 (A) of REQUIREMENTS - COMPLETE DNA SEQUENCE

x = ''
x = getDNA(input_type, input_value)
x=str(x)
clean_x=re.sub('[join(,)<>+{}]','', x)

cds = ''
cds = doSelectCDS(input_type, input_value)
cds=str(cds)
clean_cds=re.sub('[join(,)<>+{}]','', cds)

# POINT 3 (B) of REQUIREMENTS - COMPLETE AA SEQUENCE + CDS

aacds =''
aacds = doAminoAcidAndCDS(input_type, input_value)
aacds=str(aacds)
clean_aacds=re.sub('[join(,)<>+{}]','', aacds)

# POINT 3 (C) of REQUIREMENTS - CODON USAGE FREQUENCIES

lcu = ''
lcu = doLocalCodonUsage(input_type, input_value)
lcu=str(lcu)
clean_lcu=re.sub('[join(,)<>+{}]','', lcu)

tcu = ''
tcu = doTotCodonUsage()
tcu=str(tcu)
clean_tcu=re.sub('[join(,)<>+{}]','', tcu)

# POINT 3 (D) of REQUIREMENTS - RESTRICTION ENZYMES

res = ''
res = doRestrictionEnzymes(input_type, input_value)
res=str(res)
clean_res=re.sub('[join(,)<>+{}]','', res)


print ("Content-Type: text/html\r\n\r\n")

html ="<html>"
html += "<head>\n"
html += "<link rel='stylesheet' type='text/css' href='/cgi-bin/cgi/cgi_style.css'>"
html += "<style>\n"
html += "table{border-collapse: collapse; width: 100%;} tx, td {text-align: left; padding: 8px;} tr:nth-child(even) {background-color: #f3f3f3;}\n"
html += "</style>"
html += "<title>Query results</title>\n"
html += "</head>\n\n"
html += "<body>\n"

html += "<h1>Query results</h1>\n"
html += "<h3>Your query was:</h3>\n"
html += "<pre>\n"
html += input_type
html += "</pre>\n"
html += "<h3>type</h3>\n"
html += "<pre>\n"
html += input_value
html += "</pre>\n"


html += "<table>"
html += "<tr>"
html += "<th> ACCESSION </th>\n"
html += "<th> CHROM_LOC </th>\n"
html += "<th> GENE_ID </th>\n"
html += "<th> PRODUCT_NAME </th>\n"
html += "</tr>\n"
html += "<tr>\n"
html += "<th>" + clean_s + "</th>\n"
html += "<th>" + clean_u + "</th>\n"
html += "<th>" + clean_t + "</th>\n"
html += "<th>" + clean_w + "</th>\n"
html += "</tr>\n"
html += "</table>\n"

html +="<h3>Point 3.A.</h3>\n"
html += "<pre>\n"
html += "<h2>" + clean_x + "</h2>\n"
html += "<h2>" + clean_cds + "</h2>\n"
html += "</pre>\n"

html +="<h3>Point 3.B.</h3>\n"
html += "<pre>\n"
html += "<h2>" + clean_aacds + "</h2>\n"
html += "</pre>\n"

html +="<h3>Point 3.C.</h3>\n"
html += "<pre>\n"
html += "<h2>" + clean_tcu + "</h2>\n"
html += "<h2>" + clean_lcu + "</h2>\n"
html += "</pre>\n"

html +="<h3>Point 3.D.</h3>\n"
html += "<pre>\n"
html += "<h2>" + clean_res + "</h2>\n"
html += "</pre>\n"

html += "</body>\n"
html += "</html>\n"
print (html)