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
        spaces[1].connections = spaces[0],spaces[16]
        spaces[2].connections = spaces[3],spaces[16]
        spaces[3].connections = spaces[2],spaces[4]
        spaces[4].connections = spaces[3]
        spaces[5].connections = spaces[6],spaces[7]
        spaces[6].connections = spaces[5]
        spaces[7].connections = spaces[5],spaces[8]
        spaces[8].connections = spaces[7],spaces[9], spaces[11]
        spaces[9].connections = spaces[8],spaces[10]
        spaces[10].connections = spaces[9], spaces[11]
        spaces[11].connections = spaces[8], spaces[10], spaces[12]
        spaces[12].connections = spaces[11], spaces[13]
        spaces[13].connections = spaces[14],spaces[12]
        spaces[14].connections = spaces[11],spaces[13],spaces[15],
        spaces[15].connections = spaces[14], spaces[16]
        spaces[16].connections = spaces[15],spaces[1]
    
    def placeItems(self):
        availableSpaces = list(range(1,16))
        
        random.shuffle(availableSpaces)

        wumpusIndex = availableSpaces.pop()
        pit1Index = availableSpaces.pop()
        pit2Index = availableSpaces.pop()
        batIndex = availableSpaces.pop()

        self.spaces[wumpusIndex].wumpus = True
        self.spaces[pit1Index].pit = True
        self.spaces[pit2Index].pit = True
        self.spaces[batIndex].bats = True
            
            
    def getSpace(self, spaceId):
        return self.spaces[spaceId]
        
        
class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player(self.board.getSpace(0))
        self.wumpusSpace = self.wumpusSpace()
        
    def wumpusSpace(self):
        #returns the value of the space that has the wumpus
        for space in self.board.spaces:
            if space.wumpus:
                return space
        return None
        
        
    def checkSpace(self):
        space = self.player.currentSpace
        if space.wumpus ==True:
            self.player.alive = False
            return "You have been eaten by the Wumpus!"
        elif space.pit == True:
            self.player.alive = False
            return "You fell into a pit!"
        elif space.bats:
            self.player.currentSpace = random.choice(self.board.spaces)
        
    def movePlayer(self, spaceId):
        targetSpace = self.board.getSpace(spaceId)
        self.player.move(targetSpace)
        return self.checkSpace()

    def shootArrow(self, spaceId):
        if not self.player.shoot():
            return "No arrows left!"

        if self.board.getSpace(spaceId).wumpus:
            return "You killed the Wumpus! You win!"
        else:
            return "Missed. The Wumpus might wake up..."
        
        
if __name__ == "__main__":
    game = Game()

    print("Welcome to Hunt the Wumpus!")
    print("You have 3 arrows. Try to kill the Wumpus!")

    while game.player.alive:
        current = game.player.currentSpace
        connected_ids = [space.id for space in current.connections]

        print(f"\nYou are in room {current.id}.")
        print(f"Tunnels lead to: {connected_ids}")
        print(f"Arrows left: {game.player.arrows}")

        action = input("Move or Shoot? (m/s): ").strip().lower()

        if action not in ['m', 's']:
            print("Invalid action. Please choose 'm' to move or 's' to shoot.")
            continue

        try:
            target = int(input(f"Enter the room number to {'move to' if action == 'm' else 'shoot into'}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if target not in [space.id for space in current.connections]:
            print("That room is not connected to your current room.")
            continue

        if action == 'm':
            result = game.movePlayer(target)
            if result:
                print(result)
        else:
            result = game.shootArrow(target)
            print(result)
            if "win" in result.lower():
                break

    if not game.player.alive:
        print("Game Over.")
