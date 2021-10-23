#!/bin/python3

import math
import os
import random
import re
import sys

print(list(range(5,5)))
def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    result=0

    ic=min(initC,finalC)
    fc=max(initC,finalC)
    ir=min(initR,finalR)
    fr=max(initR,finalR)
  
    for r in range(ir,fr):
        result+=costRows[r]

    for c in range(ic,fc):
        result+=costCols[c]
            
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rows = int(input().strip())

    cols = int(input().strip())

    initR = int(input().strip())

    initC = int(input().strip())

    finalR = int(input().strip())

    finalC = int(input().strip())

    costRows_count = int(input().strip())

    costRows = []

    for _ in range(costRows_count):
        costRows_item = int(input().strip())
        costRows.append(costRows_item)

    costCols_count = int(input().strip())

    costCols = []

    for _ in range(costCols_count):
        costCols_item = int(input().strip())
        costCols.append(costCols_item)

    result = minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols)

    print("result=",result)
    #fptr.write(str(result) + '\n')

    #fptr.close()