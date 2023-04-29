import pandas

user_input = input("Please enter a word: ")
# TODO 1. Create a dictionary in this format:
df = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_list = [char.upper() for char in user_input]

last_list = []
for char in input_list:
    for (key, value) in alphabet_dict.items():
        if char == key:
            last_list.append(value)

print(last_list)


# 2nd way of TODO 2.
word = input("Enter a word: ").upper()
output_list = [alphabet_dict[letter] for letter in word]
print(output_list)
