from random import randint
from graphics import *
import numpy as np
import math

Names = ['Abydos','Camelot','Delmak','Gaia','Edasich','Hadante','Tauri','Hadar','Icalurus','Juna','Kheb','Langara','Palilicium']
Occurence_name = [0]*len(Names)
NbPlanet = 150
NbLink = 20
planete = [None]*NbPlanet
saut = [None]*NbLink
MaxLink = 3
count = 0
Univers = [None]*10
Univers[0] = 1
Univers[1] = 3

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


class systeme:
    number = 0

    def __init__(self, dist, sec):
        self.number += 1
        self.rand = randint(0, len(Names)-1)
        self.name = Names[self.rand]
        self.occurence = Occurence_name[self.rand]
        self.linkNumber = 0
        self.linkTable = [None]*MaxLink
        self.distance = dist
        self.sec_status = sec
        self.totalweight = 0
        Occurence_name[self.rand] += 1

    def AddLink(self, i):
        if self.linkNumber <= MaxLink:
            self.linkTable[self.linkNumber] = i
            self.linkNumber += 1
            return self.linkNumber
        else:
            return -1

    def Addtotalweight(self):
        self.totalweight += 1

    def printName(self):
        return str(self.name) + str('-') + str(self.occurence)

    @classmethod
    def NumberOfSysteme(cls):
        return cls.number


class link:

    def __init__(self, x, y, size):
        self.X = x
        self.Y = y
        self.size = size
        self.description = []

    def PrintLinkDescription(self):
        return self.description

    def __eq__(self, other):
        if (self.Y == other.Y and self.X == other.X) or (self.Y == other.X and self.X == other.Y) or (self.X == other.Y and self.Y == other.X):
            return True
        else:
            return False


planete[0] = systeme(0, 0)
dist = 2
count = 2
j = 2
for i in range(1, len(planete)):
    planete[i] = systeme(dist-1, 0)
    if count == pow(2,dist):
        Univers[j] = count
        dist += 1
        j += 1
    count += 1


for i in range(0, len(saut)):
    testStillTrue = 0
    while testStillTrue == 0:
        x = randint(0, len(planete) - 1)
        y = randint(0, len(planete) - 1)
        while (int(abs(planete[x].distance - planete[y].distance)) > 1) or (x == y):
            y = randint(0, len(planete) - 1)
        for j in range(0, i):
            if (saut[j].X == x and saut[j].Y == y) or (saut[j].Y == x and saut[j].X == y) or (saut[j].X == y and saut[j].Y == x):
                x = randint(0, len(planete) - 1)
                y = randint(0, len(planete) - 1)
                while (int(abs(planete[x].distance - planete[y].distance)) > 1) or (x == y):
                    y = randint(0, len(planete) - 1)
        if (planete[int(x)].linkNumber <= MaxLink - 1) and (planete[int(y)].linkNumber <= MaxLink - 1):
            saut[i] = link(x, y, abs(planete[x].distance - planete[y].distance))
            planete[int(x)].AddLink(i)
            planete[int(y)].AddLink(i)
            planete[int(x)].Addtotalweight()
            planete[int(y)].Addtotalweight()
            testStillTrue = 1

    saut[i].description = (str(planete[int(saut[i].X)].printName()) + str(' - ') + str(planete[int(saut[i].Y)].printName()) + str(' : ') + str(saut[i].size))

for i in range(0, len(planete)):
    print('____')
    print ('planete ' + str(planete[i].printName()) + ': ' + str(planete[i].distance))
    for j in range(0 ,MaxLink):
        index = planete[i].linkTable[j]
        if index is not None:
            print('=> ' + saut[index].description )
        else:
            print ('=> --')
print('____')
count = 0
for i in range(0, len(planete)):
    if planete[i].linkNumber != 3:
        count += 1

print(count)

initx = 1000
inity = 1000
c = [None]*NbPlanet
Nom = [None]*NbPlanet
l = [None]*NbLink
index = 0
i = 0
angle = 0
x = 0
y = 0
view = GraphWin("Galaxy View", initx, inity)
while i <= len(planete):
    while index == planete[i].distance:
        (x,y)= pol2cart((planete[i].distance*50), angle)
        c[i] = Circle(Point(initx/2 + x,inity/2 + y), 10)
        Nom[i] = Text(Point(initx/2 + x,inity/2 + y), i)
        Nom[i].draw(view)
        c[i].draw(view)
        angle += (2*math.pi / Univers[index])
        if i < (len(planete)):
            i += 1
        if i == NbPlanet:
            break
    if i == NbPlanet:
        break
    index += 1
    angle = 0
view.getMouse() # Pause to view result
view.close()    # Close window when done
