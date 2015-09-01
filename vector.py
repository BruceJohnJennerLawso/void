## vector.py ###################################################################
## vector3 class, first module of the project ##################################
################################################################################


class vector_III:
	"""3 dimensional vector class in python"""
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
		return
	
	def getVec(self):
		output = "(%f, %f, %f)\n" % (self.x, self.y, self.z)
		return output;
	
	def printVec(self): 
		print self.getVec();
		return
		
	def Plus(self, add):
		self.x += add.x
		self.y += add.y
		self.z += add.z
		return
		
	def Minus(self, sub):
		self.x -= sub.x
		self.y -= sub.y
		self.z -= sub.z
		return	
		
	def Dot(self, vec):
		output = ((self.x*vec.x)+(self.y*vec.y)+(self.z*vec.z));
		return output;
		
	def This(self):
		return self;
		# always unto thyself return?
