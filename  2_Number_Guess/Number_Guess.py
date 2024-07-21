import random

def main():
    randnumber = random.randrange(0,100)
    print("This is a number guessing game where you have to find the number between 0 and 100")
    print("The game where tell you if you need to go higher or lower to reach the number.")
    print("The goal is to get it within 10 guesses.")
    print("When you guess right it will end the game.")
    number_guess = int(input("Enter a number between 0 and 100: "))
    
    for i in range(1,10):
        if (number_guess == randnumber):
            print("Your guessed the number correctly good job")
            print(f'You guessed the number in {i} guesses')
            break
        elif(number_guess > randnumber):
            print("The number is lower")
            print("Guesses left: ", 11-i)
        elif(number_guess < randnumber):
            print("The number is higher")
            print("Guesses left: ", 11-i)
        
        print(f'You have {11-i} guess/guesses left')
        number_guess = int(input("Enter a number between 0 and 100: "))
        
    
if __name__ == "__main__":
    main()
    
    while(True):
        user_choice = "Would you like to play again?(y/n)"
        if(user_choice.lower() == "y"):
            main()
        else:
            print("Thank you for playing have a good day.")
            break
        