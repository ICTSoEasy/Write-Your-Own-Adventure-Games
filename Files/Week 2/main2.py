#import the classes we have written
from GAME import Game
from ROOM import Room

#Create (instantiate) an instance of Game, called game
game = Game()

#Create a room (we used room 1 for an example, and it currently does not
# contain anything)
room = Room(1,'Starboard Bows',None,None)

#Add the room to the game
print('Adding room 1')
game.addRoom(room)
game.listRooms()

#We can actually combine this into a single line:
print()
print('Adding room 2')
game.addRoom(Room(2,'Port Bows',None,None))
game.listRooms()
