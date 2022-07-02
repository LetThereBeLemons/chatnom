# Chatnom - A LetThereBeLemons creation
# Liscenced under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)
version = "c4v4-r1"

from random import choice as rc

reset = "\x1b[0m"
bold = "\x1b[1m"

red = "\x1b[31m"
cyan = "\x1b[36m"
green = "\x1b[32m"
yellow = "\x1b[33m"
blue = "\x1b[34m"
magenta = "\x1b[35m"

bg_red = "\x1b[41m"
bg_cyan = "\x1b[46m"
bg_green = "\x1b[42m"
bg_yellow = "\x1b[43m"
bg_blue = "\x1b[44m"
bg_magenta = "\x1b[45m"

def getColour(tp):
	if tp == "fg":
		return rc([
			red,
			cyan,
			green,
			yellow,
			blue,
			magenta
		])
	elif tp == "bg":
		return rc([
			bg_red,
			bg_cyan,
			bg_green,
			bg_yellow,
			bg_blue,
			bg_magenta
		])
	else:
		raise ValueError