import random

def compare_numbers(number, user_guess):
    cow = 0 #establish variables to count cows and bulls
    bull = 0
    for index in range (4): #for every digit in the sequence, check if it is a cow or a bull
        if user_guess[index] == number[index]: #if the digit is in the right position in the sequence, it's a bull
            bull+=1
        elif user_guess[index] in number: #if the digit is in the sequence but in the wrong place, it's a cow
            cow+=1
    return (cow, bull)

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number
guesses = 0
print(number) #change to print(number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #cahnge from raw_input to input
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")