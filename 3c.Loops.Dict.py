# dict - is a two dimenional list.   Like a word and then it's definition

systems_and_games = {
    "Atari": "Space Invaders",
    "C64": "Lazy Jones",
    "NES": "Mario 3"
}

# print (systems_and_games ["Atari"])

# dict - is a two dimenional list.   Like a word and then it's definition

for systemnum in systems_and_games.keys():
    print ("System:  " , systemnum)

# print both 

for systemnum in systems_and_games.keys():
    print ("System:  " , systemnum, systems_and_games[systemnum])

# 55.12 loops