for i in range(0,109):
	if (i<10):
		print('000%d.sdf,'%i, end ="")
	if (i<100 and i>9):
		print('00%d.sdf,'%i, end ="")
	if (i<1000 and i>99):
		print('0%d.sdf,'%i, end ="")		
