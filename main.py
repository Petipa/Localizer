import Localizer

localizer = Localizer.Localizer()

quit = False
while quit == False:

	print("hello, it is the console")
	print("(1) Initilization")
	print("(2) Calibration")
	print("(3) Display data")
	print("(4) Get status")
	print("(5) Get position")
	print("(0) Quit")
	print("(10) Debug")
	input_key = input("please press one key \n")


	if input_key == "1":
		localizer.magneto.set_config()
	elif input_key == "2":
		localizer.magneto.calibration()
	elif input_key == "3":
		localizer.magneto.disp_data()
	elif input_key == "4":
		localizer.magneto.get_status()
	elif input_key == "5":
		localizer.get_distance()
	elif input_key == "10":
		localizer.get_debug()
	elif input_key == "0":
		quit = True
	else:
		print ("please choose another input")