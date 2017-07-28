'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: July 12, 2017

Title: Semester Project Deliverable 2
       LexicalRules file for SCL Language Interpreter

Description: The LexicalRules are housed as a dictionary
             whose values are the numerical values of the
             possible keywords that can start a statement.
             Each key's values hold the numerical values of
             the allowable tokens, arithmetic operators, etc.
             that can follow.
'''

import re
from Token import *

lexicalRules = {

    # any word : any number, [], =, comma, array, type, integer
    4011 : [4004, 4008, 4009, 4011, 6010, 8000, 8023, 8037],

    # begin
    8001 : [],

    # constants
    8002 : [],

    # define : bracketed words/numbers, any number, any word, [], =, array, type, integer
    8004 : [4003, 4004, 4011, 4008, 6010, 8000, 8023, 8037],

    # display : double quotes, comma, any word
    8005 : [4002, 4009, 4011],

    # endfor
    8008 : [],

    # endfun : any word
    8009 : [4011, 8025],

    # endif
    8010 : [],

    # endwhile
    8012 : [],

    # exit
    8014 : [],

    # for : any number, any word, =, do, to
    8015 : [4004, 4011, 6010, 8006, 8036],

    # forward : declarations
    8016 : [8003],

    # function : any word, integer, is, main, return, type
    8017 : [4011, 8023, 8024, 8025, 8030, 8037],

    # global : declarations
    8018 : [8003],

    # if : bracketed words/numbers, any word, >, <, >=, <=, ==, ~=, =
    8019 : [4003, 4011, 6004, 6005, 6006, 6007, 6008, 6009, 6010],

    # implementations
    8020 : [],

    # import : double quotes, any word
    8021 : [4002, 4004, 4011],

    # input : double quotes, bracketed words/numbers, commas, any word
    8022 : [4002, 4003, 4009, 4011, 8036],

    # is
    8024 : [],

    # parameters
    8026 : [],

    # return : any word
    8030 : [4011],

    # set : (, ), bracketed words/numbers, any number, comma, any word, +, -, *, >, <, >=, <=, ==, ~=, =
    8031 : [4000, 4001, 4003, 4004, 4008, 4009, 4011, 6000, 6001, 6002, 6004, 6005, 6006, 6007, 6008, 6009, 6010],

    # symbol : any word or number
    8034 : [4004, 4011],

    # then
    8035 : [],

    # variables
    8039 : [],
    
    # while : any word, >, <, >=, <=, ==, ~=, =, do
    8040 : [4011, 6004, 6005, 6006, 6007, 6008, 6009, 6010, 8006]
    }

def getRules():
    return lexicalRules
