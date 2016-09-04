import math
import random
random.seed(100)



class Holde(object):
	"""Объект поместье"""
	def __init__(self, coord_x, coord_y, base_profit, name):
		super(Holde, self).__init__()
		# координаты
		self.coord_x = coord_x
		self.coord_y = coord_y
		# base profit
		self.base_profit = base_profit
		self.owner_name = ""
		self.owner_x = 0
		self.owner_y = 0
		self.corruption = 0.0 	#
		self.degradation = 0.0
		self.repair_cost = 1
		self.corruption_k = 0.1 #Коэффициент зависимости коррупциия от удаленности
		self.degradation_temp = 0.1 #Темп деградации
		self.level = 1
		self.profit = 0
		self.random_mul_result = 0
		self.random_add_result = 0
		self.global_state_k = 0.0
		self.treasury = 0
		##
		self.name = name



	def calculate_profit(self):
		if (self.owner_name == ""): 
			return -1
		else :
			profit = self.base_profit*self.level*(1 - self.corruption)*(1-self.degradation)*self.random_mul_result +self.random_add_result
		return profit
	#выполнить один раз за игровой цикл для обновления состояния объекта
	def update (self,state):
		self.corruption = get_corruption()
		self.degradation = self.degradation + self.degradation_temp
		self.global_state_k = get_global_state_k(state)
		self.profit = calculate_profit()
		self.trasury += self.profit

	def pay_money(self):
		money = self.treasury
		self.treasury = 0
		return money

	def set_repair_cost (self, cost) :
		self.repair_cost =  cost 

	def owner_distance(self):
		if (self.owner_name != ""):
			return sqrt((coord_x - owner_x)**2 + (coord_y - owner_y)**2)
		else:
			return -1
	def get_corruption(self):
		if (self.owner_name == ""):
			corruption = 0.0
		else:
			corruption = self.owner_distance()*self.corruption_k
		return corruption

	def set_owner(self, owner_name, owner_x, owner_y):
		self.owner_name =  owner_name
		self.owner_x = owner_x
		self.owner_y = owner_y

	def make_repair(self,cost):
		repair_value = repair_cost * cost
		if (repair_value > degradation): 
			degradation = 0
		else:
			degradation -= repair_value
	def next_level(self):
		self.level++ 
	def get_global_state_k(self,state):
		return state/10.0

	def random_encounter (self) :
		pass 



		

		


