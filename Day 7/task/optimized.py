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



word_list = ["aardvark", "baboon", "camel"]
chosen_word = secrets.choice(word_list)
lives = 6
place_holder_list = ["_" for _ in chosen_word]
guess_history = []

print("Welcome to Hangman!")

while "_" in place_holder_list and lives > 0:
    print(f"\nLives: {lives}")
    print("Word: ", " ".join(place_holder_list))
    print("Guessed letters:", ", ".join(guess_history))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single letter.")
        continue

    if guess in guess_history:
        print("⚠️ You already guessed that. Try again.")
        continue

    guess_history.append(guess)

    if guess in chosen_word:
        print("✅ Correct!")
        for i, char in enumerate(chosen_word):
            if char == guess:
                place_holder_list[i] = guess
    else:
        print("❌ Wrong!")
        lives -= 1
        print(stages[lives])

if "_" not in place_holder_list:
    print(f"\n🎉 YOU WON! The word was: {chosen_word}")
else:
    print(f"\n💀 YOU LOST! The word was: {chosen_word}")
