# new_list = [expression for item in iterable if condition]


numbers = [1, 2, 3, 4, 5]

# Square numbers for loop
squared_number = []
for number in numbers:
    squared_number.append(number * number)

print(squared_number)


# Square numbers list comprehension
squared_number_list = [number * number for number 
                       in numbers]

print(squared_number_list)