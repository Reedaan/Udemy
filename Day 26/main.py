import pandas
data = pandas.read_csv(r"D:\Python\Python Bootcamp\Day 26\NATO\nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Provide a word: ")
user_word_as_list = []
    
user_word_as_list = [(data_dict[user_word[x].upper()]) for x in range(len(user_word))] 

print(user_word_as_list)

