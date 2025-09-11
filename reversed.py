var_1 = input("Enter string : ")
var_1 = var_1.split()
rev = []
for i in var_1:
	temp = ""
	for j in range(len(i)-1,-1,-1):
		temp = temp + i[j]
	rev.append(temp)	
temp_2 = ""
for j in range(len(rev)):
	temp_2 = temp_2 + rev[j]
	if j != len(rev)-1:
		temp_2 = temp_2 + " "
print(temp_2)