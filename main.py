import csv

with open("nato_phonetic_alphabet.csv", "r") as file:
    csv = csv.reader(file)
    nato_dict = dict(csv)

user_input = input("Want to know the phonetic spelling of a word? Enter a word: ")
indv_letters = list(user_input)

phonetic_letters = []

for letter in indv_letters:
    phonetic_letters.append(nato_dict[letter.upper()])

print(phonetic_letters)



