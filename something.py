print("hello, world")

import random

print("This is my guessing game!")

secret_number = random.randint(1,1000)

attempt = 0

while True: 
    guess = int(input("This my guess : "))
    attempt += 1

    if guess == secret_number:
        print("Ya!")
    elif guess <= secret_number:
        print("try higher")
    else:
        print("your wrong,try agian")
        print(attempt)

        break




    




