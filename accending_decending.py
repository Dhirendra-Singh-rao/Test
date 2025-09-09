x={2,32,3,57}
y=list(x)	
for i in range (len(y)):
	for j in range(i+1,len(y)):
		if y[i]>y[j]:
			y[i],y[j]=y[j],y[i]
print("ascending order = ",y)

for i in range(len(y)):
	for j in range(i+1,len(y)):
		if y[i]<y[j]:
			y[i],y[j]=y[j],y[i]
print("decending order = ",y)						



