'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: June 27, 2017

Title: Semester Project Deliverable 1
       LexicalAnalyzer file for SCL Language Interpreter

Description: The lexicalAnalyzer is a dictionary of dictionaries.
             Each internal dictionary holds keywords, arithmetic
             operators, and tokens. Each key in each internal
             dictionary is assigned a random integer value, which
             the Parser will use later.
'''

import re
from CS4308_W01_Harriman_Token import *

lexicalAnalyzer = {
    "keywords" : {
        'array' : 8000,
        'begin' : 8001,
        'constant' : 8002,
        'declarations' : 8003,
        'display' : 8004,
        'do' : 8005,
        'else' : 8006,
        'endfun' : 8007,
        'endif' : 8008,
        'endrepeat' : 8009,
        'endwhile' : 8010,
        'enum' : 8011,
        'forward' : 8012,
        'function' : 8013,
        'global' : 8014,
        'if' : 8015,
        'implementations' : 8016,
        'integer' : 8017,
        'main' : 8018,
        'parameters' : 8019,
        'pointer' : 8020,
        'references' : 8021,
        'repeat' : 8022,
        'return' : 8023,
        'set' : 8024,
        'specifications' : 8025,
        'struct' : 8026,        
        'symbol' : 8027,
        'then' : 8028,
        'type' : 8029,
        'until' : 8030,
        'while' : 8031
        },
    
    "arithOps" : {
        '+' : 6000,
        '-' : 6001,
        '*' : 6002,
        '\\' : 6003,
        '>' : 6004,
        '<' : 6005,
        '>=' : 6006,
        '<=' : 6007,
        '==' : 6008,
        '~=' : 6009,
        '=' : 6010
        },

    "tokens" : {
        '\\(' : 4000,           # open parenthesis
        '\\)' : 4001,           # close parenthesis
        '\"' : 4002,            # double quote
        '\[([a-zA-Z]|([\-]?[0-9]?.[0-9]))+\]' : 4003, # brackets containing words/numbers
        '[\-]?[0-9]' : 4004,    # all numbers, including negative numbers
        '\/\*' : 4005,          # Beginning of block comment
        '\*\/' : 4006,          # End of block comment
        '\/\/' : 4007,          # line comment
        '\[\]' : 4008,          # empty brackets
        '\,' : 4009,            # comma
        '\s+' : 4010,           # whitespace
        '[a-zA-Z]+' : 4011      # alpha word
        
        }
    
    }

# Method to turn a word from the file into a Token.
def tokenize(word):
    numericalValue = 0

    # Test to see if word is a keyword.
    if word in lexicalAnalyzer["keywords"]:
        newToken = Token(word, "keyword", lexicalAnalyzer["keywords"][word])
        return newToken

    # Test to see if word is an arithmetic operator
    if word in lexicalAnalyzer["arithOps"]:
        newToken = Token(word, "arithmetic operator", lexicalAnalyzer["arithOps"][word])
        return newToken

    '''
    Test to see if the word is a token. Cycle through
    the keys of the "tokens" dictionary, using the keys as
    regular expressions tests. If there is a match, grab
    the value.
    '''
    for subkey in lexicalAnalyzer["tokens"].keys():
        if re.match(subkey, word):
            numericalValue = lexicalAnalyzer["tokens"][subkey]

    # If numericalValue is 0, then it has fallen through all the tests,
    # which means it was not matched with anything.
    if numericalValue == 0:
        return "No match found."
    newToken = Token(word, "token", numericalValue)
    return newToken

