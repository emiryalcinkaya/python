# Exercise 4-3: Counting to Twenty
for number in range(1, 21):
	print(number)

print("Next Exercise") 
# Exercise 4-4: One Million
for number in range(1, 1_000_001):
	print(number)

print("Next Exercise") 
# Exercise 4-5: Summing a Million
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("Next Exercise") 
# Exercise 4-6: Odd Numbers
odd_numbers = list(range(1,21,2))
print(odd_numbers)

print("Next Exercise")
# Exercise 4-7: Threes 
threes_multiples = list(range(3,31,3))
print(threes_multiples)

print("Next Exercise")
# Exercise 4-8: Cubes
cube_numbers = []
for value in range (1,11):
	cube_number = value**3
	cube_numbers.append(cube_number)

print(cube_numbers)

print("Next Exercise")
# Exercise 4-9: Cube Comprehension
cube_comp = [value**3 for value in range(1,11)]
print(cube_comp)
