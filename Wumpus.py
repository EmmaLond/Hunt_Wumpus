#Wumpus Game
import random

class Player:
    def__init__(self, startingSpace):
        self.currentSpace = startingSpace
        self.arrows = 3
        self.alive = True
        
    def move(self, space):
        #if the space chosen is within the connections
        if room in self.current_space.connections:
            #set the current space to space
            self.current_space = space
        else:
            raise ValueError("Invalid move")
            
        
    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            return True
        else:
            return False
        
        
class Space:
    def__init__(self, spaceID):
        self.id = spaceID
        self.connections = []
        self.wumpus = False
        self.pit = False
        self.bats = False
        
    def connect(self, other_space):
        if other_space not in self.connections:
            self.connections.append(other_space)
            other_space.connections.append(self) 

    
    
class Board:
    def__init__(self):
        spaces = [Space[i] for i in range (15)]
        self.connectSpace()
        self.placeItems()
        
    def connectSpace(self):
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
    
    def placeItems(self):
        availableSpaces = list(range(1,16))
        
        random.shuffle(available_indices)

        wumpusIndex = availableSpaces.pop()
        pit1Index = availableSpaces.pop()
        pit2Index = availableSpaces.pop()
        batIndex = availableSpaces.pop()

        self.spaces[wumpus_index].hasWumpus = True
        self.spaces[pit1Index].hasPit = True
        self.spaces[pit2Index].hasPit = True
        self.spaces[batIndex].hasBats = True
            
            
    def getSpace(self, spaceId):
        return self.spaces[spaceId]
        
        
class Game:
    def__init__(self):
        
    def wumpusSpace(self):
        #returns the value of the space that has the wumpus
        
        
    def checkSpace(self):
        space = self.player.currentSpace
        if space.has wumpus = True:
            self.player.alive = False
            return "You have been eaten by the Wumpus!"
        elif space.hasPit = True:
            self.player.alive = False
            return "You fell into a pit!"
        elif space.hasBats:
            self.player.currentSpace = random.choice(self.board.spaces)
        
    def movePlayer(self, spaceID):
        #
        
        
