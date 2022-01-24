#An initial definition of the game
class Game:
    #Initiaslisation happens when you take this description and make it into
    #an object.
    # - self - all class definitions need this so that it can look at it's own properties & methods
    # - rooms will be the dictionary of rooms - these will start as empty
    # - items will be the dictionary of items not held in a room - these will start as empty
    def __init__(self):
        self.rooms = {} #empty list
        self.items = {} #empty list
        self.status = False #not in play

    #This will tell us whether we are in play or not
    def getPlayStatus(self):
        return self.status

    #This will invert the play status (if we are playing, make us not playing and vice versa)
    def flipPlayStatus(self):
        self.status = not self.status

    #This will add an object to the items dictionary
    def addItem(self,item):
        pass

    #This will move an item to a room from the holding list
    def moveItemToRoom(self,itemId,roomId):
        pass

    #This will move an item from a room to the holding list
    def moveItemToRoom(self,itemId,roomId):
        pass

    #This will add a room to the rooms list
    #It stores it under it's own ID for ease of access
    def addRoom(self,room):
        self.rooms[room.getId()] = room

    #This will list all rooms currently 'owned' by the game
    # not useful for the player, but good for our debugging.
    def listRooms(self):
        print('Listing rooms')
        print('=============')
        for id in self.rooms:
            print(id, '->', self.rooms[id].getShortDesc())

    #This will add a long description to a given room
    def addRoomLongDescription(self,room,desc):
        self.rooms[room].setLongDesc(desc)
