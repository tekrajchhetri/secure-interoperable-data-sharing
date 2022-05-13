# -*- coding: utf-8 -*-
# @Time    : 13.05.22 12:48
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : legal_engine.py
# @Software: PyCharm

class LegalEngine:
    def hasConsent(self, data):
        """For our study we assume that there's consent.
        This is were you'd integrate to other platforms such as https://doi.org/10.3390/s22072763 which handles consent
        :param data:
        :return:
        """
        return False