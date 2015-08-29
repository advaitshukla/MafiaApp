class Lobby:
    def run(self):
        print "Running the lobby..."
        lobbyResults = LobbyResults()
        lobbyResults.game = Game()
        return lobbyResults

class LobbyResults:
    pass

class Game:
    def run(self):
        return EndGameResults()

class EndGameResults:
    pass