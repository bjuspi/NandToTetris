# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 06:16:51 2020

@author: bjusp
"""

class SymbolTable():
    def __init__(self):
        self.table = {}
        
    def addEntry(self, symbol, address):
        self.table[symbol] = address
    
    def contains(self, symbol):
        return (symbol in self.table.keys())
            
    def getAddress(self, symbol):
        return self.table[symbol]
        
    def addBuiltInSymbol(self):
        self.table["SP"] = 0
        self.table["LCL"] = 1
        self.table["ARG"] = 2
        self.table["THIS"] = 3
        self.table["THAT"] = 4
        self.table["SCREEN"] = 16384
        self.table["KBD"] = 24576
        
        for address in range(16):
            symbol = "R" + str(address)
            self.table[symbol] = address
