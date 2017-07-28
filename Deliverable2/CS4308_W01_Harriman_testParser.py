'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: July 12, 2017

Title: Semester Project Deliverable 2

Description: This is the main program to
             test Parser and view results
'''

from CS4308_W01_Harriman_Scanner import *
from CS4308_W01_Harriman_Parser import *

'''
A Scanner object is created to read the test
program file and to feed into the Parser object.
'''

scnr = Scanner('sclex1.scl')
prsr = Parser(scnr)

'''
For this deliverable, the Parser simply requests each line
from the Scanner using its execute() method, until the end
of the file is reached, or an error is encountered. If
there is an error, it will print to console and the file
will be closed. Otherwise, the end of the file will be reached.
'''

prsr.execute()
