from random import randint

class LobbyController():
    """docstring for LobbyController"""
    def __init__(self):
        self.getCredentials()
        #print('Hello {0} here are the contents of the file: \n'.format(person))
        #file = open(filename , 'r')
        #file_contents = file.read()
        #print(file_contents)
        self.file_len()

    def getCredentials(self):
        person = raw_input('Enter your name: ')
        userID = randint(100000000, 999999999)
        file = open(filename, 'a+')
        file.write('user: {0} ID: {1} \n'.format(person,userID))
        file.close()

    def file_len(self):
        count = 0
        with open(filename) as infp:
            for line in infp:
                count = count + 1
        print(count)
        if(count < 4):
            pass
        else:
            print("Game is ready to be played")
        
filename = 'DBfile.dat'
c = LobbyController()
        