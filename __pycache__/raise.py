try:
    age=int(input("enter age:"))
    if age<18:
       raise ValueError
    else:
        print("eligible")
except ValueError:
    print("invalid age")
       