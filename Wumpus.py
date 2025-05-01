#Wumpus Game
class Player:
    def__init__(self, startingSpace):
        self.currentSpace = startingSpace
        self.arrows = 3
        self.alive = True
        
class Space:
    def__init__(self, spaceID, connections)
    self.id = spaceID
    self.connections = connections or []
    self.wumpus = False
    self.pit = False
    self.bats = False
    
class Game:
    def__init__(self):
    
    def createBoard(self):
        #for loop that creates the amount of spaces
        spaces = [Space[i] for i in range (15)]
        #list the space connections
        room[0].connections = room[1],room[2]
        room[1].connections = room[0],room[16]
        room[2].connections = room[3],room[16]
        room[3].connections = room[2],room[4]
        room[4].connections = room[3]
        room[5].connections = room[6],room[7]
        room[6].connections = room[5]
        room[7].connections = room[5],room[8]
        room[8].connections = room[7],room[9], room[11]
        room[9].connections = room[8],room[10]
        room[10].connections = room[9], room[11]
        room[11].connections = room[8], room[10], room[12]
        room[12].connections = room[11], room[13]
        room[13].connections = room[14],room[12]
        room[14].connections = room[11],room[13],room[15],
        room[15].connections = room[14], room[16]
        room[16].connections = room[15],room[1]
        
    def movePlayer(self, newSpaceId):
        
    def shootArrow(self, newSpaceId):
        
        
        