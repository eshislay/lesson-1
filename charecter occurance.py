string=input("please enter your own word:")
char=input("please enter your own charecter:")
i=0
count=0
while(i < len(string)): #string operation
    if(string[i] == char): #condition 1
      count = count + 1
    i=i+1  
print("the total number of times",char,"has occured =",count)