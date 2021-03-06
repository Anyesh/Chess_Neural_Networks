from tests.test_utils.test_utility import *


# This class tests if king legal moves are blocked as intended
class KingBoardOperationsTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        # These 3 methods will wipe the slate clean so we can begin anew
        self.board.setupEmptyBoard()
        self.gameLogic.whitePlayer.clearPlayerData()
        self.gameLogic.blackPlayer.clearPlayerData()

    # ///////////
    # // WHITE //
    # ///////////

    def testGetWhiteKingOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.isPieceExists(Values.king, D4)

    def testPutWhiteKingOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.king, D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testGetBlackKingOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.isPieceExists(-Values.king, D4)

    def testPutBlackKingOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.king, D4)
