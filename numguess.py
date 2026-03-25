import random
def numguess():
    print("🎮 welcome to number guessing game")
    print("you will have 5 attempts to guess the number")
    number=random.randint(1,100)
    attempts=5
    while attempts>0:
        try:
            
            guess=int(input("enter a number (1-100):"))        
            if guess<number:
                print("its lower than the number 📉 enter greater number")
                
            elif guess>number:
                
                print("it's greater than the number 📈 enter smaller number")
                
            else:
                print(f"🎉 correct! you guessed in {10-attempts} attempts.")               
                return
            print(f"you have {attempts} attempts to guess the correct number")
            attempts=attempts-1
        except:
            print("please enter a valid number!")
    print("you lost the game! better luck next time")
numguess()
