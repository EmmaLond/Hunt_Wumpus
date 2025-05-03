#Unit Test File
import unittest
from Wumpus import Game, Player, Space, Board

class TestWumpus(unittest.TestCase):
    
    def testPlayerMovement(self):
        a = Space(1)
        b = Space(2)
        a.connect(b)
        player = Player(a)
        player.move(b)
        self.assertEqual(player.currentSpace, b)
        
    def testInvalidMoves(self):
        a = Space(1)
        b = Space(2)
        player = Player(a)
        with self.assertRaises(ValueError):
            player.move(b)
        
    #def testShootArrow(self):
        
    #def testZeroArrows(self):
        
    #def testCheckWumpusSpace(self):
        
    #def checkRandomizedBats(self):
        

if __name__ == '__main__':
    unittest.main()