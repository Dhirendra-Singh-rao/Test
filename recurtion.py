import function as fun 


def select():
	choice = int(input("Press 1 for add\nPress 2 for sub\nPress 3 for mul\nEnter a valid choice : "))
	if choice == 1 :
		result = fun.addition()
		print(result)
	elif choice == 2 :
		result = fun.substraction()
		print(result)
	elif choice == 3 : 
		result = fun.multiplication()
		print(result)
	else : 
		print("Invalid Choice")
		select()

select()