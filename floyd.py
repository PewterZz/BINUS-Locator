#a really really high number
#this number exists as a pivot so that if a value exists in the matrix that is not infinity
#that means that a condition will run because infinity is supposed to describe a non path
#meaning that there is no path to that node
#for example, this adjacency matrix
# [[INF, 1, INF],
#  [1, INF, INF],
#  [INF, INF, INF]]
#tells us there is only one path in the graph which is from node 0 to node 1 as everything else is INF
#matrix[0][1] == 1, matrix[1][0] == 1
INF = 999

#the floyd warshall algorithm with running time O(V^3) where V is the number of vertexes (nodes) in the graph
def floyd_warshall(graph):
  # Initialize distances to be the same as the input graph
  #this distances array stores the shortest path of all nodes in the graph
  #it is what we are returning later on
  #it is also why this algorithm is considered a dynamic algorithm
  #go further down to see more details and context as to why
  distances = list(map(lambda i : list(map(lambda j : j, i)), graph))

  # Initialize the number of nodes
  num_nodes = len(distances)

  # Initialize the predecessor matrix
  predecessors = [[None for _ in range(num_nodes)] for _ in range(num_nodes)]

  # Iterate through all pairs of nodes
  #when we do a triple iteration over the distances array, we make sure to check the values of each node from time to time
  #this algorithm iterates a lot of times and through that it is able to check what the values in the distances array are
  #when calculating some point if the algorithm discovers that it already has a value in a certain index
  #it will use that value to calculate the shortest path from that index to the current/next
  #this process is known as relaxing the graph as it possibly eases up the calculations for the next iterations each time it happens
  for k in range(num_nodes):
    for i in range(num_nodes):
      for j in range(num_nodes):
        # Check if going through node k gives a shorter path
        # between node i and node j
        if distances[i][k] + distances[k][j] < distances[i][j]:
            distances[i][j] = distances[i][k] + distances[k][j]
            #predecessors stores the previous value of the node, which will be used later on outside
            #to get the shortest path direction
            predecessors[i][j] = k

  return distances, predecessors