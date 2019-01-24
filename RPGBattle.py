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

	def __init__(self, name):
		self.name = name
		pass


class Engine(object):
	
	def __init__(self):
		pass

	def new_battle(self):
		pass

	def get_help(self):
		print(f'This feature is not implemented.')
		self.play()

	def quit_game(self):
		print(f'This feature is implemented.')
		exit(0)

	def play(self):
		print('Welcome to RPG Battle!')
		print("Type 'help' to read the rules; type 'start' to begin a new game, or type 'quit' to exit.")
		play_input = input(' > ')
		if play_input.lower() == 'help':
			self.get_help()
		elif play_input.lower() == 'start':
			print(f'This feature is not implemented.')
			self.play()
		elif play_input.lower() == 'quit':
			self.quit_game()
		else:
			print(f'The feature {help_or_start} is not implemented.')
			self.play()


def main():
	game = Engine()
	game.play()
	
main()

