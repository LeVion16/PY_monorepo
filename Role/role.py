def is_correct(height_:int, age_:int, name_:str):
    '''Ellenőrzi, hogy a megadott személy alkalmas-e a szerepre életkor, valamint magasság alapján és
    ha nem felel meg, felsorolja az elutasítás okait.'''
    reasons = [] # Ebbe a listába gyüjtjük az okokat!

    if age_ > 28:
        reasons.append("Életkor nem megfelelő")
    if height_ < 170:
        reasons.append("Magasság nem megfelelő")

    if reasons:
        reasons_text = ", ".join(reasons) # Szépen írja ki
        print(f"Kedves {name_}, maga nem alkalmas a szerepre. Az elutasítás oka(i): {reasons_text}")
    else:
        print(f"Kedves {name_}, maga alkalmas a szerep megszerzéséhez!")

name = input("Add meg a neved: ")
age = int(input("Adja meg az életkorát: "))
height = int(input("Adja meg a magasságát: "))

is_correct(height, age, name)