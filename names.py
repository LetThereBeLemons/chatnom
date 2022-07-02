# Chatnom - A LetThereBeLemons creation
# Liscenced under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)
version = "c1v1-r1"
from random import choice as rc

names_first = [
	"Little",
	"Glittery",
	"Cute",
	"Shiny",
	"Fuzzy",
	"Furry",
	"Fluffy",
	"Soft",
	"Cuddly"
]

names_last = [
	"Lemons",
	"Moggy",
	"Kitty",
	"Pussy",
	"Lolly",
	"Bunny",
	"Cotton"
]

def getName():
	return rc(names_first) + " " + rc(names_last)