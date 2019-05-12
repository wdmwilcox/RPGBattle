from character import Gnome
from time import sleep
class Battle(object):

	def __init__(self, player_level):
		self.player_level = player_level
		self.battle_over = False
		self.enemies = [Gnome(1)]
		self.loot = {}

	def generate_enemies(self):
		pass

	def display_information(self):
		pass

	def display_enemy_dialogue(self):
		pass

	def add_loot(self,loot):
		pass

	def calculate_outcome(self):
		return "this is the outcome"
		pass

	def get_enemy_turn(self, player):
		for enemy in self.enemies:
			enemy.play_turn(self, player)
			sleep(1)

	def check_battle_over(self):
		for enemy in self.enemies:
			if enemy.stats['health'] > 0:
				return False
		return True
