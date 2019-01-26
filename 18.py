import cStringIO
import time
from little_help import *

# In this excersise we want to find max path, so to make it doable for Dijkstra, change biggest numbers to smallest, and opposite
bias = 1000

def parseGraph(raw):
    cRaw = cStringIO.StringIO(raw)

    weights = []
    # Adjacent list - index = node number, value is list of pairs in form (neighbourIdx, weight)
    adjacentList = []
    
    neighbourNodeIdx = 1
    
    # Convert weights to list of rows (and int values)
    line = cRaw.readline()
    while (line != ""):
        weights.append(map(lambda strWeight: bias - int(strWeight), line.split()))
        line = cRaw.readline()
        
    # Add epsilon node
    adjacentList.append([Neighbour(neighbourNodeIdx, weights[0][0])])
    
    y = 0
    while y < len(weights) - 1:
        current    = weights[y]
        neighbours = weights[y+1]
        
        neighbourNodeIdx += len(current)
        
        for cIdx in range(0, len(current)):
            cNeighbours = []
            cNeighbours.append(Neighbour(neighbourNodeIdx + cIdx, neighbours[cIdx]))
            cNeighbours.append(Neighbour(neighbourNodeIdx + cIdx + 1 , neighbours[cIdx + 1]))            
            adjacentList.append(cNeighbours)
        
        y += 1
    

    # Connect last row to eps node
    current = weights[len(weights) - 1]
    neighbourNodeIdx += len(current)
    
    for cIdx in range(0, len(current)):
        cNeighbours = []
        cNeighbours.append(Neighbour(neighbourNodeIdx, 0))         
        adjacentList.append(cNeighbours)
        
    # Add eps node
    adjacentList.append([])
    
    
    # for nodeIdx in range(0, len(adjacentList)):
        # print "Node ", nodeIdx, " neighbours ", adjacentList[nodeIdx]
    
    return adjacentList
    
def main():
    # testo = "\
# 3\n\
# 7 4\n\
# 2 4 6\n\
# 8 5 9 3"

    testo = "\
75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    
    
    testo = open('p067_triangle.txt', 'r').read()
    
    graph = parseGraph(testo)
    
    paths = shortestPath(graph, 0)
    
    path = []
    # Reconstruct path from last node
    prev = len(graph) - 1
    while (prev != 0):
        path.append(prev)
        prev = paths[prev]
    
    path.append(prev)
    path.reverse()
    #print "Path ", path
    
    sum = 0
    
    for node in range(len(path) - 1):
        for neighbor in graph[path[node]]:
            if (neighbor.idx == path[node+1]):
                if (neighbor.weight != 0):
                    corrected = bias - neighbor.weight
                    sum += corrected
        
    print sum  
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    
    print "Execution ", end - start
    
    
    
# Path  [0, 1, 2, 4, 8, 13, 19, 26, 33, 42, 51, 62, 73, 86, 100, 115, 131, 148, 166, 184, 203, 224, 245, 267, 291, 315, 341, 367, 395, 424, 453, 483, 515, 548, 582, 617, 653, 690, 728, 767, 806, 846, 888, 931, 974, 1019, 1065, 1112, 1160, 1209, 1258, 1308, 1359, 1412, 1465, 1520, 1576, 1632, 1689, 1747, 1806, 1867, 1928, 1990, 2054, 2119, 2185, 2252, 2320, 2388, 2458, 2528, 2599, 2671, 2744, 2818, 2893, 2970, 3047, 3125, 3205, 3286, 3367, 3449, 3532, 3616, 3701, 3788, 3875, 3963, 4052, 4143, 4234, 4327, 4421, 4515, 4611, 4708, 4806, 4904, 5004, 5051]
# 7273
