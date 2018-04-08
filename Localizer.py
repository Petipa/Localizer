import QMC5883L
import math
import Magnet
from Formula import cube


class Localizer(object):

	def __init__(self):
		self.magneto = QMC5883L.QMC5883L()
		self.magnet = Magnet.Magnet()
		
	
	def get_distance(self):
		data = self.magneto.get_data()
		coeff_A = self.magnet.get_coeff_A()
		coeff_B = self.magnet.get_coeff_B()
		position = ( 1/ (coeff_A*cube(coeff_B*data[2])))
		print ("dataZ ={}".format(data[2]))
		print ("coeff_A ={}".format(coeff_A))
		print("the distance between the magnet and the magnetometer is {} cm".format(position))
		
	def get_debug(self):
		print("debug")
		data = self.magneto.get_data()
		coeff_A = self.magnet.get_coeff_A()
		coeff_B = self.magnet.get_coeff_B()
		
		if data[0] != 0
			Bx = ( 1/ (coeff_A*cube(coeff_B*data[0])))
		else Bx = 0
		if data[1] != 0
			By = ( 1/ (coeff_A*cube(coeff_B*data[1])))
		else By = 0
		if data[2] != 0
			Bz = ( 1/ (coeff_A*cube(coeff_B*data[2])))
		else Bz = 0
		
		R = sqrt(Bx**2+By**2+Bz**2)
		Phi = math.atan(By/Bx)
		Theta = math.acos(Bz/R)
		
		print ("Bx ={}".format(Bx))
		print ("By ={}".format(By))
		print ("Bz ={}".format(Bz))
		print ("R ={}".format(R))
		print ("Phi ={}".format(math.degrees(Phi)))
		print ("Theta ={}".format(math.degrees(Theta)))
		