#import the classes we have written
from GAME import Game
from ROOM import Room

#Create (instantiate) an instance of Game, called game
game = Game()

#Test the game status and that we can flip it
print('Is the game running?')
print(game.getPlayStatus())
print('Flip it around!')
game.flipPlayStatus()
print('Is the game running now?')
print(game.getPlayStatus())

#Create a room (we used room 1 for an example, and it currently does not
# contain anything)
room = Room(1,'Startboard Bows',None,None)
#Look at the room's short description
print(room.getShortDesc())

#Whoops - we made a typo! Change the short description and look again
room.setShortDesc('Starboard Bows')
print(room.getShortDesc())
