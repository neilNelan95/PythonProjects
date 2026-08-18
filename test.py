import random

secret_number = random.randint(1,100)

attempts = 1

guess = int(input("Guess a number between 1 and 100: "))

while (guess != secret_number) :


    if (guess < secret_number):
        
        print("\n Number of attempts: " + str(attempts))
        attempts += 1
        guess = int(input("\n Sorry but that's too low! Try again: "))
        
    else:
        print("\n Number of attempts: " + str(attempts))
        attempts += 1
        guess = int(input("\n Sorry but that's too high! Try again: "))

print("\n Congrats! You got it in " + str(attempts) + " attempts!")