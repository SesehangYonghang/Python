# Number Guessing Game using LOOPS
secret_number = 7
def main():
    Guessing_game()
def Guessing_game():
    
    while True:
        guess = int(input("Enter your guess(NUMBER): "))

        if guess == -1:
            print("Game Exited")
            break
        if guess < 0:
            print("Guess Skipped! Try Again")
            continue
        if guess == secret_number:
            print("🎉 Correct!")
            break
        else:
            print("Wrong Guess, Try Again")
main()
