import random

print ("Hello! This is a random password generator")

while True:
    yn = input("Would you like to create a new password? (Yes/No): ").lower()

    if yn == "yes":
        letter = "abcdefghijklmnopqrstuvwxyz"
        cletter = "ABCDEFGHIJKLMNOPQRSTUVWXZY"
        sletter = "!@#$%^&*()_+=-/*<>:"
        nletter = "1234567890"

        choices = letter+cletter+sletter+nletter

        ranpass = ''.join(random.choices(choices, k=12))
        print ("Your random password is",ranpass)
        yn = input("Would you like to create and new password again? (Yes/No): ").lower()
        if yn == "yes":
            continue
        elif yn == "no":
            quit()
        else:
            print ("Invalid input please try again!")
            continue

    if yn == "no":
        quit()
        
    else:
        print ("Invalid input please try again")
        continue
