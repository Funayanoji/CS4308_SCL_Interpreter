'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: June 27, 2017 

Title: Semester Project Deliverable 1
       Token class for SCL Language Interpreter
'''

import re

class Token:
    '''
    Implementation of Token class
    '''

    def __init__(self, word, tokenType, value):
        '''
        Constructor. Each Token holds its original
        word value, its tokenType ("keyword", etc.),
        and its numerical value for the Parser.
        '''
        self.word = word
        self.tokenType = tokenType
        self.value = value

    def toString(self):
        return ("Token: " + self.word + ", " + self.tokenType + ", " + str(self.value))
