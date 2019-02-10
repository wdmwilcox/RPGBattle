from character import Character, Player, Enemy, Gnome
from battle import Battle

class Engine(object):
	
	def __init__(self):
		pass

	def get_help(self):
		print(f'This feature is not implemented.')
		self.play()

	def quit_game(self):
		print(f'This feature is implemented.')
		exit(0)

	def make_player(self):
		print(f'You wake up with amnesia.  What is your name?')
		player_name = input(' > ')
		print(f'''Ah yes, {player_name}.  You feel a bruise on your head and see a simple wooden club at your feet.
A quick check of your pockets reveal that your gold is missing.  You have been robbed!  You aren't going to take this
lying down; you reach down to grab the club and find some monster footprints leading away.  It's time to get your money back!''')
		player = Player(player_name)
		return player			

	def play_battle(self):
		battle = Battle(player_level)
		battle.generate_enemies()
		battle.display_information()
		while battle.battle_over == False:
			battle.display_enemy_dialogue()
			player_choice = battle.get_choices()
			for action in player.actions():
				if player_choice == player.actions[action]:
					player.actions[action].do_action(battle)
				else:
					print("You can't do that right now.")
				
				

	def play(self):
		print('Welcome to RPG Battle!')
		print("Type 'help' to read the rules; type 'start' to begin a new game, or type 'quit' to exit.")
		play_input = input(' > ')
		if play_input.lower() == 'help':
			self.get_help()
		elif play_input.lower() == 'start':
			self.player = self.make_player()
			print(f'Hello, {self.player.name}.  This feature is not implemented.')
		elif play_input.lower() == 'quit':
			self.quit_game()
		else:
			print(f'The feature {help_or_start} is not implemented.')
			self.play()