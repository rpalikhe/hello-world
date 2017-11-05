def Clinic():
    print("You've just entered the clinic")
    print("Do you take door in the left or right?")
    answer = input("type left or right and hit Enter").lower()
    if answer == 'left' or answer == 'l':
        print("This is the verbal abuse room, you heap of parrot droopings")
    elif answer == 'right' or answer == 'r':
        print("Of course this is the argument room, I've told you that already")
    else:
        print("you didn't pick left or right! Try again")
        Clinic()

Clinic()


