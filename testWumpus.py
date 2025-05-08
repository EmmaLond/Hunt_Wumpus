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
        
    def testShootArrow(self):
        player = Player(Space(0))
        self.assertTrue(player.shoot())
        self.assertTrue(player.shoot())
        self.assertTrue(player.shoot())
        self.assertFalse(player.shoot())
        self.assertEqual(player.arrows, 0)
        
    def testBoardInitialization(self):
        board = Board()
        self.assertEqual(len(board.spaces), 17)
        self.assertTrue(any(s.wumpus for s in board.spaces))
        self.assertEqual(sum(1 for s in board.spaces if s.pit), 2)
        self.assertEqual(sum(1 for s in board.spaces if s.bats), 1)
    
    def test_shoot_arrow_hits_wumpus(self):
        game = Game()
        wumpusSpace = Space(3)
        wumpusSpace.wumpus = True
        game.board.spaces = [Space(i) for i in range(5)]
        game.board.spaces[3] = wumpusSpace
        result = game.shootArrow(3)
        self.assertIn("win", result.lower())
        
    def test_shoot_arrow_misses(self):
        game = Game()
        for s in game.board.spaces:
            s.wumpus = False
        result = game.shootArrow(1)
        self.assertIn("missed", result.lower())
        
        

if __name__ == '__main__':
    unittest.main()