'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: July 12, 2017 

Title: Semester Project Deliverable 2
       Scanner class for SCL Language Interpreter
'''

from LexicalAnalyzer import *
from Token import *

class Scanner:
    '''
    Implementation of scanner class
    '''

    def __init__(self, filename):
        '''
        Constructor. A file object is created
        and acts as the heart of the constructor.
        '''
        self.filename = filename
        with open(filename, 'r') as f:
            self.fileObject = f.read().splitlines()
        self.numLines = len(self.fileObject)
        self.currentLineNum = 0
        self.currentLine = self.fileObject[self.currentLineNum]
        self.withinComment = False

    '''
    Various getter methods
    '''
    def getFileName(self):
        return self.filename

    def getNumLines(self):
        return self.numLines

    def getCurrentLine(self):
        return self.currentLine

    def getCurrentLineNum(self):
        return self.currentLineNum

    def getLengthOfLine(self):
        return len(self.currentLine.split())
    
    def hasNext(self):
        return self.numLines - self.currentLineNum > 0

    def endFile(self):
        '''
        This method immediately moves the self.currentLineNum
        to the last line of the file. This will be utilized
        when an error has occurred, so the parser won't continue
        to call for more lines from the Scanner.
        '''
        self.currentLineNum = self.numLines
        print ("File is closed.")


    def tokenizeCurrentLine(self, line):
        '''
        Method to turn all words in a line into Tokens.
        Simultaneously checks for comments, which the Scanner
        will ignore.
        '''
        tokenizedLine = ""
        for word in line.split():
            '''
            If the Scanner encounters the beginning of a block
            comment, the Scanner ingored everything afterwards
            '''
            if tokenize(word).value == 4005:
                self.withinComment = True
                return ""
            if tokenize(word).value == 4006:
                self.withinComment = False
                return ""
            if tokenize(word).value == 4007:
                return (tokenizedLine)
            if not self.withinComment:
                tokenizedLine += ("\n    " + tokenize(word).toString())
        return (tokenizedLine)

    def readNext(self):
        '''
        Read the next line in the file, and
        update the current line number we're on.
        '''
        if self.hasNext():
            self.currentLine = self.fileObject[self.currentLineNum]
            self.currentLineNum += 1
