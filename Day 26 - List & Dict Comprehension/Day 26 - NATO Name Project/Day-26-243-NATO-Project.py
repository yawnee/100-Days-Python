# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(data.to_dict())
# #TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [print(phonetic_dict[letter]) for letter in word]



# ------- My solution below works perfectly but is different method from lesson ----
# #TODO 1. Create a dictionary in this format:
# #{"A": "Alfa", "B": "Bravo"}
# # convert the csv and turn it into a dictionary
# import pandas
#
# data = pandas.read_csv('nato_phonetic_alphabet.csv')
# nato_dict = {}
#
# for (index, row) in data.iterrows():
#     letter = row.letter
#     word = row.code
#     nato_dict.update({letter: word})
#     nato_dict.update({letter: word})
#
# print(nato_dict) # debugging - dict created
#
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# answer = input('Enter a word: ')
# print("")
#
# characters = [letter for letter in answer]
# for each_letter in characters:
#     upper_letter = each_letter.upper()
#     print(nato_dict[upper_letter])
