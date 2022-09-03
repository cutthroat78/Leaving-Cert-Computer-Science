# Question 16(a)
 # Prompt the user to enter a password and store the ...
 # value entered in the variable password
password = input("Enter a password: ")

 # A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter
numbers = False # True if password contains a number

# Loop through each character in the password and ...
# check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in UPPER_CASE_LETTERS:
        uppercase = True
    if character in NUMBERS:
        numbers = True

# Calculate the score based on the rules

score = 0 # Initalise Score

# Rule 1
if len(password) > 7:
    score += 5
elif len(password) < 7 and len(password) > 4:
    score += 2
elif len(password) < 4:
    score -= 2

# Rule 2
if lowercase:
    score += 1
# Rule 3
if lowercase and uppercase:
    score += 5

# Rule 4
if uppercase:
    score += 2

# Rule 5
if numbers:
    score += 5

# Rule 6
if password[0] in NUMBERS:
    score += 1
if password[-1] in NUMBERS:
    score += 1
if password[0] in NUMBERS and password[-1] in NUMBERS:
    score += 2

# Rule 7
if password.isdigit():
    score -= 10

# Display the score
print("Password: " + str(password) + "\nScore: "+ str(score))
