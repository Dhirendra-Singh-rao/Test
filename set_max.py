#write a py script to find the maximum and minimum value in a set 
x = {2,32,3,52}
print(x)
min = None
max = None

for i in x : 
	if min == None :
		min = i
	elif min > i :
		min = i

for j in x : 
	if max == None :
		max = j 
	elif max < j : 
		max = j 

print("minimum Value : ",min)
print("maximum Value : ",max)

#write py script to sort a set in ascending and descending order