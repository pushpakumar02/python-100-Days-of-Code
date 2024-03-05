PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_files:
    letter_contents = letter_files.read()
    for name in names:
        new_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, new_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
