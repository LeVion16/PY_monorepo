while True:
    try:
        num = int(input("Adj meg egy számot: "))
        print("A megadott szám duplája:", num*2)
        break
    except ValueError:
        print("Kérlek számot adj meg!")