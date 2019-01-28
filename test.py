import math, sys

#Generates successors for supplied value
def successors(val):
    ret = []

    if (val &lt= 200):
        try:
            ret.append([math.factorial(val), 1])
        except:
            pass

    #Exception when values are not kosher I guess
    try:
        ret.append([math.floor(val), 2])
    except:
        ret.append([int(val), 2])

    if (val  0 and queue[0][0] != goal:
        current = queue.pop(0)

        for x in successors(current[0]):
            if not x[0] in seen:
                queue.append(x)
                seen[x[0]] = current

    #For some reason, 12 doesn't work...
    if (len(queue) == 0):
        print "Failed to find steps..."
        return None

    #Converts the data structures to the series of steps that the algorithm found
    print "Generating steps..."
    done = False
    steps = [queue[0]]
    step = queue[0][0]
    while not done:
        if step != 4:
            steps.append(seen[step])
            step = seen[step][0]
        else:
            done = True

    steps.reverse()
    return steps

s = bfs(int(sys.argv[1]))
if not s == None:
    for x in s:
        if x[1] == None:
            print "Start: " + str(x[0])
        elif x[1] == 1:
            print "Factorial: " + str(x[0])
        elif x[1] == 2:
            print "Floor: " + str(x[0])
        elif x[1] == 3:
            print "Square Root: " + str(x[0])