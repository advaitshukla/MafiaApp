class BaseScreen:
    def displayScreen(self):
        print "Displaying Screen: " + self.name

class EndGameResultsScreen(BaseScreen):
    def __init__(self, endGameResults):
        self.name = "EndGameResultsScreen"