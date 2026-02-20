num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
opration=input("Enter the operation you want to perform: ")
if opration=="+":
    print(num1+num2)
elif opration=="-":
    print(num1-num2)
elif opration=="*":
    print(num1*num2)
elif opration=="/":
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1/num2)
else:
    print("Invalid operation. Please enter +, -, *, or /.")