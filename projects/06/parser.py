# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 06:49:49 2020

@author: bjusp
"""

class Parser():
    def __init__(self, inputPath):
        self.inputFile = open(inputPath, "r")
        self.lines = self.inputFile.readlines()
        self.assemblyCodes = []
        self.index = 0
        self.type = ""
        self.instructionIndex = 0
        self.instructions = []
        
        for line in self.lines:
            assemblyCode = line.split("//")[0].replace(" ", "").rstrip()
            if (assemblyCode != ""):
                self.assemblyCodes.append(assemblyCode)
        
    def hasMoreCommands(self):
        return (self.index < len(self.assemblyCodes))
    
    def advance(self):
        self.index += 1
        
    def increment(self):
        self.instructionIndex += 1
        self.instructions.append(self.assemblyCodes[self.index])
    
    def commandType(self):
        initialCharacter = self.assemblyCodes[self.index][0]
        startingBracket = r"("
        if (initialCharacter == "@"):
            self.type = "A_COMMAND"
        elif (initialCharacter == startingBracket):
            self.type = "L_COMMAND"
        else:
            self.type = "C_COMMAND"
            
        return self.type
    
    def symbol(self):
        return self.assemblyCodes[self.index][1:-1]
    
    def dest(self):
        if (self.type == "C_COMMAND"):
            return self.assemblyCodes.split("=")[0]
    
    def comp(self):
        if (self.type == "C_COMMAND"):
            return self.assemblyCodes.split("=")[1].split(";")[0]
    
    def jump(self):
        if (self.type == "C_COMMAND"):
            if (len(self.assemblyCodes.split("=")[1].split(";")) > 1):
                return self.assemblyCodes.split("=")[1].split(";")[1] 
    
    def close(self):
        self.inputFile.close()    
        
        
parser = Parser("Max.asm")
print(parser.symbol())