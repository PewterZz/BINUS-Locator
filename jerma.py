import sys
from collections import defaultdict

#a really really high number
#this number exists as a pivot so that if a value exists in the matrix that is not infinity
#that means that a condition will run because infinity is supposed to describe a non path
#meaning that there is no path to that node
INF = 9999999

def floyd_warshall(adj_list):
    # Initialize the number of nodes
    num_nodes = len(adj_list)
    # Initialize the distances and predecessors matrix
    distances = [[INF for _ in range(num_nodes)] for _ in range(num_nodes)]
    print("The amount of memory this thing takes is : " + str(sys.getsizeof(distances)))

    predecessors = [[None for _ in range(num_nodes)] for _ in range(num_nodes)]
    
    # Fill in the distances matrix with the initial values from the adjacency list
    for node, edges in enumerate(adj_list):
        for neighbor, weight in edges:
            distances[node][neighbor] = weight
            # set the predecessor to be the current node
            predecessors[node][neighbor] = node
            
    # Iterate through all pairs of nodes
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                # Check if going through node k gives a shorter path
                # between node i and node j
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    #set the predecessor to be node k
                    predecessors[i][j] = predecessors[k][j]

    return distances, predecessors