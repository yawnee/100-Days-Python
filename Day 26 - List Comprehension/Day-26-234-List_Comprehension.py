# Comments
# List comprehension is taking an old list and making a new list out of it by using one line
# example: new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]

# Example 1 - Increasing the numbers in the list by 1
print("Increasing the numbers in the list by 1")
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

print("")

# Example 2 - Splitting each letter
print("Splitting each letter")
name = "Angela"
new_list = [letter for letter in name]
print(new_list)

print("")

# Example 3 - Adding range by doubling each number
print("Adding range")
double_list = [a*2 for a in range(1, 5)]
print(double_list)

print("")

# Example 4 - Conditional list comprehension
print("Conditional list comprehension")
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(names)
short_names = [name for name in names if len(name) < 5]
print(short_names)

print('')

# Example 4 - Change list to upper
print("Change list to upper case")
upper_case_names = [name.upper() for name in names if len(name) > 5]
print(upper_case_names)

