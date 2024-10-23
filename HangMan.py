import random

def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'computer']
    

    word = random.choice(word_list)
    word_length = len(word)
    

    display = ['_'] * word_length
    

    attempts = 6
    guessed_letters = []
    
    print("Welcome to Hangman!")
    

    while attempts > 0:
        print(f"\nWord: {' '.join(display)}")
        print(f"Wrong guesses left: {attempts}")
        

        guess = input("Guess a letter: ").lower()
        

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single alphabetic letter.")
            continue


        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
    
        guessed_letters.append(guess)
        
    
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            

            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1
        

        if "_" not in display:
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    

    if attempts == 0:
        print(f"\nGame over! The word was: {word}")


hangman()
