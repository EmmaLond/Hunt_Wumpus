#Wumpus Game
import random

class Player:
    def __init__(self, startingSpace):
        self.currentSpace = startingSpace
        self.arrows = 3
        self.alive = True
        
    def move(self, space):
        #if the space chosen is within the connections
        if space in self.currentSpace.connections:
            #set the current space to space
            self.currentSpace = space
        else:
            raise ValueError("Invalid move")
            
        
    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            return True
        else:
            return False
        
        
class Space:
    def __init__(self, spaceID):
        self.id = spaceID
        self.connections = []
        self.wumpus = False
        self.pit = False
        self.bats = False
        
    def connect(self, otherSpace):
        if otherSpace not in self.connections:
            self.connections.append(otherSpace)
            otherSpace.connections.append(self) 

    
    
class Board:
    def __init__(self):
        self.spaces = [Space(i) for i in range (17)]
        self.connectSpace()
        self.placeItems()
        
    def connectSpace(self):
        #for loop that creates the amount of spaces
        spaces = self.spaces
        #list the space connections
        spaces[0].connections = spaces[1],spaces[2]
        space[1].connections = space[0],space[16]
        space[2].connections = space[3],space[16]
        space[3].connections = space[2],space[4]
        space[4].connections = space[3]
        space[5].connections = space[6],space[7]
        space[6].connections = space[5]
        space[7].connections = space[5],space[8]
        space[8].connections = space[7],space[9], space[11]
        space[9].connections = space[8],space[10]
        space[10].connections = space[9], space[11]
        space[11].connections = space[8], space[10], space[12]
        space[12].connections = space[11], space[13]
        space[13].connections = space[14],space[12]
        space[14].connections = space[11],space[13],space[15],
        space[15].connections = space[14], space[16]
        space[16].connections = space[15],space[1]
    
    def placeItems(self):
        availableSpaces = list(range(1,16))
        
        random.shuffle(available_indices)

        wumpusIndex = availableSpaces.pop()
        pit1Index = availableSpaces.pop()
        pit2Index = availableSpaces.pop()
        batIndex = availableSpaces.pop()

        self.spaces[wumpusIndex].hasWumpus = True
        self.spaces[pit1Index].hasPit = True
        self.spaces[pit2Index].hasPit = True
        self.spaces[batIndex].hasBats = True
            
            
    def getSpace(self, spaceId):
        return self.spaces[spaceId]
        
        
class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player(self.board.getSpace(0))
        self.wumpusspace = self.wumpusSpace()
        
    def wumpusSpace(self):
        #returns the value of the space that has the wumpus
        for space in self.board.spaces:
            if space.hasWumpus:
                return space
        return None
        
        
    def checkSpace(self):
        space = self.player.currentSpace
        if space.hasWumpus ==True:
            self.player.alive = False
            return "You have been eaten by the Wumpus!"
        elif space.hasPit == True:
            self.player.alive = False
            return "You fell into a pit!"
        elif space.hasBats:
            self.player.currentSpace = random.choice(self.board.spaces)
        
    def movePlayer(self, spaceId):
        targetSpace = self.board.getSpace(spaceId)
        self.player.move(targetSpace)
        return self.checkSpace()

    def shoot_arrow(self, spaceId):
        if not self.player.shoot():
            return "No arrows left!"

        if self.cave.getSpace(spaceId).has_wumpus:
            return "You killed the Wumpus! You win!"
        else:
            return "Missed. The Wumpus might wake up..."