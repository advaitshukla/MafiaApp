from lobby import Lobby

class BaseMenu:
    def displayMenu(self):
        print "Displaying Menu: " + self.name


class OptionMenu(BaseMenu):
    CREATE_LOBBY = "CREATE_LOBBY"
    JOIN_LOBBY = "JOIN_LOBBY"

    def __init__(self):
        self.name = "OptionMenu"

    def getSelection(self):
        return self.CREATE_LOBBY # for now.

class CreateLobbyMenu(BaseMenu):
    def __init__(self):
        self.name = "CreateLobbyMenu"

    def createLobby(self):
        return Lobby()

class JoinLobbyMenu(BaseMenu):
    def __init__(self):
        self.name = "JoinLobbyMenu"

    def joinLobby(self):
        # For now just create one.
        return Lobby()