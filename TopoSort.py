
class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push(self,item):
        self.stack.append(item)

      # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

      # check what item is on top of the stack without removing it
    def peek (self):
        return self.stack[len(self.stack) - 1]

      # check if a stack is empty
    def isEmpty (self):
        return (len(self.stack) == 0)

      # return the number of elements in the stack
    def size (self):
        return (len(self.stack))

class Queue (object):
    def __init__ (self):
        self.queue = []

    def enqueue (self, item):
        self.queue.append (item)

    def dequeue (self):
        return (self.queue.pop(0))

    def isEmpty (self):
        return (len (self.queue) == 0)

    def size (self):
        return len (self.queue)

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def wasVisited (self):
        return self.visited

    # determine the label of the vertex
    def getLabel (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)




class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex already exists in the graph
    def hasVertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).label):
                return True
        return False

    # given a label get the index of a vertex
    def getIndex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if ((self.Vertices[i]).label == label):
                return i
        return -1

  # add a Vertex with a given label to the graph
    def addVertex (self, label):
        if not self.hasVertex (label):
            self.Vertices.append (Vertex(label))

        # add a new column in the adjacency matrix for the new Vertex
        nVert = len(self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new Vertex in the adjacency matrix
        newRow = []
        for i in range (nVert):
            newRow.append (0)
        self.adjMat.append (newRow)

    # add weighted directed edge to graph
    def addDirectedEdge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def addUndirectedEdge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v
    def getAdjUnvisitedVertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
                return i
        return -1

    # do the depth first search in a graph
    def dfs (self, v):
        # create a Stack
        theStack = Stack()

        # mark vertex v as visited and push on the stack
        (self.Vertices[v]).visited = True
        return self.Vertices [v]
        theStack.push (v)

        # vist other vertices according to depth
        while (not theStack.isEmpty()):
            # get an adjacent unvisited vertex
            u = self.getAdjUnvisitedVertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                return self.Vertices[u]
                theStack.push(u)
        # the stack is empty let us reset the falgs
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do breadth first search in a graph
    def bfs (self, v):
    # create a Queue
        theQueue = Queue ()
        (self.Vertices[v]).visited = True
        return self.Vertices[v]
        theQueue.enqueue(v)
        while(not theQueue.isEmpty()):
            v1 = theQueue.dequeue()
            v2 = self.getAdjUnvisitedVertex(v1)
            while(v2 != -1):
                (self.Vertices[v2]).visited == True
                return self.Vertices[v2]
                theQueue.enqueue(v2)
                v2 = self.getAdjUnvisitedVertex(v1)
        #queue is empty so reset the flag
        for i in range (len(self.Vertices)):
            (self.Vertices[i]).visted = False

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
        if (self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] != 0):
            return self.adjMat[self.getIndex(toVertexLabel)][self.getIndex(toVertexLabel)]
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def getNeighbors (self, vertexLabel):
        neigh_ls = []
        index = self.getIndex(vertexLabel)
        for i in range(len(self.adjMat[index])):
            if(self.adjMat[index][i] != 0):
                neigh_ls.append(self.Vertices[i])
        return neigh_ls

    # get a copy of the list of vertices
    def getVertices (self):
        c = self.Vertices[:]
        return c

    # delete an edge from the adjacency matrix
    def deleteEdge (self, fromVertexLabel, toVertexLabel):
        self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def deleteVertex (self, vertexLabel):
        for i in range(len(self.Vertices)):
            for j in range(self.getIndex(vertexLabel),(len(self.Vertices) - 1)):
                self.adjMat[i][j] = self.adjMat[i][j + 1]
            self.adjMat[i].pop()
        self.adjMat.pop()
        for i in self.Vertices:
            if(i.label == vertexLabel):
                self.Vertices.remove(i)









def main():
    # create a Graph object
    cities = Graph()

    # open file for reading
    inFile = open ("./graph.txt", "r")

    # read the Vertices
    numVertices = int ((inFile.readline()).strip())
    print (numVertices)

    for i in range (numVertices):
        city = (inFile.readline()).strip()
        print (city)
        cities.addVertex (city)

    # read the edges
    numEdges = int ((inFile.readline()).strip())
    print (numEdges)

    for i in range (numEdges):
        edge = (inFile.readline()).strip()
        print (edge)
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.addDirectedEdge (start, finish, weight)

    # print the adjacency matrix
    print ("\nAdjacency Matric")
    for i in range (numVertices):
        for j in range (numVertices):
            print (cities.adjMat[i][j], end = ' ')
        print ()
    print ()

    if (cities.toposort() == None):
        print ('Error: Graph has cycle.')
    else:
        for i in range(stack.size()):
            print (cities.Vertices[stack.pop()])
        print()

main()
