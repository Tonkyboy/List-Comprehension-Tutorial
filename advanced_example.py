# Example 1: Creating a Dictionary from Lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

# with a for loop
person_data = {}
for i in range(len(keys)):
    person_data[keys[i]] = values[i]

print(person_data)


# with list comprehension
person_data_list = {key: value for key, value in zip(
    keys, values)}

print(person_data_list)



# Example 2: Matrix Transposition
matrix = [[1, 2, 3], [4, 5, 6]]

# with a for loop
result = []
for i in range(len(matrix[0])):
    temp_row = []
    for row in matrix:
        temp_row.append(row[i])
    result.append(temp_row)

print(result)


# with list comprehension
result_list = [[row[i] for row in matrix] for i in 
               range(len(matrix[0]))]

print(result_list)















