import numpy as np
import time

from queue import PriorityQueue

def johnsons_algorithm(adj_matrix):
    n = len(adj_matrix)
    # Step 1: Initialize distance matrix
    D = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        D[i][i] = 0

    # Step 2: Initialize priority queue
    pq = PriorityQueue()
    for i in range(n):
        pq.put((0, i))

    # Steps 3-7: Perform Bellman-Ford
    while not pq.empty():
        dist, u = pq.get()
        for v in range(n):
            if adj_matrix[u][v] != float('inf'):
                if D[u][v] > dist + adj_matrix[u][v]:
                    D[u][v] = dist + adj_matrix[u][v]
                    pq.put((D[u][v], v))

    return D


array = [[10]*100 for i in range(100)]


start = time.time()
johnsons_algorithm(array)
end = time.time()

el = end - start

print(el)
