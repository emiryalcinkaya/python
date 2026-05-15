numbers = ['10', '24', '53', '65', '92']

message = "Here is the original list of numbers: "
print(message)
print(numbers)

message = "\nHere is the sorted list of numbers: " 
print(message)
print(sorted(numbers))

message = "\nHere is the reverse sorted list of numbers: " 
print(message)
print(sorted(numbers, reverse=True))
