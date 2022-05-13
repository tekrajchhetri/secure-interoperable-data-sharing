# -*- coding: utf-8 -*-
# @Time    : 08.05.22 13:43
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : data_migration.py
# @Software: PyCharm
import textwrap
from core.connection_manager import ConnectionManager
from SPARQLWrapper import  POST

class DataMigration:
    def migrate_to_gdb(self, triples):
        query = """
        INSERT DATA {GRAPH <http://www.tekrajchhetri.com/sricats> {""" + triples + """}}"""
        cm = ConnectionManager()
        sparql = cm.graphdb_connection(type="post")
        sparql.setMethod(POST)
        sparql.setQuery(query)
        sparql.setReturnFormat('json')
        result = sparql.query()
        if str(result.response.read().decode("utf-8")) == "":
            return "SUCCESS"
        return "FAIL"

