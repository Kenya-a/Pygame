import random

secret = random.randint(1, 50)

attempts = 0

while True: 
    
    guess = int(input("this is my guess: "))
    attempts += 1

    if guess == secret:
        print("you got it!")
    elif guess <= secret: 
        print("try higher")
    else: 
        print("try lower")