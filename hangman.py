import random
#predefined list of words
words = ["python", "skills", "coding", "program", "flutter"]

word = random.choice(words)   #taking randon word
word_letters = list(word)     #splitting word into letters
guessed_letters = []      
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("_ " * len(word))        #printing blanks at initial 

while wrong_guesses < max_attempts:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    if guess in word_letters:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_attempts - wrong_guesses}")

    current_progress = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(current_progress))

    if "_" not in current_progress:
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("Game Over! The word was:",word)