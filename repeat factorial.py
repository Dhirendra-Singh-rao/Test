n=int(input("enter n value: "))
r=int(input("enter r value"))
x=n-r
fact=1
for i in range(1,n+1):
	fact=fact*i
print("factorial of" ,n,"=",fact)
fact2=1	
for i in range(1,x+1):
	fact2=fact2*i	
print("factorial of",r,"=",fact2)
p = fact/fact2
print(p)