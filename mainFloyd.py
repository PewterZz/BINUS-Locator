import os
import gmplot
import pandas as pd
import time
import Node
import floyd

#used to convert our node paths into an adjacency matrix
def initialize(adj, V):
    # Initialize a matrix
    matrix = [[0 for j in range(V)]
              for i in range(V)]

    for i in range(V):
        k = 0
        for j in adj[i].getdest():
            matrix[i][int(j)] = float(adj[i].getdist()[k])
            k += 1

    return matrix


#v needs to be the value of all the data in the csv, which starts from 0 so you will need to change it to the max id - 1
V = 22

#coords stores all the lat and long values like this [(lat, long), (lat, long), ...]
coords = []
i = 0
while(i < V):
    data = pd.read_csv("coords23.csv")
    #here after we read the data from the csv, we make a node from the class we made so that it can be easily used later on
    coords.append(Node.Node(int(data['id'][i]), data['loc'][i].split(','), data['type'][i], data['dest'][i].split(','), data['dist'][i].split(','), data['chain'][i].split(',')))
    i += 1

#making empty matrixes to prepare for later use
#not currently used
path = [[] for i in range(V)]
distance = [[] for i in range(V)]

#makes the adjacency matrix from our class nodes
adjMat = initialize(coords, V)


for i in range(len(adjMat)):
    for j in range(len(adjMat[i])):
        #we replace any 0's with INF because of the way this floyd warshall implementation works
        #it needs a really high value for comparison
        if adjMat[i][j] == 0:
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
            adjMat[i][j] = float('inf')

# print(adjMat)

#start time
st = time.time()
directions = [[0 for j in range(len(adjMat))] for i in range(len(adjMat))]

#floyd warshall takes an adjacency matrix as an argument and returns two values
#one that stores the shortest path to all nodes (distances) and another that stores the shortest path destinations (pred) 
#e.g. the value of the shortest path stored in distances from node 0 to node 5 is 150. You can tell what nodes were used
#by checking the pred array, it went from node 0 -> 1 -> 2 - > 3 -> 4 - > 5 which accounting for their individual distances
#amounted to 150 (! this is just an example)
distance, pred = floyd.floyd_warshall(adjMat)

# Print out the path in reverse order
print(path[::-1])

#end time
ed = time.time()

#total time
total_time = ed - st

lat = []
long = []
for i in coords:
    lat.append(float(i.getlat()))
    long.append(float(i.getlong()))

#googlemapplotter will start everything up, and the apikey parameter is used so that we can access the dev version of gmaps
gmapone = gmplot.GoogleMapPlotter(-6.224668378957205, 106.8039080855123, 19, apikey="AIzaSyB04QWbhqXqjeYz9nFZ3JnHrtNR86cxPZA")

#the scatter function is what we use to make the dots on the google map
gmapone.scatter(lat, long, "red", size=2, marker=False)

#here every coords in the csv is stored in the lat and long array and drawn into the gmap without any lines drawn on them
gmapone.scatter([lat[0]], [long[0]], "yellow", size=2, marker=False)

#marker is the little pointer above some of the endpoints
gmapone.marker(lat[0], long[0], color='yellow')


while(True):
    choice = int(input("What would you like to find ?: \n 1. Restaurant \n 2. Sports and Recreation \n 3. Else \n"))
    if(choice == 1):
        for i in coords:
            if i.isrestaurant():
                #the node here is the node that is the restaurant and we store this value because we want to know
                #the path that the algorithm took to get the shortest path to the restaurant
                node = i.id
                #this path array stores the path that the shortest path took. Even if there are other paths that lead to the 
                #location we use this to determine which path is actually the shortest from the context of the algorithm
                path = [node]
                while pred[0][node] is not None:
                    node = pred[0][node]
                    path.append(node)
                #reversed becaused the pred function starts from the last node
                path.reverse()
                #inserts 0 to the 0th index which is where all the paths start from
                path.insert(0, 0)
                #tlat and tlong stores the lat and long coords that are going to be drawin using gmplot
                tlat = []
                tlong = []
                for p in range(len(path)):
                    tlat.append(float(coords[int(path[p])].getlat()))
                    tlong.append(float(coords[int(path[p])].getlong()))

                #the shortest path is taken from the modified matrix that is returned from the algorithm
                #the shortest path from 0 to the current i.id (Restaurant)
                #if you want to read the modified matrix it works like this:
                #the value of matrix[0][11] shows the shortest path from node 0 to node 11
                #the value of matrix[4][12] shows the shortest path from node 4 to node 12
                #the value will be 0 if there doesnt exist a path between the two nodes
                print(f'Shortest path to Node {i.id} (Restaurant) is: {distance[0][i.id]}')

                #the plot function draws a line between a certain coordinate and another, we stored everything in an array
                #and thus with the order that we received from the algorithm we follow that same exact path
                gmapone.plot(tlat, tlong, 'cyan', edge_width=8)
                gmapone.marker(tlat[-1], tlong[-1], color='red', label='Restaurant')

    if (choice == 2):
        for i in coords:
            if i.isrecreational():
                node = i.id
                path = [node]
                while pred[0][node] is not None:
                    node = pred[0][node]
                    path.append(node)
                #reversed becaused the pred function starts from the last node
                path.reverse()
                #inserts 0 to the 0th index which is where all the paths start from
                path.insert(0, 0)
                tlat = []
                tlong = []
                for p in range(len(path)):
                    tlat.append(float(coords[int(path[p])].getlat()))
                    tlong.append(float(coords[int(path[p])].getlong()))

                #same as above description 
                print(f'Shortest path to Node {i.id} (Recreational) is: {distance[0][i.id]}')
                gmapone.plot(tlat, tlong, 'cyan', edge_width=8)
                gmapone.marker(tlat[-1], tlong[-1], color='red', label='Recreational')

    #prints total time
    print(f"Time taken: {total_time}")

    #makes a file called map.html based on what we have done so far
    gmapone.draw("map.html")
    break