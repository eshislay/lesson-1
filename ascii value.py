# get user input
char=input("enter a character:")

# check if the input is a single character
if len(char)==1:
    # get ASCII value using ord() function
    ascii_value=ord(char)
    print(f"the ASCII value of'{char}'is {ascii_value }")
else:
    print("please enter a single character.")
