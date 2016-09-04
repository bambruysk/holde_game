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
		for i in xrange(0,height-1):
			self.holdes.append([])
			for j in xrange(0,width-1):
				self.holdes[j].append(Holde(j,i,20,"")
		self.holdes[0,0].neighbours = {"N":self.holdes[0,1],"NE":self.holdes[1,0]}
		for j in xrange(1,self.height-1):
			self.holdes[0,j].neighbours{"SW"} = None
			self.holdes[0,j].neighbours{"NW"} = None
			self.holdes[0,j].neighbours{"S"} = self.holdes[0,j-1]
			self.holdes[0,j].neighbours{"SE"} = self.holdes[1,j-1]
			self.holdes[0,j].neighbours{"NE"} = self.holdes[1,j]
			self.holdes[0,j].neighbours{"N"} = self.holdes[0,j+1] if (j != self.height-1) else None


		for i in xrange(2,width-1,2):
			for j in xrange(0,height-1):
				self.holdes[i,j].neighbours{"SW"} = None if (j == 0) else self.holdes[i-1,j-1]
				self.holdes[i,j].neighbours{"NW"} = self.holdes[i-1,j] 
				self.holdes[i,j].neighbours{"N"} = None if ( j == height-1) else self.holdes[i,j+1] 
				self.holdes[i,j].neighbours{"S"} = None if ( j == 0) else self.holdes[i,j-1] 
				self.holdes[i,j].neighbours{"NE"} = None if (i == width-1) self.holdes[i+1,j] 
				self.holdes[i,j].neighbours{"SE"} = None if (i == width-1 or j == 0) else self.holdes[i+1,j-1] 

		for i in xrange(1,width-1,2):
			for j in xrange(0,height-1):
				self.holdes[i,j].neighbours{"SW"} =  self.holdes[i-1,j-1]
				self.holdes[i,j].neighbours{"NW"} = None if (j == height-1) else self.holdes[i-1,j+1] 
				self.holdes[i,j].neighbours{"N"} = None if ( j == height-1) else self.holdes[i,j+1] 
				self.holdes[i,j].neighbours{"S"} = None if ( j == 0) else self.holdes[i,j-1] 
				self.holdes[i,j].neighbours{"NE"} = None if (i == width-1 or j == height-1) self.holdes[i+1,j+1] 
				self.holdes[i,j].neighbours{"SE"} = None if (i == width-1 ) else self.holdes[i+1,j] 


		self.counter = 0

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
		return False
	def getNeighboughrs(self, hold):
		pass

	def distance(self,holde_a, holde_b):
		pass

	def distance_rec(self, holde_a, holde_b, dist):
		counter++;
		if (holde_a.coord_x == holde_b.coord_x and holde_a.coord_y == holde_b.coord_y):
			return counter

		else if (holde_a.coord_x == holde_b.coord_x and holde_a.coord_x > holde_b.coord_x)
			return 