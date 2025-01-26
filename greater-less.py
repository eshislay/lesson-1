print ("NUMBER IS greater,less than OR equal")
number1=input("enter 1st number:")
number1=int(number1)
number2=input("enter 2nd number:")
number2=int(number2)
if number1>number2:
    print(number1,"is greater than",number2)
elif number1<number2:
    print(number1,"is less than",number2)
else:
    print(number1,"is equal than",number2)