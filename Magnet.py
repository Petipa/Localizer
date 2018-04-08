import Formula

class Magnet(object):

	def __init__(self):
		self.coeff_A = 1
		self.coeff_B = -0.1
		
	def get_coeff_A(self):
		return self.coeff_A
		
	def get_coeff_B(self):
		return self.coeff_B