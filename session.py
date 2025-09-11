def check_session(m):
	if m=="september" or m=="october" or m=="november":
		print(m,"is the autumn session month")
	elif m=="december"or m=="january" or m=="february":
		print(m,"is the winter session month")
	elif m=="march" or m=="april" or m=="may":
		print(m,"is the spring session month")
	elif m=="june" or m=="july" or m=="august":
		print(m,"is the summer session month")
	else:
		print("invalid syntax")
m=input("enter the month name : ")
check_session(m)		
