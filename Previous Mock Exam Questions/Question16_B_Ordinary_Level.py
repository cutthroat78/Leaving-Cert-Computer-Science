#Question 16(b)
#Write your name here:
import random
words = ["cat", "mat", "can", "man", "pool", "tool", "mule", "pat", "tan", "rule"]
print("The list of word is: ", words)
random_word = words[random.randint(0,len(words)-1)]

print("The length of the word is:", len(random_word))

print("The first letter in the word is:", random_word[0])


tries = 0

while True:
  user_guess = input("Please guess what the word is: ")
  if user_guess == random_word:
    print("Well done!")
    break
  else:
    print("You guessed incorrectly, try again")
    tries += 1
    if tries == 3:
        break

print("The word was:", random_word)
