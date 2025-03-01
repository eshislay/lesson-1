# take user input
decimal_number=int(input("enter a decimal number:"))
binary_number=bin(decimal_number).replace("0b","")
# print result
print(f"binary representation: {binary_number}")