import time
from menus import OptionMenu, CreateLobbyMenu, JoinLobbyMenu
from screens import EndGameResultsScreen

class MafiaApp:
    """Abstraction of the MafiaApp client"""
    def __init__(self):
        self.game = None
        self.lobby = None

    def start(self, args):
        self.splashScreen()

        while True:
            selection = self.optionMenu()

            if selection is OptionMenu.CREATE_LOBBY:
                self.lobby = self.createLobbyMenu()
            elif selection is OptionMenu.JOIN_LOBBY:
                self.lobby = self.joinLobbyMenu()

            if self.lobby is None:
                raise Exception("Lobby cannot be null")

            lobbyResults = self.lobby.run() # Run the instance of the lobby on the client.

            self.game = lobbyResults.game # As part of the lobby concluding the game is returned.

            endGameResults = self.game.run() # Game is started and runs to completing and results are collected.
            self.endGameResultsScreen(endGameResults)

    def splashScreen(self):
        # displaySplashScreen()
        time.sleep(3)

    def optionMenu(self):
        # Create the menu
        menu = OptionMenu()
        menu.displayMenu()
        return menu.getSelection()

    def createLobbyMenu(self):
        menu = CreateLobbyMenu()
        menu.displayMenu()
        return menu.createLobby() # Creates the Lobby instance

    def joinLobbyMenu(self):
        menu = JoinLobbyMenu()
        menu.displayMenu()
        return menu.joinLobby() # Returns the Lobby instance the user joined.

    def endGameResultsScreen(self, endGameResults):
        screen = EndGameResultsScreen(endGameResults)
        screen.displayScreen()

app = MafiaApp()
app.start(None)