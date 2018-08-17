from random import randint

Names = ['Abydos','Camelot','Delmak','Gaia','Edasich','Hadante','Tauri','Hadar','Icalurus','Juna','Kheb','Langara','Palilicium']
Occurence_name = [0]*len(Names)
planete = [None]*50
saut = [None]*50
i = 0
j = 0
testStillTrue = 0
MaxLink = 3

class systeme:
    number = 0
    def __init__(self):
        self.number += 1
        self.rand = randint(0, len(Names)-1)
        self.name = Names[self.rand]
        self.occurence = Occurence_name[self.rand]
        self.linkNumber = 0
        self.linkTable = [None]*MaxLink
        Occurence_name[self.rand] += 1

    def AddLink(self,i):
        if self.linkNumber <= MaxLink:
            self.linkTable[self.linkNumber] = i
            self.linkNumber += 1
            return self.linkNumber
        else:
            return -1

    def printName(self):
        return str(self.name) + str('-') + str(self.occurence)
    @classmethod
    def NumberOfSysteme(cls):
        return cls.number

class link:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.description = []
    def PrintLinkDescription(self):
        return self.description
    def __eq__(self, other):
        if (self.Y == other.Y and self.X == other.X) or (self.Y == other.X and self.X == other.Y) or (self.X == other.Y and self.Y == other.X):
            return True
        else:
            return False
print ("-----")
for i in range (0,len(planete)):
    planete[i] = systeme()
i = 0
j = 0
print ("-----")
for i in range (0,len(saut)):
    testStillTrue = 0
    while testStillTrue == 0:
        testStillTrue = 1
        x = randint(0, len(planete) - 1)
        y = randint(0, len(planete) - 1)
        while x == y:
            y = randint(0, len(planete) - 1)
        saut[i] = link(x, y)
        for j in range(0,i):
            if saut[j] == saut[i]:
                x = randint(0, len(planete) - 1)
                y = randint(0, len(planete) - 1)
                while x == y:
                    y = randint(0, len(planete) - 1)
                saut[i] = link(x,y)
                testStillTrue = 0
        if (planete[int(saut[i].X)].linkNumber <= MaxLink -1) and (planete[int(saut[i].Y)].linkNumber <= MaxLink -1):
            planete[int(saut[i].X)].AddLink(i)
            planete[int(saut[i].Y)].AddLink(i)
        else:
            testStillTrue = 0
    saut[i].description = (str(planete[int(saut[i].X)].printName()) + str(' - ') + str(planete[int(saut[i].Y)].printName()))

    #print(saut[i].description)

i = 0
j = 0
for i in range (0,len(planete)):
    print('____')
    print ('planete ' + str(planete[i].printName()) + ':')
    for j in range(0,MaxLink):
        index = planete[i].linkTable[j]
        if (index != None):
            print('=> ' + saut[index].description)
        else:
            print ('=> --')
print('____')
print ('fini')
