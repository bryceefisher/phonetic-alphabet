import csv

with open("nato_phonetic_alphabet.csv", "r") as file:
    csv = csv.reader(file)
    nato_dict = dict(csv)


def generate_phon():
    user_input = input("Want to know the phonetic spelling of a word? Enter a word: ")
    try:
        phonetic_letters = [nato_dict[letter.upper()] for letter in user_input]
        print(phonetic_letters)
    except KeyError:
        print("Only enter letters, not numbers!")
        generate_phon()


generate_phon()

