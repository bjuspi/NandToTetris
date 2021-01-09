# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from parser import *
from symboltable import *
from code import *

def main():
    print("Start the assembling process")
    
    inputPath = "Rect.asm"
    outputPath = "Rect.hack"
    
    outputFile = open(outputPath ,"w")
    
    initialize()

    assemblyCodes = Parser(inputPath)
    
    while (assemblyCodes.hasMoreCommands()):
        print(assemblyCodes.commandType())
        if (assemblyCodes.commandType() == "L_COMMAND"):
            print(assemblyCodes.symbol())
            symbolTable.addEntry(assemblyCodes.symbol(), assemblyCodes.instructionIndex)
            assemblyCodes.advance()
        else:
            assemblyCodes.increment()
            assemblyCodes.advance()

    n = 16
    
    for instruction in assemblyCodes.instructions:
        print(instruction)
        if (instruction[0] == "@"):
            if symbolTable.contains(instruction[1:]):
                value = symbolTable.getAddress(instruction[1:])
                value = decimalToBinary(value)
            elif instruction[1:].isdigit():
                value = decimalToBinary(int(instruction[1:]))
            else:
                symbolTable.addEntry(instruction[1:], n)
                value = decimalToBinary(n)
                n += 1
            length = len(str(value))
            machineCode = "0" + ((15-length)*"0") + str(value)

        else:
            code = Code()
            if ("=" in instruction):
                dest = instruction.split("=")[0]
                dest = code.dest(dest)
                d = True
            else:
                dest = code.dest("")
                d = False
                
            if (";" in instruction):
                jump = instruction.split(";")[1]
                jump = code.jump(jump)
                j = True
            else:
                jump = code.jump("")
                j = False
                
            if (d&j):
                comp = instruction.split("=")[1].split(";")[0]
                comp = code.comp(comp)
            elif (d):
                comp = instruction.split("=")[1]
                comp = code.comp(comp)
            elif (j):
                comp = instruction.split(";")[0]
                comp = code.comp(comp)
            else:
                comp = code.comp(instruction)
                
            machineCode = "111" + comp + dest + jump
            
        outputFile.write(machineCode + "\n")
    
    assemblyCodes.close()
    outputFile.close()
    
def initialize():
    global symbolTable
    symbolTable = SymbolTable()
    symbolTable.addBuiltInSymbol()  
    
def decimalToBinary(decimal):  
    return bin(decimal).replace("0b", "")  
    
    
main()