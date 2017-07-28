'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: July 12, 2017

Title: Semester Project Deliverable 2
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
    
    "keywords" : {
        'array' : 8000,
        'begin' : 8001,
        'constants' : 8002,
        'declarations' : 8003,
        'define' : 8004,
        'display' : 8005,
        'do' : 8006,
        'else' : 8007,
        'endfor' : 8008,
        'endfun' : 8009,
        'endif' : 8010,
        'endrepeat' : 8011,
        'endwhile' : 8012,
        'enum' : 8013,
        'exit' : 8014,
        'for' : 8015,
        'forward' : 8016,
        'function' : 8017,
        'global' : 8018,
        'if' : 8019,
        'implementations' : 8020,
        'import' : 8021, 
        'input' : 8022,
        'integer' : 8023,
        'is' : 8024, 
        'main' : 8025,
        'parameters' : 8026,
        'pointer' : 8027,
        'references' : 8028,
        'repeat' : 8029,
        'return' : 8030,
        'set' : 8031,
        'specifications' : 8032,
        'struct' : 8033,        
        'symbol' : 8034,
        'then' : 8035,
        'to' : 8036,
        'type' : 8037,
        'until' : 8038,
        'variables' : 8039,
        'while' : 8040
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

    '''
    If numericalValue is 0, then it has fallen through all the tests,
    which means it was not matched with anything.
    '''
    if numericalValue == 0:
        return "No match found."
    newToken = Token(word, "token", numericalValue)
    return newToken

