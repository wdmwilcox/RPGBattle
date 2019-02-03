# namespace
import random
import time

# globals

# classes

class Character(object):
	
	def __init__(self):
		self.stats = {'health' : 100.0,
		'attack power' : 1.0,
		'defense' : 1.0,
		}
		
		
class Player(Character):
	
	def __init__(self, name):
		self.name = name
		

class Enemy(Character):

	def __init__(self):
		self.dialogue = {'meet' : [],
						 'hit' : [],
						 'miss' : [],
						 'defeat' : [],
						 'victory' : [],
						}


class Gnome(Enemy):  # This class does not condone racism towards gnomes

	def __init__(self, level):
		self.name = 'Gnome'
		self.dialogue = {'hit' : ['Ouch',
							      'Darnit',
								  'Argh',
								  ],
						 'meet' : ['I\'m a guh-nome!',
								   'You\'re \'bout to get gnomed!',
								   'Watch your knees!',
								   'Fresh out the garden!',
								   ],
						 }
								   

class Engine(object):
	
	def __init__(self):
		pass

	def get_help(self):
		print(f'This feature is not implemented.')
		self.play()

	def quit_game(self):
		print(f'This feature is implemented.')
		exit(0)

	def get_player_name(self):
		print(f'You wake up with amnesia.  What is your name?')
		player_name = input(' > ')
		print(f'''Ah yes, {player_name}.  You feel a bruise on your head and see a simple wooden club at your feet.
A quick check of your pockets reveal that your gold is missing.  You have been robbed!  You aren't going to take this
lying down; you reach down to grab the club and find some monster footprints leading away.  It's time to get your money back!''')
		return player_name

	def new_battle(self):
		
		monster = Enemy(player_level)
	


	def play(self):
		print('Welcome to RPG Battle!')
		print("Type 'help' to read the rules; type 'start' to begin a new game, or type 'quit' to exit.")
		play_input = input(' > ')
		if play_input.lower() == 'help':
			self.get_help()
		elif play_input.lower() == 'start':
			self.player_name = self.get_player_name()
			print(f'Hello, {self.player_name}.  This feature is not implemented.')
		elif play_input.lower() == 'quit':
			self.quit_game()
		else:
			print(f'The feature {help_or_start} is not implemented.')
			self.play()


def main():
	game = Engine()
	game.play()
	
main()

