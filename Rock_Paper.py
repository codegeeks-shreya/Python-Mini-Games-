import random

password = " "
while password != "123":                             # can also write it as    while true:  password = input ("Enter password: ")
    password = input("Enter your password: ")                                                   #  if password == shreya@123: break
print("Access Granted")                                                                         #  print ("Access Granted")


print("Welcome to Rock-Paper-Scissors Game! ")

name = input("Please enter your name? ")


yNinput = input("Do you want to play this game? ")
# print(player)
while yNinput.lower() != "yes":
    print("Sorry, you didn't answer. Please try again.")
    yNinput = input("Do you want to play this game? ")
    if yNinput.lower() == "q" or yNinput.lower() == "no":
        print("Have a nice day! ")
        quit()


print("Okay!", name , "Let's play the game :) ")

computer_wins = 0
player_wins = 0
draws = 0

options = ["rock", "paper", "scissor"]
#computer_choice = random.choice(options)

while True:
    user_input = input("Choose Rock/Paper/Scissor or Q to Quit : ").lower()
    if user_input == "q":
        print("You quit :(")
        break
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    computer_choose = options[random_number]
    print("Computer choose: ", computer_choose)

    if user_input == computer_choose:
        print ("Its a draw!")
        draws += 1
    elif (user_input == "rock" and computer_choose == "scissor") or (user_input == "paper" and computer_choose == "rock") or (user_input == "scissor" and computer_choose == "paper"):
        print ("You won!")
        player_wins += 1
    else:
        print ("You lost!")
        computer_wins += 1

print("Scorecard: User: ", player_wins, ",  Computer:", computer_wins , ", Draws: ", draws)