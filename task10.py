text = ["apple", "34", "banana", "100", "abc", "75"]

numbers = list(filter(str.isdigit, text))
print(numbers)
