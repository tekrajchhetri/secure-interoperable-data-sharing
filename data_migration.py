# -*- coding: utf-8 -*-
# @Time    : 08.05.22 13:43
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : data_migration.py
# @Software: PyCharm
import textwrap
from connection_manager import ConnectionManager
from SPARQLWrapper import  POST

class DataMigration:
    def prefix(self):
        prefix = textwrap.dedent("""
            PREFIX : <http://tekrajchhetri.com/sricats#> 
            PREFIX sosa: <http://www.w3.org/ns/sosa/>  
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>  
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        """)
        return prefix

    def migrate_to_gdb(self, data):
        query = textwrap.dedent("""{0} 
                    INSERT DATA {{ 
                    {1}
                    }}

                """).format(self.prefix(),
                             data
                            )
        cm = ConnectionManager()
        sparql = cm.graphdb_connection(type="post")
        sparql.setMethod(POST)
        sparql.setQuery(query)
        sparql.setReturnFormat('json')
        result = sparql.query()
        if str(result.response.read().decode("utf-8")) == "":
            return "SUCCESS"
        return "FAIL"

