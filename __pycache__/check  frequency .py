# Define the test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:", test_dict)

# Ask the user to enter the value to check the frequency
value_to_check = input("Enter the value to check its frequency: ")

# Check the frequency of the entered value in the dictionary
frequency = test_dict.get(value_to_check, 0)

# Print the frequency of the value
print(f"The frequency of '{value_to_check}' is: {frequency}")