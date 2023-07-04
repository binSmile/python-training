#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'splitTickers' function below.
#
# The function accepts STRING baseFileName as parameter.
#

def splitTickers(baseFileName):
    outfiles = {}
    suffixes = ['uk', 'us', 'de']
    for s in suffixes:
        outfiles[s] = open(baseFileName + '.' + s, 'w')

    with open(baseFileName) as bf:
        for line in bf:
            ticker = line.strip()
            if ticker:
                if len(ticker.split('.')) > 1:
                    country = ticker.split('.')[1].lower()
                else:
                    country = 'us'
                outfiles[country].write(ticker+'\n')

    for o in outfiles:
        outfiles[o].close()


if __name__ == '__main__':
    baseFileName = input()

    splitTickers(baseFileName)
