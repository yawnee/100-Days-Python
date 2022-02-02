# ----------------- Notes ----------------------------------------
# #fileNotFound
# with open("asdasdasd.txt") as file:
#     file.read()
#
# #keyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exist_ent"]
#
# #indexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]
#
# #typeError
# text = 'abc'
# print(text + 5)

# Executing something that might cause an exception (attempt)
#try:

# Do this if there was an exception (fail)
#except:

# Do this if there was no exception (success)
#else:

# Do this no matter what happens (must do)
#finally:

# Raise our own exceptions
#raise

# --------------------------------------------------------------------

#fileNotFound
# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key':'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print('File was closed.')

# ----------------------------------------------------------------------

#Raise notes
# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key':'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError('This is an error that I made up')

# --------------------------------------------------------------------

# Raise example 2

height = float(input('height: '))
weight = int(input('weight: '))
if height > 3:
    raise ValueError('Human height should not be over 3 meters.')

bmi = weight / height ** 2
print(bmi)







