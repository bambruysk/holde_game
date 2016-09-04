
class Player(object):
	"""docstring for Player"""
	def __init__(self, name, coord, money):
		super(Player, self).__init__()
		self.name = name
		self.coord = coord
		self.money = money
		self.holdes =  []


	def get_money_from_holdes(self):
		for hold in self.holdes:
			self.money += hold.pay_money()

	def buy_new_holde(self,cost,hold):
		hold.set_owner(self)
		self.holdes.append(hold)

	def repair_holde(self,cost,hold)
		if (cost> self.money):
			return "You need more money for repair!"
		else:
			hold.make_repair(cost)
			return "Hold reapired succesfull!"
	def buff_holde (self,cost,hold,buff)

		