import os
import gmplot
import pandas as pd
import time
import Node
import johnson

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

V = 22
coords = []
i = 0
while(i < V):
    data = pd.read_csv("coords23.csv")
    coords.append(Node.Node(int(data['id'][i]), data['loc'][i].split(','), data['type'][i], data['dest'][i].split(','), data['dist'][i].split(','), data['chain'][i].split(',')))
    i += 1

path = [[] for i in range(V)]
distance = [[] for i in range(V)]
adjMat = initialize(coords, V)

#start time
st = time.time()

#the johnson algorithm takes an adjacency matrix, an empty distance and path array, and the number of vertexes in the graph
#it returns the shortest path direction matrix which is stored in spa (shortest path array)
#the empty distance array here stores the shortest path distances
spa = johnson.JohnsonAlgorithm(adjMat, distance, path, V)

#end time of the algorithm
ed = time.time()
total_time = ed - st

#used so that the values that are returned from spa are integers and seperated by a comma
#because the direct value of the function return is kinda bad
spa = [[int(x) for x in sublist[0].split(',')] for sublist in spa]

#stores the latitude and longitude coordinates
lat = []
long = []
#coords contains the values of the coordinates stored like this : [(lat, long), (lat, long), ...]
for i in coords:
    lat.append(float(i.getlat()))
    long.append(float(i.getlong()))

#starts the google map plotter used to make all the drawing work
gmapone = gmplot.GoogleMapPlotter(-6.224668378957205, 106.8039080855123, 19, apikey="AIzaSyB04QWbhqXqjeYz9nFZ3JnHrtNR86cxPZA")

#plots the points (circles)
gmapone.scatter(lat, long, "red", size=2, marker=False)
gmapone.scatter([lat[0]], [long[0]], "yellow", size=2, marker=False)

#plots the marker that is placed on the special types of places
gmapone.marker(lat[0], long[0], color='yellow')

#driver code
while(True):
    choice = int(input("What would you like to find ?: \n 1. Restaurant \n 2. Sports and Recreation \n 3. Else \n"))
    if(choice == 1):
        for i in coords:
            #checks to see if the current i.id is a restaurant or not
            if i.isrestaurant():
                tlat = []
                tlong = []
                for p in range(len(spa[i.id])):
                    print(coords[int(spa[i.id][p])].id)
                    tlat.append(float(coords[int(spa[i.id][p])].getlat()))
                    tlong.append(float(coords[int(spa[i.id][p])].getlong()))

                print(f'Shortest path to Node {i.id} (Restaurant) is: {distance[0][i.id]}')
                gmapone.plot(tlat, tlong, 'cyan', edge_width=8)
                gmapone.marker(tlat[-1], tlong[-1], color='red', label='Restaurant')

    if (choice == 2):
        for i in coords:
            if i.isrecreational():
                tlat = []
                tlong = []
                for p in range(len(spa[i.id])):
                    print(coords[int(spa[i.id][p])].id)
                    tlat.append(float(coords[int(spa[i.id][p])].getlat()))
                    tlong.append(float(coords[int(spa[i.id][p])].getlong()))

                tlat.append(float(i.getlat()))
                tlong.append(float(i.getlong()))
                print(f'Shortest path to Node {i.id} (Recreational) is: {distance[0][i.id]}')
                gmapone.plot(tlat, tlong, 'cyan', edge_width=8)
                gmapone.marker(tlat[-1], tlong[-1], color='red', label='Recreational')

    print(f"Time taken: {total_time}")
    gmapone.draw("map.html")
    break