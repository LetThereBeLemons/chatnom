# Chatnom - A LetThereBeLemons creation
# Liscenced under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)
version = "c0v3-r1"

from names import getName
from cats import getCat
from time import sleep as ts
import colours

while True:
	try:
		print(colours.bold + getCat() + "\n" + colours.cyan + colours.bold + getName() + colours.reset)
		input()
	except KeyboardInterrupt or EOFError:
		print("\nGoodbye!")
		ts(0.5)
		exit()