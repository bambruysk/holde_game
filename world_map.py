import holde
import math
#    / \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_
#    \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_
#    / \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_
#    \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#    / \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_
#    \_/ \_/c\_/ \_/ \_/ \_/ \_/ \_/ 
#    / \_/ \_/ \_/d\_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_
#    \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#    / \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_
#    \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 


class World_Map(object):
	"""docstring for World_Map"""
	def __init__(self, number,width,height):
		super(World_Map, self).__init__()
		self.number = number
		self.width = width
		self.height = height
		self.holdes = []
		for i in xrange(1,height):
			self.holdes.append([])
			for j in xrange(1,width):
				holdes[j].append(Holde(j,i,20,"")

	def isNeighboughr(self,holde_a,holde_b):
		if (holde.coord_x % 2 == 0): 
			if (math.abs(holde_a.coord_x - holde_b.coord_x) == 1):
				if (holde_a.coord_y == holde_b.coord_y or holde_a.coord_y == holde_b.coord_y + 1):
					return True
			else if (holde_a.coord_x == holde_b.coord_x):
				if (math.abs(holde_a.coord_y - holde_b.coord_y) == 1):
					return True
		else :
			if (math.abs(holde_a.coord_x - holde_b.coord_x) == 1):
				if (holde_a.coord_y == holde_b.coord_y or holde_a.coord_y == holde_b.coord_y - 1):
					return True
			else if (holde_a.coord_x == holde_b.coord_x):
				if (math.abs(holde_a.coord_y - holde_b.coord_y) == 1):
					return True
		return FAlse
	def getNeighboughrs(self, hold):
		