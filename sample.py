name = input("Enter Your Name : ")
age = input("Enter Your Age : ")
contact = input("Enter Your Number : ")
file = open("Personal.txt","a")
file.write("Name = " + name +"\n")
file.write("Age = " + age + "\n")
file.write("Contact = " + contact)
file.close()

file1 = open("Personal.txt","r")
file_data = file1.read()
file1.close()

print(file_data)


"""a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)"""