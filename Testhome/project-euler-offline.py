#!/usr/bin/env python
'''
project-euler-offline.py
Christopher Su
Checks solutions to Project Euler problems offline.
'''



import logging
import os
import json
from pyDes import *
import codecs

def loadJSON(jsonStr):
    try:
        data = json.loads(jsonStr)
    except ValueError:
        logging.exception("Error parsing %s." % json_file)
        sys.exit(1)
    return data

def main():
    dir = os.path.dirname(__file__)
    txtFile = codecs.open( os.path.join(dir, "solutions-encrypted"), "rb")
    txtStr = txtFile.read()
    print "loading data..."
    plain_text = triple_des('03b5660c7c16a07b').decrypt(txtStr, padmode=2)
    solutions = loadJSON(plain_text)
    l_solutions = sorted(map(int,solutions.keys()))
    current = raw_input("What problem are you currently working on? ")

    if current not in solutions:
        print "Sorry, not in solutions;",
        print "available solutions: 1 to", l_solutions[len(l_solutions)-1]
    else:
        while True:
            proposed = raw_input("\nEnter solution: ('exit'=exit)\n")
            if proposed == "exit":
                break
            elif proposed == solutions[current]:
                print "Correct!"
                current = raw_input("\nWhat problem are you working on? ")
                if current == "exit":
                    break
            else:
                print "Sorry, that is incorrect, should be:", solutions[current]

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    main()