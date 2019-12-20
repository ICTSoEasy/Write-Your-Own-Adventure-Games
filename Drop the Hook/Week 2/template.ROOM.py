#An initial definition of a room
class Room:
    #Initiiaslisation happens when you take this description and make it into
    #an object.
    # - self - all class definitions need this so that it can look at it's own properties & methods
    # - id - we will give it a number to identify itt by
    # - shortDesc will be the 'name' of the room
    # - exits will be a list of exits from the room
    # - contains will be a list of the things contained in the room
    # - longDesc will be the longer description which we will only see if we actually look around.
    #   as this is not strictly neccesary, we start it as nothing and then set it later if we 
    #   so wish.
    def __init__(self, id, shortDesc, exits, contains):
        self.id = id
        self.shortDesc = shortDesc
        self.exits = exits
        self.contains = contains
        self.longDesc = ''

    #This will look at itself and give us back the short description
    def getShortDesc(self):
        pass

    #This will take the new description we give it and set this as the object's short description
    def setShortDesc(self,desc):
        self.shortDesc = desc

    #This will look at itself and give us back the long description
    def getLongDesc(self):
        pass

    #This will take the new description we give it and set this as the object's long description
    def setLongDesc(self,desc):
        self.longDesc = desc

    #This give us a list of exits
    def getExits(self):
        pass

    #This allows us to test if exit exists in our list of known exits
    def checkExitExists(self,exit):
        pass

    #This allows us to add a new exit direction which points to the ID of whatever room we wish
    def addExit(self,exitDirection,exitID):
        pass

    #This allows us to remove an exit
    def removeExit(self,exitDirection):
        pass

    #This will give us a list of things the room contains
    def getContains(self):
        pass

    #This will let us test if a particular item is in the room
    def ifContains(self,contains):
        pass

    #This lets us rmove an item from the room
    def remove(self,item):
        pass

    #This lets us put an item in to the room
    def putIn(self,item):
        pass