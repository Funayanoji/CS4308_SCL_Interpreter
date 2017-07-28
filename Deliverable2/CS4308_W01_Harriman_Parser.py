'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: July 12, 2017

Title: Semester Project Deliverable 2
       Parser class for SCL Language Interpreter
'''

from CS4308_W01_Harriman_Scanner import *
from CS4308_W01_Harriman_LexicalRules import *

class Parser:
    '''
    Implementation of parser class
    '''

    def __init__(self, scannerObject):
        '''
        Constructor. The Parser is given a Scanner
        object to request lines from the file being read.
        '''
        self.scannerObject = scannerObject

    '''
    Method to get scanner's file name
    '''
    def getFileName(self):
        return self.scannerObject.getFileName()

    '''
    Method that throws an error when a Lexical Rule
    has been violated. The Parser also terminates
    calls to the Scanner.
    '''
    def throwError(self):
        print "\nError on line", self.scannerObject.getCurrentLineNum(), "-", self.scannerObject.getCurrentLine()
        print "Lexical Rule violated.\n"
        self.scannerObject.endFile()

    '''
    Main method parser - as long as there are lines
    to be read by the Scanner, the Parser requests them.

    The Parser passes each word in a line to the LexicalRules
    class to determine if it exists within the rules. If any
    word does not exist, or is not allowed in a particular statement,
    an error is thrown.
    '''
    def execute(self):
        while self.scannerObject.hasNext():
            validFlag = True
            self.scannerObject.readNext()
            if len(self.scannerObject.tokenizeCurrentLine(self.scannerObject.getCurrentLine())) > 0:
                if self.scannerObject.tokenizeCurrentLine(self.scannerObject.getCurrentLine())[0][1] in getRules():
                    for word in self.scannerObject.tokenizeCurrentLine(self.scannerObject.getCurrentLine())[1:]:
                        if word[1] in getRules()[self.scannerObject.tokenizeCurrentLine(self.scannerObject.getCurrentLine())[0][1]]:
                            pass
                        else:
                            print word[0], word[1]
                            validFlag = False
                    if not validFlag:
                        self.throwError()
                else:
                    print "Not found in Lexical Rules."
                    self.throwError()
        self.scannerObject.endFile()
            

    

