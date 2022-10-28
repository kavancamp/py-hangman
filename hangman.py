import random
from words import words 
import string

def get_valid_word(words):
  word = random.choice(words) #randomly chooses from list
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word


def hangman():
  word = get_valid_word(words)
  word_letters = set(word) 
  alphabet = set(string.ascii_uppercase)
  used_letters = set() #what the user has guessed

  user_letter = input('Guess a letter: ').upper()
  if user_letter in alphabet - used_letters:
    used_letters.add(user_letter)
    if user_letter in word_letters:
      word_letters.remove(user_letter)
  elif user_letter in used_letters:
    print('You have already used that character. Try again')
  else: 
    print('Invalid character. Please enter a letter.')
    


user_input = input('Type something')
print(user_input)