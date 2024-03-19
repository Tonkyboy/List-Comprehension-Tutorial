# Example 1: Flattening a List of Lists
nested_list = [[1,2], [3,4,5], [6]]

# flattened with a for loop
flattened_list = []
for sublist in nested_list:
    for num in sublist:
        flattened_list.append(num)

print(flattened_list)


# flattened with list comprehension
flattened_list_list = [num for sublist in nested_list
                       for num in sublist]

print(flattened_list_list)



# Example 2: Filtering and Transforming Strings
sentences = ["Hello world", "Python is fun", 
             "Keep it short"]

# filtering and transforming with a for loop
short_word = []
for sentence in sentences:
    words = sentence.split()
    for word in words:
        if len(word) < 5:
            short_word.append(word)

print(short_word)

# filtering and transforming with list comprehension
short_word_list = [word for sentence in sentences 
                   for word in sentence.split() 
                   if len(word) < 5]

print(short_word_list)














