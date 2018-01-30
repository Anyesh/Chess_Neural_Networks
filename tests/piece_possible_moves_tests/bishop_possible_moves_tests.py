import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if bishop legal moves are blocked as intended
class BishopPossibleMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhiteBishopFromA1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteBishopFromD5():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteBishopFromD4FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,C3))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteBishopFromD4EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,C3))
        comparisonMoves = [E5, E3, C5, C3]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackBishopFromH1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackBishopFromE4():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackBishopFromDE6FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,D5))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackBishopFromDE6EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,D5))
        comparisonMoves = [F7, F5, D7, D5]
        self.assertEqual(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    