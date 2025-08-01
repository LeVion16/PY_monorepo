import random

num = random.randint(1,100)
user_input= ''

while user_input != num:
    user_input = int(input("Gondoltam egy számra! Szerindet melyik lehet az: "))
    if user_input == num:
        print("Gratulálok, kitaláltad a helyes megoldást:", num)
    else:
        print("Sajnos ez nem talált! Próbáld újra!")
        if user_input < num:
            print("A szám amire gondoltam nagyobb.")
        else:
            print("A szám amire gondoltam kisebb.")