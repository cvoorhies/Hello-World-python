import random



word_list = ('joy', 'ahead', 'beginning', 'window', 'father', 'dog')

#generate random word
answer_len = 0
answer = random.choice(word_list)
answer_len = len(answer)
num_Wrong_Guesses = 0
current_guess_index = 0
current_guessed_Letters = []
num_Guesses = 0
print()
print()
# print the word image
for char in answer:
    print ('*', end='')

#print correct letters guessed


# print the hangman game board
def print_hangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")

#show correct guesses
def showLetters(guessedLetters):
    counter = 0
    correctguesses = 0
    for char in answer:
        if(char in guessedLetters):
            print (answer[counter], end=" ")
            correctguesses += 1
        else:
            print('*', end='')
        counter+=1
    return correctguesses

def printLines():
  print("\r")
  for char in answer:
    print("\u203E", end=" ")



#play game
def game():
    print("Welcome to hangman")
    print("-------------------------------------------")
    num_Wrong_Guesses = 0
    current_guess_index = 0
    current_guessed_Letters = []
    num_Guesses = 0
   #print(answer_len)
    #print_hangman(num_Wrong_Guesses)
    while(num_Wrong_Guesses != 6 and num_Guesses != answer_len):
        num_Guesses = showLetters(current_guessed_Letters)
        print()
        print('letters guessed so far: ')
        print(current_guessed_Letters)
        print()
        guessed_Letters = input('Choose a letter: ')

        if(answer[current_guess_index] == guessed_Letters):
            print_hangman(num_Wrong_Guesses)
            #Print word
            current_guess_index+=1
            current_guessed_Letters.append(guessed_Letters)
            num_Guesses = showLetters(current_guessed_Letters)
            print()
            
        else:
            num_Wrong_Guesses += 1
            current_guessed_Letters.append(guessed_Letters)
            print_hangman(num_Wrong_Guesses)
            num_Guesses = showLetters(current_guessed_Letters)
            print()
            print()
            
            
        if(num_Guesses == answer_len):
            print("You Win!!!")
        else:
            print('You Lose!!')

yes_no = input('Would you like to play hangman: ')
if(yes_no == 'yes' or  'y' or 'Y'):
   game()
else:
   print('Good Bye')
   exit