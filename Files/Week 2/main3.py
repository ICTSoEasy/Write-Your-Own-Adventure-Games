#import the classes we have written
from GAME import Game
from ROOM import Room

#Create (instantiate) an instance of Game, called game
game = Game()

print('Adding rooms')
game.addRoom(Room(1,'Starboard Bows',None,None))
game.addRoom(Room(2,'Port Bows',None,None))
game.addRoom(Room(3,'Starboard Forebeam',None,None))
game.addRoom(Room(4,'Starboard Foredeck',None,None))
game.addRoom(Room(5,'Port Foredeck',None,None))
game.addRoom(Room(6,'Port Forebeam',None,None))
game.addRoom(Room(7,'Starboard Beam',None,None))
game.addRoom(Room(8,'Starboard Midships',None,None))
game.addRoom(Room(9,'Port Midships',None,None))
game.addRoom(Room(10,'Port Beam',None,None))
game.addRoom(Room(11,'Starboard Quarter',None,None))
game.addRoom(Room(12,'Starboard Aft Deck',None,None))
game.addRoom(Room(13,'Port Aft Deck',None,None))
game.addRoom(Room(14,'Port Quarter',None,None))
game.addRoom(Room(15,'Poop Deck',None,None))
game.addRoom(Room(16,'Starboard Forecastle',None,None))
game.addRoom(Room(17,'Port Forecastle',None,None))
game.addRoom(Room(18,'Starboard Fore Hold',None,None))
game.addRoom(Room(19,'Port Fore Hold',None,None))
game.addRoom(Room(20,'Starboard Aft Hold',None,None))
game.addRoom(Room(21,'Port Aft Hold',None,None))
game.addRoom(Room(22,'Captain\'s Cabin',None,None))
game.addRoom(Room(23,'Rudder',None,None))

game.listRooms()
