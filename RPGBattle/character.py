from time import sleep
from random import randrange

class Character(object):

	def __init__(self):
		self.stats = {'health' : 100.0,
		'attack power' : 1.0,
		'defense' : 1.0,
		}
		self.actions = {}
		self.level = 1

	def take_damage(damage):
		self.stats["health"] -= damage
		if self.stats["health"] <= 0:
			self.die()
	
	def die():
		pass

class Player(Character):

	def __init__(self, name):
		super().__init__()
		self.name = name
		self.actions = {'attack': self.attack,
					'flee': self.flee,
					'taunt': self.taunt,
					'apocalypse': self.apocalypse,
					}

	def get_choice(self):
		print('What shall you do?  ')
		for action in self.actions.keys():
			print(action)
		choice = input(' > ')
		return choice

	def flee(self, battle):
		print(f"{self} fleed.")
		pass

	def taunt(self, battle):
		print(f"{self} taunted.")
		pass

	def attack(self, battle):
		print(f"{self} attacked.")
		print("Who do you want to attack?")
		for i in range(0,len(battle.enemies)):
			print(f"{i + 1}: {battle.enemies[i]}")
		try:
			enemy_choice = int(input(" > "))
			damage = self.stats['attack power']
			battle.enemies[enemy_choice - 1].stats['health'] -= damage
			print(f"Attacked {battle.enemies[enemy_choice - 1]} for {damage}.")
			print(battle.enemies[enemy_choice - 1].stats['health'])
		except:
			print("Please enter a number.")
			attack(battle)

	def apocalypse(self, battle):
		print("You just ended the world.")
		sleep(1)
		print("Well, that was pointless.")
		sleep(1)
		print("Enjoy your solitary existence in the void, I guess...")
		sleep(2)
		exit(0)


class Enemy(Character):

	def __init__(self):
		super().__init__()
		self.dialogue = {'meet' : [],
						 'hit' : [],
						 'miss' : [],
						 'defeat' : [],
						 'victory' : [],
						}

	def play_turn(self, battle, player):
		# choose action, report results
		pass

	def speak(self):
		pass


class Gnome(Enemy):  # This class does not condone racism towards gnomes

	def __init__(self, level):
		super().__init__()
		#TODO hardcoded health for testing. Change later
		self.stats['health'] = 3
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

	def play_turn(self, battle, player):
		# choose action, report results
		random_number = randrange(0,100)
		if random_number < 50:
			self.attack()
		else:
			self.flee()
		pass

	def attack(self):
		print(f"{self} attacked.")
		pass

	def flee(self):
		print(f"{self} fleed.")
		pass

	def speak(self):
		print(f"{self} spoke.")
		pass
	
	def die(self):
		print(f"{self} died.")

