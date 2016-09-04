import randomr
random.seed()

class Dice(object):
	"""docstring for Dice"""
	def __init__(self, number):
		super(Dice, self).__init__()
		self.number = number
	def roll(self):
		return random.randint(1,self.number)
