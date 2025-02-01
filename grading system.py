print("grading system for exams")
sub1=input("enter marks for first subject:")
sub1=int(sub1)
sub2=input("enter marks for first subject:")
sub2=int(sub2)
sub3=input("enter marks for first subject:")
sub3=int(sub3)
sub4=input("enter marks for first subject:")
sub4=int(sub4)
sub5=input("enter marks for first subject:")
sub5=int(sub5)
sum=sub1+sub2+sub3+sub4+sub5
average=sum/5
print("average:",average)
if average>=90 and average<=100:
    print("grade A+")
elif average>=80 and average<90:
    print("grade A")
elif average>=70 and average<80:
    print("grade B")
elif average>=60 and average<70:
    print("grade C")
elif average>=50 and average<60:
    print("grade D")
else:
    print("grade F")
