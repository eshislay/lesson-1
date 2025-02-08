print("age eligibility check")
age =int(input("enter your age:"))
# checking the eligibility criteria
if 10<= age <=20:
    if age>= 15:
     print("you are eligible for admission in senior category.")
    else:
       print("you are eligible for admission in junior category.")
else:
     print ("you are not eligible for admission")