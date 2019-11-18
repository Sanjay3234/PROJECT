name=input("PLEASE ENTER YOUR NAME =")
while name.isalpha()==False or len(name)<8 :
    if ' ' in name:
        break
    else:
        print("THE NAME YOU ENTERED IS INCORRECT")
    name=input("ENTER THE NAME AGEIN =")
print("HELLO SIR ! NOW YOU CAN USE THE CALCULATOR FOR FOLLOWING OPERATIONS")
print("Select the operation you want to perform")
print("1.Add    2.Subtract     3.Multiply      4.Divide     5.Reminder     6.Quotient      7.Power")
Choice=int(input("Enter your choice(1/2/3/4/5/6/7):"))
if Choice == 1:
    num1 = int(input("Enter first number ="))
    num2 = int(input("Enter second number ="))
    sum=num1+num2
    print("Sum of num1 and num2 =",num1+num2)
elif Choice == 2:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Difference=num1-num2
    print("Difference of num1 and num2 =", num1 - num2)
elif Choice == 3:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Multiplication=num1*num2
    print("Multiplication of num1 and num2 =", num1 * num2)
elif Choice == 4:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Divide=num1/num2
    print("Division of num1 and num2 =", num1 / num2)
elif Choice == 5:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Quotiend=num1//num2
    print("Quotient after dividing num1 and num2 =", num1 // num2)
elif Choice == 6:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Reminder=num1%num2
    print("Reminder after dividing num1 and num2 =", num1 % num2)
elif Choice == 7:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    power=num1**num2
    print("Power of num1 by num2 =", num1 ** num2)

