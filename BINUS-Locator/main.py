import os
import gmplot
import pandas as pd
import time
import Node
import johnson

def convert(adj, V):
    # Initialize a matrix
    matrix = [[0 for j in range(V)]
              for i in range(V)]

    for i in range(V):
        k = 0
        for j in adj[i].getdest():
            matrix[i][int(j)] = float(adj[i].getdist()[k])
            k += 1

    return matrix

V = 13
coords = []
i = 0
while(i < V):
    data = pd.read_csv("BINUS-Locator\coords23.csv")
    coords.append(Node.Node(int(data['id'][i]), data['loc'][i].split(','), data['type'][i], data['dest'][i].split(','), data['dist'][i].split(','), data['chain'][i].split(',')))
    i += 1

path = [[] for i in range(V)]
distance = [[] for i in range(V)]
adjMat = convert(coords, V)

st = time.time()
johnson.JohnsonAlgorithm(adjMat, distance, path)
ed = time.time()
total_time = ed - st

for i in distance:
    print(i)
lat = []
long = []
for i in coords:
    lat.append(float(i.getlat()))
    long.append(float(i.getlong()))

gmapone = gmplot.GoogleMapPlotter(-6.224668378957205, 106.8039080855123, 10, apikey="AIzaSyB04QWbhqXqjeYz9nFZ3JnHrtNR86cxPZA")
gmapone.scatter(lat, long, "red", size=2, marker=False)
gmapone.scatter([lat[0]], [long[0]], "yellow", size=2, marker=False)
gmapone.marker(lat[0], long[0], color='yellow')
# gmapone.plot(lat, long, 'blue', edge_width=11)

# gmapone.draw("map.html")

while(True):
    choice = int(input("What would you like to find ?: \n 1. Restaurant \n 2. Sports and Recreation \n 3. Else \n"))
    if(choice == 1):
        for i in coords:
            if i.isrestaurant():
                tlat = []
                tlong = []
                for j in coords:
                    # if j.isrestaurant():
                    #     break
                    for k in j.getchain():
                        if int(k) == i.id:
                            tlat.append(float(j.getlat()))
                            tlong.append(float(j.getlong()))
                tlat.append(float(i.getlat()))
                tlong.append(float(i.getlong()))
                print(f'Shortest path to Node {i.id} (Restaurant) is: {distance[0][i.id]}')
                gmapone.plot(tlat, tlong, 'blue', edge_width=11)
                gmapone.marker(tlat[-1], tlong[-1], color='red', label='Restaurant')

    if (choice == 2):
        for i in coords:
            if i.isrecreational():
                tlat = []
                tlong = []
                for j in coords:
                    for k in j.getchain():
                        if int(k) == i.id:
                            tlat.append(float(j.getlat()))
                            tlong.append(float(j.getlong()))
                tlat.append(float(i.getlat()))
                tlong.append(float(i.getlong()))
                gmapone.plot(tlat, tlong, 'green', edge_width=11)
                gmapone.marker(tlat[-1], tlong[-1], color='red')
    output_path = "algorithm/main/templates"
    file_name = "map.html"
    file_path = os.path.join(output_path, file_name)
    print(f"Time taken: {total_time}")
    gmapone.draw(file_path)
    break