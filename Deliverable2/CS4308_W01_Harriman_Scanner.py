'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: July 12, 2017

Title: Semester Project Deliverable 2
       Scanner class for SCL Language Interpreter
'''

from CS4308_W01_Harriman_LexicalAnalyzer import *
from CS4308_W01_Harriman_Token import *

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
        Method to turn all words in a line into Tokens. For Deliverable 2,
        the tokenizedLine to be returned is a list of the tokens' original words
        and numerical values as a tuple, as opposed to a string to represent
        a sentence, as it was in Deliverable 1.
        
        This method also checks for and ignores block comments and all words
        after a line comment that start with '//'.
        '''
        tokenizedLine = []
        for word in line.split():
            '''
            If the Scanner encounters the beginning of a block
            comment, the Scanner ingores everything afterwards
            '''
            if tokenize(word).value == 4005:  # this is the value for /*
                self.withinComment = True
                return ""
            
            if tokenize(word).value == 4006:  # this is the value for */, 
                self.withinComment = False    # therefore, we're out of the comment
                return ""
            
            if tokenize(word).value == 4007:  # this is the value for //, a line comment;
                return (tokenizedLine)        # therefore, anything following can be ignored
            
            if not self.withinComment:        # if we're not within a comment, tokenize
                tokenizedLine.append(tokenize(word).toString())
        return (tokenizedLine)

    def readNext(self):
        '''
        Read the next line in the file, and
        update the current line number we're on.
        '''
        if self.hasNext():
            self.currentLine = self.fileObject[self.currentLineNum]
            self.currentLineNum += 1
