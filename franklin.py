from collections import defaultdict
import time
import sys

MAX_INT = float('Inf')


def minDistance(dist, visited):
    (minimum, minVertex) = (MAX_INT, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and visited[vertex] == False:
            (minimum, minVertex) = (dist[vertex], vertex)

    return minVertex

def getPath(pred, src, des):
    if pred[des] == -1:
        return str(des)
    return getPath(pred, src, pred[des]) + ',' + str(des)

def Dijkstra(graph, modifiedGraph, src, distance, index, path, pred, srcVertex):
    subtime = 0
    num_vertices = len(graph)
    sptSet = defaultdict(lambda: False)

    dist = [float('inf')] * num_vertices
    pred[src] = -1

    dist[src] = 0
    path[index].append(src)

    for count in range(num_vertices-1):
        curVertex = minDistance(dist, sptSet)
        sptSet[curVertex] = True

        for des, weight in graph[curVertex]:
            if ((sptSet[des] == False) and
                    (dist[des] > (dist[curVertex] + weight))):
                dist[des] = dist[curVertex] + weight
                pred[des] = curVertex
                path[index].append(des)
    for vertex in range(num_vertices):
        distance[index].append(dist[vertex])
        start = time.time()
        srcVertex[vertex].append(getPath(pred, src, vertex))
        end = time.time()
        elapsed = end - start
        subtime += elapsed

    return subtime
    

def BellmanFord(edges, graph, num_vertices):
    dist = [float('inf')] * (num_vertices)
    dist[num_vertices-1] = 0
    for i in range(num_vertices-1):
        for src, value in enumerate(graph):
            for des, weight in value:
                if dist[src] + weight < dist[des]:
                    dist[des] = dist[src] + weight
    return dist

def JohnsonAlgorithm(graph, distance, path, vertices):
    count = 0
    subtime = 0
    edges = []

    # Create a list of edges using the adjacency list representation
    for i in range(len(graph)):
        for j in graph[i]:
            edges.append([i, j[0], j[1]])

    # Here, you will need to call the Bellman Ford function to calculate the modified weights
    modifyWeights = BellmanFord(edges, graph, len(graph))

    # Create an empty list to represent the modified graph
    modifiedGraph = [[] for y in range(len(graph))]

    # Here, you will need to update the modifiedGraph list using the modified weights
    # obtained from the Bellman Ford function
    for i in range(len(graph)):
        for j in graph[i]:
            modifiedGraph[i].append((j[0], (j[1] + modifyWeights[i] - modifyWeights[j[0]])))

    # Here, you will need to call the Dijkstra function for each source vertex
    # and pass an empty dictionary as the `pred` parameter
    pred = defaultdict(lambda: -1)
    srcVertex = [[] for i in range(vertices)]
    print("The amount of memory this thing takes is : " + str(sys.getsizeof(srcVertex)))
    for src in range(len(graph)):
        subtime += Dijkstra(graph, modifiedGraph, src, distance, count, path, pred, srcVertex)
        count += 1
    return srcVertex, subtime