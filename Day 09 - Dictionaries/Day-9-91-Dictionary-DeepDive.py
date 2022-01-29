#Dictionaries have a key and a value. {key: value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)

#adding dictionaries
programming_dictionary["Loop"] = "This sentence is now added to the dictionary"
print(programming_dictionary)

#creating empty dictionary
empty_dictionary = {

}

#wiping dictionary
#programming_dictionary = {}

#edit an item in a dictionary
programming_dictionary["Bug"] = "This is now a bug"
print(programming_dictionary)

#loop through a dictionary
#Gives you only the keys
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

