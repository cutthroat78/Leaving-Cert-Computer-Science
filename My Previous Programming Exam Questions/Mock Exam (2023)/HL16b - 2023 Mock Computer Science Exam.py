import random

faces = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]

suits = ["C","D","H","S"]

player_face = faces[random.randint(0,12)]
player_suit = suits[random.randint(0,3)]

player_face_num = int(player_face)

if player_suit == "S":
    player_suit_num = 4
elif player_suit == "H":
    player_suit_num = 3
elif player_suit == "D":
    player_suit_num = 2
elif player_suit == "C":
    player_suit_num = 1

player_draw = player_face + player_suit

print("Your draw was: " + player_draw)

bet = int(input("Please enter your bet: "))

computer_face = faces[random.randint(0,12)]
computer_suit = suits[random.randint(0,3)]

computer_face_num = int(computer_face)

if computer_suit == "S":
    computer_suit_num = 4
elif computer_suit == "H":
    computer_suit_num = 3
elif computer_suit == "D":
    computer_suit_num = 2
elif computer_suit == "C":
    computer_suit_num = 1

computer_draw = computer_face + computer_suit

print("The computer draw was: " + computer_draw)

if computer_face_num > player_face_num:
    print("You lose!")
elif computer_face_num < player_face_num:
    print("Well done\nYou win: € " + str(bet * 3))
elif computer_face_num == player_face_num and computer_suit == player_suit:
    print("Draw")
elif computer_suit_num > player_suit_num:
    print("You lose!")
elif computer_suit_num < player_suit_num:
    print("Well done\nYou win: € " + str(bet * 3))
