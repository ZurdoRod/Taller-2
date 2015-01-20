'''
Created on 19/1/2015

@author: Carlos_Rodriguez_06-40189
'''
class Tarifas(object):

    td = 0
    tn = 0
    ti = 0
    

    def __init__(self, td, tn):
        self.td = td
        self.tn = tn
        if td > tn:
            self.ti = td
        else:
            self.ti = tn
        