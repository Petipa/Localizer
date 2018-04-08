from smbus2 import SMBus
import time

adr = 0x0d
bus = SMBus(1)

class QMC5883L(object):

	def __init__(self):
		self.bus = SMBus(1)
		self.offset_X = 0
		self.offset_Y = 0
		self.offset_Z = 0
	 
	
	def set_config(self):
		bus.write_byte_data(adr,0x0b,0x01)
		bus.write_byte_data(adr,0x09,0x0d)
	
	def get_status(self):
		ready=bus.read_byte_data(adr,0x06)
		print("status={}".format(ready))
		
	def _convert_data(self, data):
		magval = ((data[1] << 8) + data[0])
		if magval > (2 ** 15) - 1:
		 magval = magval - (2 **16)
		magval = float(magval) * 2 / 2 ** 15
		return magval
		
	def get_data(self):
	#print the data X, Y, Z converted
		data = bus.read_i2c_block_data(adr,0x00,6)
		X_data = self._convert_data(data[0:2])-self.offset_X		
		Y_data = self._convert_data(data[2:4])-self.offset_Y		
		Z_data = self._convert_data(data[4:6])-self.offset_Z
		data = [X_data, Y_data, Z_data]
		return data
		
				
	def disp_data(self):
		i = 0
		while i < 1:
			data= self.get_data()
			print("data X = {} G".format(data[0]))
			print("data Y = {} G".format(data[1]))
			print("data Z = {} G".format(data[2]))
			time.sleep(1)
			i += 1
	
		
	def calibration(self):
		data = self.get_data()
		self.offset_X = data[0]
		self.offset_Y = data[1]
		self.offset_Z = data[2]
		
		