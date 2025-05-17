a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print('''
      Add or add - Addition
      Sub or sub- Subtraction
      Mul or mul - Multiplication
      Pow or pow - Power
      Div or div - Division
      Floor or floor - Floor Division
      Mod or mod - Modulus
      ''')

def add(a,b):
    c =  a + b
    print(c)
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b        
def pow(a,b):
    return a ** b
def div(a,b):
    return a / b
def floor(a,b):
    return a // b
def mod(a,b):
    return a % b

res = str(input("Enter the operation : "))

if res == "Add" or res == "add":
    print("The sum of",a,"and",b,"is",add(a,b)) 
elif res == "Sub" or res == "sub":
    print("The difference of",a,"and",b,"is",sub(a,b))
elif res == "Mul" or res == "mul":
    print("The product of",a,"and",b,"is",mul(a,b))
elif res == "Pow" or res == "pow":
    print("The power of",a,"and",b,"is",pow(a,b))
elif res == "Div" or res == "div":
    print("The quotient of",a,"and",b,"is",div(a,b))
elif res == "Floor" or res == "floor":
    print("The floor division of",a,"and",b,"is",floor(a,b))
elif res == "Mod" or res == "mod":
    print("The remainder of",a,"and",b,"is",mod(a,b))
else:
    print("Invalid operation")
