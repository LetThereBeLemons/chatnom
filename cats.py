# Chatnom - A LetThereBeLemons creation
# Liscenced under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)
version = "c2v1-r1"
from random import choice as rc

cats = [
	"""
|\---/|
| o_o |
 \_^_/
	""",
	"""
 /\_/\\
( o.o )
 > ^ <

	""",
	"""
    |\__/,|   (`\\
  _.|o o  |_   ) )
-(((---(((--------
	""",
	"""
      |\      _,,,---,,_
     /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
	"""
]

def getCat():
	return rc(cats)