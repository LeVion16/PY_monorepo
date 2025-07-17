def get_rate_by_distance(distance_:float) -> int:
    '''Meghatározza a kilométerenkénti díjat a megadott távolság alapján.'''
    if 1 <= distance_ <= 5:
        return 500 # Forint / km
    elif 6 <= distance_ <= 10:
        return 1000
    elif 11 <= distance_ <= 15:
        return 1500
    elif 16 <= distance_ <= 20:
        return 2000
    elif 21 <= distance_ <= 25:
        return 2500
    elif 26 <= distance_ <= 30:
        return 3000

def get_salary(rate_:int, distance_:float) ->float:
    '''Kiszámítja a biciklis futár fizetését a távolság és a díjszabás alapján.'''
    return rate_ * distance_

distance = float(input("Add meg az út hosszát (km-ben): "))

while not 1 <= distance <= 30:
    print("A megadott távolság kívül esik a fizetési tartományon!")
    break

rate = get_rate_by_distance(distance)
salary = get_salary(rate, distance)
print(f"A biciklis futár fizetése: {salary}FT")