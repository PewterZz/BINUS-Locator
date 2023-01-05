class Node:

    def __init__(self, id, loc, type, dest, dist, chain):
        self.id = id
        self.loc = loc
        self.type = type
        self.dest = dest
        self.dist = dist
        self.chain = chain

    def isrestaurant(self):
        return self.type == 'restaurant'

    def isrecreational(self):
        return self.type == 'recreational'

    def getdest(self):
        return self.dest

    def getlat(self):
        return self.loc[0]

    def getlong(self):
        return self.loc[1]

    def getdist(self):
        return self.dist

    def getchain(self):
        return self.chain