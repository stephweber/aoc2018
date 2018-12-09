# import re
import numpy as np

def readFile(file):

    with open(file, 'r') as f:
    
        # Read in input file
        claims = [line.strip() for line in f if line]

    return claims

def overlap(file):
    # List all claims
    claims = readFile(file)

    xPosition = []
    yPosition = []
    xDim = []
    yDim = []

    # For each claim, find position and dimensions
    for item in claims:
        # pattern = 
        # re.match(pattern,item,flags=0) 

        # Parse string 
        p1 = item.split(' ')
        p2 = p1[2].split(',')
        p2[1] = p2[1].replace(':','')
        p3 = p1[3].split('x')
        xPosition.append(int(p2[0]))
        yPosition.append(int(p2[1]))
        xDim.append(int(p3[0]))
        yDim.append(int(p3[1]))

    # Find max lower right corner of all claims
    maxX = max([p + d for p, d in zip(xPosition, xDim)])
    maxY = max([p + d for p, d in zip(yPosition, yDim)])

    # Create fabric
    fabric = np.zeros((maxX,maxY))

    # Increase value in each square inch for each claim 
    for i in range(0,len(xPosition)):
        fabric[xPosition[i]:(xPosition[i]+xDim[i]), yPosition[i]:(yPosition[i]+yDim[i])] += 1

    # Count number of inches in more than 1 claim
    overlap = np.sum(fabric>1)
    
    # Find claim with no overlaps
    for i in range(0,len(claims)):
        claim = fabric[xPosition[i]:(xPosition[i]+xDim[i]), yPosition[i]:(yPosition[i]+yDim[i])]
        if np.all(claim==1):
            nonoverlap = i
            break

    return overlap, nonoverlap+1

print(overlap('day3input.txt'))
# print(overlap('test.txt'))

    

    