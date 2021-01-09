# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:26:32 2020

@author: bjusp
"""

class Code():    
    def dest(self, dest):
        if (dest == ""):
            return "000"
        elif (dest == "M"):
            return "001"
        elif (dest == "D"):
            return "010"
        elif (dest == "MD"):
            return "011"
        elif (dest == "A"):
            return "100"
        elif (dest == "AM"):
            return "101"
        elif (dest == "AD"):
            return "110"
        elif (dest == "AMD"):
            return "111"
    
    def comp(self, comp):
        if (comp == "0"):
            return "0101010"
        elif (comp == "1"):
            return "0111111"
        elif (comp == "-1"):
            return "0111010"
        elif (comp == "D"):
            return "0001100"
        elif (comp == "A"):
            return "0110000"
        elif (comp == "M"):
            return "1110000"
        elif (comp == "!D"):
            return "0001101"
        elif (comp == "!A"):
            return "0110001"
        elif (comp == "!M"):
            return "1110001"
        elif (comp == "-D"):
            return "0001111"
        elif (comp == "-A"):
            return "0110011"
        elif (comp == "-M"):
            return "1110011"
        elif (comp == "D+1"):
            return "0011111"
        elif (comp == "A+1"):
            return "0110111"
        elif (comp == "M+1"):
            return "1110111"
        elif (comp == "D-1"):
            return "0001110"
        elif (comp == "A-1"):
            return "0110010"
        elif (comp == "M-1"):
            return "1110010"
        elif (comp == "D+A"):
            return "0000010"
        elif (comp == "D+M"):
            return "1000010"
        elif (comp == "D-A"):
            return "0010011"
        elif (comp == "D-M"):
            return "1010011"
        elif (comp == "A-D"):
            return "0000111"
        elif (comp == "M-D"):
            return "1000111"
        elif (comp == "D&A"):
            return "0000000"
        elif (comp == "D&M"):
            return "1000000"
        elif (comp == "D|A"):
            return " 0010101"
        elif (comp == "D|M"):
            return "1010101"
    
    def jump(self, jump):
        if (jump == ""):
            return "000"
        elif (jump == "JGT"):
            return "001"
        elif (jump == "JEQ"):
            return "010"
        elif (jump == "JGE"):
            return "011"
        elif (jump == "JLT"):
            return "100"
        elif (jump == "JNE"):
            return "101"
        elif (jump == "JLE"):
            return "110"
        elif (jump == "JMP"):
            return "111"