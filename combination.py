'''n=int(input("enter n value: "))
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
fact3=1
for i in range(1,r+1):
	fact3=fact3*i	
c = fact/(fact2*fact3)
print(c)'''





def fact(n):
	result=1
	for i in range(1,n+1):
		result=result*i
	return result 
a=int(input("enter a :"))
b=int(input("enter b :"))	
result_a=fact(a)
result_c=fact(a-b)
result_b=fact(b)	
acb=result_a/(result_c*result_b)
print("{}c{}={}".format(a,b,acb))