print("number is greater,less or egual")
n1=input("enter first number:")
n1=int(n1)
n2=input("enter second number:")
n2=int(n2)
n3=input("enter third number:")
n3=int(n3)
if n1>n2 and n1>n3:
    print(n1,"is greater")
elif n2>n1 and n2>n3:
    print(n2,"is greater")
else:
    print(n3,"is gretaer")