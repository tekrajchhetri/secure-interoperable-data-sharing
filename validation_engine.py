# -*- coding: utf-8 -*-
# @Time    : 15.03.22 21:35
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : validation_engine.py
# @Software: PyCharm

class ValidationEngine:
    def data_quality_validation(self, input_rdf):
        """ perform validation of the received input data in RDF format for quality
        :param input_rdf: input data in RDF format <https://www.w3.org/TR/rdf11-concepts/>
        :return: boolean
        """
        return False

    def data_integrity_validator(self, input_rdf):
        """ Performs integrity checks of the data to ensure no data tampering is done
        :param input_rdf: input data in RDF format
        :return:
        """
        return False
