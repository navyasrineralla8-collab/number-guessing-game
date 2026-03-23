import random
def numguess():
    print("🎮 welcome to number guessing game")
    number=random.randint(1,100)
    attempts=0
    while True:
        try:
            guess=int(input("enter a number (1-100):"))
            attempts+=1
            if guess<number:
                print("its lower tahan the number 📉 enter greater number")
            elif guess>number:
                print("it's greater then the number 📈 enter smaller number")
            else:
                print(f"🎉 correct! you guessed in {attempts} attempts.")
                break
        except:
            print("please enter a valid number!")
numguess()
