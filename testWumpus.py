#Unit Test File
import unittest
from game import Game, Player, Space, Board

class TestWumpus(unittest.TestCase):
    
    def testPlayerMovement(self):
        a = Space(1)
        b = Space(2)
        a.connect(b)
        player = Player(a)
        player.move(b)
        self.assertEqual(player.current_space, b)
        
    #def testInvalidMoves(self):
        
    #def testShootArrow(self):
        
    #def testZeroArrows(self):
        
    #def testCheckWumpusSpace(self):
        
    #def checkRandomizedBats(self):
        

if __name__ == '__main__':
    unittest.main()