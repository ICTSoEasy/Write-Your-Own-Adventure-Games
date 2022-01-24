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

print('Adding long descriptions')
game.addRoomLongDescription(1,"This is the starboard bow of the good ship Nautilus. You can see the bowsprit point forwards and the rest of the ship is to the rear, on account of this being the front. There is a lot of sea about, isn't there?")
game.addRoomLongDescription(2,"This is the port bow of the good ship Nautilus. You can see the bowsprit point forwards and the rest of the ship is to the rear, on account of this being the front. The starboard bow is just over there. There is a lot of sea about, isn't there?")
game.addRoomLongDescription(3,"The starboard forebeam is the little bit of deck just forward of the starboard beam and just abeam of the starboard foredeck. It's main reason to exist is because ships don't really divide into nice even shapes.")
game.addRoomLongDescription(4,"The starboard foredeck is just ahead of the foremast and as far forward as you can get without looking like Leonardo Di Caprio")
game.addRoomLongDescription(5,"The port foredeck is just ahead of the foremast. If you go any further forward you might find yourself doing impressions of Claire Danes")
game.addRoomLongDescription(6,"The port forebeam is the little bit of deck just like the starboard forebeam, only the other way around.")
game.addRoomLongDescription(7,"The starboard beam is half way down the starboard side of the ship, overlooking the deep, deep sea.")
game.addRoomLongDescription(8,"The starboard midships is the starboard side of the middle of the ship, smack between the main mast and the foremast. Just ripe for anything falling from the masts to land on your noggin.")
game.addRoomLongDescription(9,"The port midships is the port side of the middle of the ship. The foremast and mainast stretch way, way, way above you.")
game.addRoomLongDescription(10,"The port beam is half way down the port side of the ship, overlooking the deep, deep sea. In fact, when the ship rolls just so, it's overhanging... the... sea. Gulp!")
game.addRoomLongDescription(11,"The starboard quarter is the almost all the way to the back, and on the starboard side, of the Nautilus. Any further aft and you'd be on the poop deck.")
game.addRoomLongDescription(12,"The starboard aft deck is just behind the main mast, towards the middle of the ship. There's quite a lot of deck cargo around - must be quite hard to move on this ship.")
game.addRoomLongDescription(13,"The port aft deck is just behind the main mast, towards the middle of the ship, just opposite the starboard aft deck. There's quite a lot of deck cargo around - must be quite hard to move on this ship.")
game.addRoomLongDescription(14,"The port quarter is the almost all the way to the back, and on the port side, of the Nautilus. You can't half feel the roll of the ship from here!")
game.addRoomLongDescription(15,"The poop deck (hahaha!) is the rearmost part of the ship, where the steering wheel is located. Posh people only up there!")
game.addRoomLongDescription(16,"The forecastle is where the ropes - and rats - hang out. It's small, cramped, and quite smelly!")
game.addRoomLongDescription(17,"The forecastle is where the ropes - and rats - hang out. It's small, cramped, and quite smelly!")
game.addRoomLongDescription(18,"The forehold is where quite a lot of the cargo is kept, and split into two halves. This side looks like mainly wool - not the kind of loot you'd expect from a good pirate!")
game.addRoomLongDescription(19,"The forehold is where quite a lot of the cargo is kept, and split into two halves. This side looks like mainly barrels of rum - which explains why the ship keeps sailing in circles...")
game.addRoomLongDescription(20,"The aft hold is slightly longer than the forehold. This part seems to be mainly spare parts - old sails, sticks (or are they masts) and that kind of thing. It's quite cramped!")
game.addRoomLongDescription(21,"The aft hold is slightly longer than the forehold. This part seems to be mainly paintings of the Captain's wife. How very odd!")
game.addRoomLongDescription(22,"The captain's cabin stretches the whole width of the ship and is filled with a nice dining table, a cot, and some books. As it's a pirate ship the books are mainly of the type that involve cats sitting in hats.")
game.addRoomLongDescription(23,"This is the rudder, the bit that turns the ship left and right. Mainly left - probably because of the amount of rum consumed. It's... quite slippy...")
game.listRooms()
