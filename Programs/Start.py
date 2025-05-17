# print("Hello World!")

# a = int(input("Enter First Number : "))
# b = int(input("Enter Second Number : "))
# result = a + b
# print("The sum of",a,"and",b,"is", result)


# greeting = "Welcome"
# name = input("Enter your name : ")
# print(greeting + " " + name)

# parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[3])
# print(parrot[-1])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

name = str(input("Enter your Name : "))
age = int(input("Enter your age : "))
height = float(input("Enter your height in feet : "))
student = str(input("Are you a Student : (Yes/NO) "))
is_student=True
no_student=False
if student=="Yes" or student=="YES" or student=="yes" :
    student=is_student
elif student=="NO" or student=="No" or student=="no" :
    student=no_student
else:
    print("Invlaid Entry")
    exit()
print(""" 
      Thank you for entering your details
      Here are your Detials
      Please confirm them
""")

print(f"Name : {name}")
print("Age : ",age)
print("Height : ",height)
print("Student : ",is_student)




