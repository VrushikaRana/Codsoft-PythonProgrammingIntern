# Making a Calculator which performs "Arithmetic Operations" in Python language

print("Choose one to perform any of the following operations: ")
print(" 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Modulus \n 6.Exponentiation \n 7.Floor Division \n 8.To Exit")
choice=int(input("Enter your choice : "))

if choice == 8:
    print("Arithmetic Calculator Application is Closing!!!")
    
# taking float as input, hence one can even get the answers for their float values.
num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))

def addition(num1,num2):
    return (num1 + num2)

def substraction(num1,num2):
    return (num1 - num2)

def multiplication(num1,num2):
    return (num1 * num2)
    
def division(num1,num2):
    return (num1 / num2)

def modulus(num1,num2):
    return (num1 % num2)

def exponentiation(num1,num2):
    return (num1 ** num2)

def floor_division(num1,num2):
    return (num1 // num2)

if choice == 1:
    print("Addition of two numbers :", addition(num1,num2))
       
elif choice == 2:
    print("Substraction of two numbers :",substraction(num1,num2))

elif choice == 3:
    print("Multiplication of two numbers :",multiplication(num1,num2))

elif choice == 4:
    print("Division of two numbers :",division(num1,num2))

elif choice == 5:
    print("Modulus of two numbers :",modulus(num1,num2))
       
elif choice == 6:
    print("Exponentiation of two numbers :",exponentiation(num1,num2))
       
elif choice == 7:
   print("Floor Division of two numbers :",floor_division(num1,num2))
           
else:
    print('Invalid Input!!!...\n "You can try again"')
    


