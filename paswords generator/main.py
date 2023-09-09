import random
from random import shuffle
def pasword_generator():

    words = []
    unique_char = ["#","%","@","&","_"]
    password = ""
    length = int(input("enter the password length: "))

    while True:
        word = input("Enter the words you like. Or F if finish: ")
        if word == "F":
            break
        words.append(word)

    while True:
        shuffle(words)
        random_counter = random.randint(0, 10)

        if 0<random_counter and random_counter < 5:
            password += unique_char[random.randint(0, len(unique_char)-1)]

        if 5<random_counter and random_counter <= 10:
            password += str(random.randint(0, 10))

        else:
            random_word = words[random.randint(0, len(words)-1)]
            random_letter = random_word[random.randint(0, len(random_word)-1)]
            password += random_letter

        if len(password) == length:
            break

    return password

    
if __name__ == '__main__':
    print(pasword_generator())