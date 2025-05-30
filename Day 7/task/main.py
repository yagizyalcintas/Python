stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




import secrets
word_list = ["aardvark", "baboon", "cammmel"]
lives=6
place_holder_list=[]
chose_word_list=[]
guess_history=[]

place_holder=""
place_holder_after_guess=""

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
chosen_word = secrets.choice(word_list)
print(chosen_word)
for letter in chosen_word:
    place_holder += "_"
print(place_holder)

for letter in chosen_word:
    place_holder_list.append("_")
    chose_word_list.append(letter)
print(place_holder_list)
print(chose_word_list)


while place_holder_after_guess != chosen_word and lives !=0:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    guess_history.append(guess)
    if guess_history.count(guess) > 1:
        print("you have already guessed it before make another guess")
    else:
        correct_guess = False
        for letter in chosen_word:
            if letter == guess:
                correct_guess=True
                for i in range(chose_word_list.count(letter)):
                    place_holder_list[chose_word_list.index(letter)]= letter
                    chose_word_list[chose_word_list.index(letter)]=""
    
        place_holder_after_guess=""
        for letter in place_holder_list:
            place_holder_after_guess += letter
        print(place_holder_after_guess)
        if not correct_guess:
            print("Wrong!")
            lives -= 1
            print(stages[lives])
        else:
            print(f"right!")
            print(stages[lives])
        if lives == 0:
            print(f"the correct word was {chosen_word}, YOU LOST!")
        elif place_holder_after_guess == chosen_word:
            print("YOU WON!")


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

