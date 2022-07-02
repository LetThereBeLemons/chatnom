# Chatnom - A LetThereBeLemons creation
# Liscenced under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)
version = "c1v2-r1"
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
	"Cuddly",
	"Squishy",
	"Squidgy",
	"Lovely",
	"Pretty",
	"Buttery",
	"Evil"
]

names_last = [
	"Lemon",
	"Moggy",
	"Kitty",
	"Lolly",
	"Bunny",
	"Cotton",
	"Buttercup",
	"Pickles",
	"Mimi",
	"Coco",
	"Macaroni",
	"Rose",
	"Shadow",
	"Pepper",
	"Nutmeg",
	"Peanut"
]

def getName():
	return rc(names_first) + " " + rc(names_last)