'''
@author-name: Rishab Katta
@author-name: Akhil Karrothu
'''
from graph import Graph
from searchAlgos import *
import sys

lolmaze = []


def get_neighbors(ip_i, ip_j):
    '''
    get_neighbors returns the neighboring vertices of the vertex sent as function parameters
    :param ip_i: Index position i
    :param ip_j: Index position j
    :return:
    '''
    if lolmaze[ip_i][ip_j] == "*":
        return []

    neighbors = []

    # moving up
    i = ip_i
    j = ip_j
    rockbool = False
    while i >= 0:
        if (lolmaze[i][ip_j] == "*"):
            rockbool = True
            if (i + 1) != ip_i:
                neighbors.append(str(i + 1) + "," + str(ip_j))
                break
        i -= 1
    if rockbool == False:
        if ip_i != 0:
            neighbors.append(str(0) + "," + str(ip_j))

    # moving down
    i = ip_i
    j = ip_j
    rockbool = False
    while i < len(lolmaze):
        if (lolmaze[i][ip_j] == "*"):
            rockbool = True
            if (i - 1) != ip_i:
                neighbors.append(str(i - 1) + "," + str(ip_j))
                break
        i += 1
    if rockbool == False :
        if ip_i != len(lolmaze) - 1:
            neighbors.append(str(len(lolmaze) - 1) + "," + str(ip_j))


    # moving right
    i = ip_i
    j = ip_j
    rockbool = False
    while j < len(lolmaze[ip_i]):
        if (lolmaze[ip_i][j] == "*"):
            rockbool = True
            if (j - 1) != ip_j:
                neighbors.append(str(ip_i) + "," + str(j - 1))
                break
        j += 1
    if rockbool == False:
        if ip_j != len(lolmaze[ip_i]) - 1:
            neighbors.append(str(ip_i) + "," + str(len(lolmaze[ip_i]) - 1))

    # moving left
    rockbool = False
    i = ip_i
    j = ip_j
    while j >= 0:
        if (lolmaze[ip_i][j] == "*"):
            rockbool = True
            if (j + 1) != ip_j:
                neighbors.append(str(ip_i) + "," + str(j + 1))
                break
        j -= 1
    if rockbool == False:
        if ip_j != 0:
            neighbors.append(str(ip_i) + "," + str(0))



    return neighbors


def main():
    '''
    main is used to read the file, get the neighbors by calling get_neighbors function, create a graph and find
    the shortest path between 2 vertices using BFS and display the output
    :return:
    '''


    try:
        file = str(sys.argv[1])
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if any(char.isdigit() for char in line):
                    list2 = line.split(" ")
                    heightofpond = int(list2[0])
                    widthofpond = int(list2[1])
                    escaperow = int(list2[2])
                if not any(char.isdigit() for char in line):
                    list1 = line.split(" ")
                    lolmaze.append(list1)
    except:
        print("give a proper filename as a command line argument")
        sys.exit(0)

    #get neighbors and create a graph by using Graph module
    icemaze = Graph()
    for i in range(0, len(lolmaze)):
        for j in range(0, len(lolmaze[i])):
            neighbors = get_neighbors(i, j)
            state = str(i) + "," + str(j)
            for neighbor in neighbors:
                icemaze.addEdge(state, neighbor)

    escapevert = str(escaperow) + "," + str(widthofpond - 1)

    #find how many moves required to get to the escape point using BFS and put it in a dictionary based on that order
    paths = {}
    for startvert in icemaze.getVertices():
        path = []
        listofvert = []
        list1 = []
        path = findShortestPath(icemaze.getVertex(startvert), icemaze.getVertex(escapevert))
        if path is not None:
            key = len(path) - 1
            listofvert.append(startvert)
            if key == 0:
                key = 1
            if key not in paths.keys():
                paths[key] = listofvert
                continue
            if key in paths.keys():
                list1 = paths.get(key)
                list1 = list(set(list1 + listofvert))
                paths.update({key: list1})
        if path is None or len(path) == 0:
            key = "No path"
            listofvert.append(startvert)
            if key not in paths.keys():
                paths[key] = listofvert
                continue
            if key in paths.keys():
                list1 = paths.get(key)
                list1 = list(set(list1 + listofvert))
                paths.update({key: list1})

    #print the output
    for key in paths.keys():
        print(str(key) + " : " + str(paths.get(key)))


if __name__ == '__main__':
    main()