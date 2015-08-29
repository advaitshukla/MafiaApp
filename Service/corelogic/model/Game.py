class Game:
    """Model object storing important game information"""
    def __init__(self, id, numPlayers):
        self.id = id
        self.numPlayers = numPlayers
        self.gameOver = False
        self.rounds = []
