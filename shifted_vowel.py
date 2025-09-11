x=input("enter a string : ")
print(x)
for i in x:
	for j in i:
		if j == "a":
			x = x.replace("a","e")
		elif j == "e":
			x = x.replace("e","i")
		elif j == "i":
			x = x.replace("i","o")
		elif j == "o":
			x = x.replace("o","u")
		elif j =="u":
			x = x.replace("u","a")
print("shifted vowels = ",x)						