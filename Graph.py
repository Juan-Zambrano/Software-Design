class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

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
    dfs_list = [] 
    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    dfs_list.append(self.Vertices[v].label)
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        dfs_list.append(self.Vertices[u].label)
        theStack.push(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return(dfs_list)

  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue ()
    bfs_list = [] 
    #mark vertex v as visited and make it current
    (self.Vertices[v]).visited = True
    current = v
    print(self.Vertices[v])
    bfs_list.append(self.Vertices[v].label)
    u = self.getAdjUnvisitedVertex(current)
    if(u == -1 and theQueue.isempty()):
        print(self.Vertices[current])
        bfs_list.append(self.Vertices[current].label)
    elif(u == -1):
        current = theQueue.dequeue()
        print(self.Vertices[current])
        bfs_list.append(self.Vertices[current].label)
    else:
        (self.Vertices[u]).visited = True
        theQueue.enqueue(u)
        
    while(not theQueue.isEmpty()):
      u = self.getAdjUnvisitedVertex(current)
      if(u == -1):
        current = theQueue.dequeue()
        print(self.Vertices[current])
        bfs_list.append(self.Vertices[current].label)
      else:
        (self.Vertices[u]).visited = True
        theQueue.enqueue(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return(bfs_list)

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    start = self.getIndex(fromVertexLabel)
    finish = self.getIndex(toVertexLabel)
    weight = self.adjMat[finish][start]
    if(weight == 0):
      return -1
    else:
      return(weight)

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    idx = self.getIndex(vertexLabel)
    neighbours = [] 
    u = self.getAdjUnvisitedVertex(idx)
    if(u == -1):
      return([])
    else:
      #print(u, self.Vertices[u])
      neighbours.append(u)
      (self.Vertices[u]).visited = True
      while(u != -1):
        u = self.getAdjUnvisitedVertex(idx)
        if(u == -1):
          pass
        else:
          #print(u, self.Vertices[u])
          neighbours.append(u)
          (self.Vertices[u]).visited = True
    return(neighbours)


  # get a copy of the list of vertices
  def getVertices (self):
    new_list = [] 
    for i in range(len(self.Vertices)):
      new_list.append(self.Vertices[i].label)
    return(new_list)
      

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    v1 = self.getIndex(fromVertexLabel)
    v2 = self.getIndex(toVertexLabel)
    weight = self.adjMat[v2][v1]
    if(weight == 0):
      return #do we just return if the edge doesn't exist
    else:
      self.adjMat[v2][v1] = 0
      self.adjMat[v1][v2] = 0


  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    v1 = self.getIndex(vertexLabel)

    #remove the vertex from the list of vertices    
    self.Vertices.remove(self.Vertices[v1])

    #removing the col
    for i in range(len(self.adjMat)):
     a = self.adjMat[i]
     a.pop(v1)
    
    #removing the row
    del(self.adjMat[v1])

#Delete edge and DFS
#try a graph where there are 4 verites and you have an edge from self to other vertex
#get edge weight 
#BFS 

             
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
  #print (numEdges)
  
  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    #print (edge)
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

  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()
  print (startVertex)
  # close file
  inFile.close()

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  print (startIndex)

  
  # do depth first search
  print ("\nDepth First Search from " + startVertex)
  print()
  dfs_list = cities.dfs (startIndex)
  print(i for i in dfs_list)

  # do breadth first search
  print("\nBreadth First Search from " + startVertex)
  print()
  bfs_list =  cities.bfs(startIndex)
  print(i for i in bfs_list)
  print()
  
  #getting edge weight #can weight be zero for an edge that exists
  print("Edge weight between Houston and Miami:")
  print(cities.getEdgeWeight("Houston","Miami"))
  print(" ")
  print("List of vertices: ")
  print(cities.getVertices())
  print(" ")
  cities.deleteEdge("Seattle","San Francisco")
  print(" ")
  #Deleting the vertex 
  cities.deleteVertex("Seattle")
  print()
  print("Verties after seattle has been deleted:")
  print()
  print(cities.getVertices())
  print()
  for i in range(len(cities.adjMat)):
    for j in range(len(cities.adjMat)):
      print(cities.adjMat[i][j], end = " ")
    print()
  print()
  if__name__ == "__main__"
    main()
 