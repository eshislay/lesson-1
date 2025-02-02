s1=int(input("enter your first speed:"))
s2=int(input("enter your second speed:"))
s3=int(input("enter your third speed:"))
average=(s1+s2+s3)/3
print("the average speed is:",average)
if s1<average:
     print("speed 1 is slower than average with difference of",average-s1)
if s2<average:
    print("speed 2 is slower than average with difference of",average-s2)
if s3<average:
    print("speed 3 is slower than average with difference of",average-s3)