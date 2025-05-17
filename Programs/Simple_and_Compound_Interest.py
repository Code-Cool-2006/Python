P = float(input("Enter the principle amount : "))
R = float(input("Enter the rate of interest : "))
T = float(input("Enter the time in years : "))
n = int(input("Enter the no of times the interest is compounded : "))
amt = P*1+R/n ** n*T
CI = amt - P
SI = (P*R*T)/100
print("The Simple Interest is : " + str(SI))
print("The Compound Interest is : " + str(CI))