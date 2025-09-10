#write a py.script to convert a sentance in each firstword capitl letter 
x=input("enter a sentance : ")
y = x.split(" ")
result=""
for word in y:
	capital_word = ""
	for j in range(len(word)):
		if j == 0:
			first = word[j]
			capital_word=capital_word+first.upper()
		else:
			capital_word= capital_word+word[j].lower()
	if result=="":
		result=capital_word
	else:
		result=result+" "+capital_word
print(result)		