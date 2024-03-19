# Example 1: Creating a List of Even Numbers
# evens with a for loop
evens = []
for num in range(1, 11):
    if num % 2 == 0:
        evens.append(num)

print(evens)


# evens with list comprehension
evens_list = [num for num in range(1, 11) if num % 2 == 0]

print(evens_list)


# Example 2: Squaring a List of Numbers
numbers = [1, 3, 5, 7]

# squares with a for loop
squares = []
for num in numbers:
    squares.append(num * num)

print(squares)



# squares with list comprehension
squares_list = [num * num for num in numbers]

print(squares_list)















