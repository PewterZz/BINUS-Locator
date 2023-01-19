from collections import defaultdict

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
    num_vertices = len(graph)
    sptSet = defaultdict(lambda: False)

    dist = [MAX_INT] * num_vertices
    pred[src] = -1  # The predecessor of the source is set to -1

    dist[src] = 0

    for count in range(num_vertices):
        curVertex = minDistance(dist, sptSet)
        path[index].append(curVertex)
        sptSet[curVertex] = True

        for vertex in range(num_vertices):
            if ((sptSet[vertex] == False) and
                    (dist[vertex] > (dist[curVertex] +
                                     modifiedGraph[curVertex][vertex])) and
                    (graph[curVertex][vertex] != 0)):
                dist[vertex] = (dist[curVertex] + modifiedGraph[curVertex][vertex])
                pred[vertex] = curVertex  # Update the predecessor of vertex

    for vertex in range(num_vertices):
        distance[index].append(float(dist[vertex]))
        if src == 0:
            srcVertex[vertex].append(getPath(pred, src, vertex))


    


def BellmanFord(edges, graph, num_vertices):
    dist = [MAX_INT] * (num_vertices + 1)
    dist[num_vertices] = 0

    for i in range(num_vertices):
        edges.append([num_vertices, i, 0])

    for i in range(num_vertices):
        for (src, des, weight) in edges:
            if (dist[src] != MAX_INT) and (dist[src] + weight < dist[des]):
                dist[des] = dist[src] + weight

    return dist[0:num_vertices]


def JohnsonAlgorithm(graph, distance, path, vertices):
    count = 0
    edges = []

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    # Here, you will need to call the Bellman Ford function to calculate the modified weights
    modifyWeights = BellmanFord(edges, graph, len(graph))

    modifiedGraph = [[0 for x in range(len(graph))] for y in
                     range(len(graph))]

    # Here, you will need to update the modifiedGraph matrix using the modified weights
    # obtained from the Bellman Ford function
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                modifiedGraph[i][j] = (graph[i][j] + modifyWeights[i] - modifyWeights[j])

    # Here, you will need to call the Dijkstra function for each source vertex
    # and pass an empty dictionary as the `pred` parameter
    pred = defaultdict(lambda: -1)
    srcVertex = [[] for i in range(vertices)]
    for src in range(len(graph)):
        Dijkstra(graph, modifiedGraph, src, distance, count, path, pred, srcVertex)
        count += 1

    print(distance)
    return srcVertex