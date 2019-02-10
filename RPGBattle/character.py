import time

class Character(object):
	
	def __init__(self):
		self.stats = {'health' : 100.0,
		'attack power' : 1.0,
		'defense' : 1.0,
		}
		self.actions = {}
	
	
class Player(Character):
		
	def __init__(self, name):
		self.name = name
		self.actions = {'attack': self.attack,
					'flee': self.flee,
					'taunt': self.taunt,
					'apocalype': self.apocalype,
					}
					
	def flee(self):
		pass
		
	def taunt(self):
		pass
		
	def attack(self):
		pass
		
	def apocalype(self):
		print("You just ended the world.")
		time.sleep(1)
		print("Well, that was pointless.")
		time.sleep(1)
		print("Enjoy your solitary existence in the void, I guess...")
		time.sleep(10)
		exit(0)
					

class Enemy(Character):

	def __init__(self):
		self.dialogue = {'meet' : [],
						 'hit' : [],
						 'miss' : [],
						 'defeat' : [],
						 'victory' : [],
						}
						
	def play_turn(self):
		pass
	
	def speak(self):
		pass
		
	def die(self):
		pass
		

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
						 
	def attack(self):
		pass
		
	def flee(self):
		pass
		
	def speak(self):
		pass
		
	def die(self):
		pass
		
		

		