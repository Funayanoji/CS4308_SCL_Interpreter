'''
Author: Margaret Harriman
Class: CS 4308 W01
School: Kennesaw State University
Professor: Dr. Jose Garrido
Date: June 27, 2017

Title: Semester Project Deliverable 1
       This is the main program to
       test Scanner and view results
'''

from CS4308_W01_Harriman_Scanner import *


# Instantiate a new Scanner object
# Create a new text file to store printed results
myScanner = Scanner('sclex1.scl')
results = open('results.txt', 'w')

#Header information
print ("Filename:", myScanner.getFileName())
print ("Number of Lines:", myScanner.getNumLines())
print ("BEGIN READING FILE\n\n")

# Loop through lines in file, printing to console and writing to 'results.txt' file
while myScanner.hasNext():
    myScanner.readNext()
    print "CURRENT LINE #", myScanner.getCurrentLineNum(), "-", myScanner.getCurrentLine().strip()
    print myScanner.tokenizeCurrentLine(myScanner.getCurrentLine())
    print "======================="
    
    results.write(("\nCURRENT LINE # " + str(myScanner.getCurrentLineNum()) + " - " + myScanner.getCurrentLine().strip()))
    results.write(("\n" + myScanner.tokenizeCurrentLine(myScanner.getCurrentLine())))
    results.write("\n=======================\n")
# Close file
results.close()
print ("END OF FILE")
