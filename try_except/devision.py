while True:
    try:
        num1 = int(input("Add meg az osztandót: "))
        num2 = int(input("Add meg az osztót: "))
        print("A két szám elosztva: ", num1 // num2 == 0)
        break
    except ZeroDivisionError:
        print("Nullával nem lehet osztani! Próbáld újra!")
    except ValueError:
        print("Kérlek számot adj meg!")
