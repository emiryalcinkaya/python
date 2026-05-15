# Exercise 5-2: More Conditional Tests

name = 'Emir'
city = 'Berlin'
age = 21
foods = ['pizza', 'burger', 'pasta']

# Equality and inequality with strings
print(name == 'Emir')
print(name == 'Ahmet')

print(city != 'Munich')
print(city != 'Berlin')

# Using lower()
print(city.lower() == 'berlin')
print(name.lower() == 'emir')
print(name.lower() == 'ahmet')

# Numerical tests
print(age == 21)
print(age != 18)

print(age > 18)
print(age < 18)

print(age >= 21)
print(age <= 20)

# Using and
print(age > 18 and city == 'Berlin')
print(age > 25 and city == 'Berlin')

# Using or
print(age > 25 or city == 'Berlin')
print(age < 18 or city == 'Munich')

# Item in a list
print('pizza' in foods)
print('sushi' in foods)

# Item not in a list
print('sushi' not in foods)
print('burger' not in foods)
