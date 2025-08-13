import random

print("Ez egy kő-papír-olló játék. A kilépéshez irja be: Kilépés.")
eszközök = ['olló', 'kő', 'papír']

while True:
    user_input = input("Írd be a fegyvered (kő, papír, olló): ").lower()
    cpu_choice = random.choice(eszközök)
    if user_input == "Kilépés".lower():
        print("Szia, remélem még tudunk majd játszani!")
        break
    
    if user_input not in eszközök:
        print("Kérlet egy eszközt válassz!")
        continue

    match (user_input, cpu_choice):
        case (player, pc) if player == pc:
            print(f"Döntetlen! A gép választása: {cpu_choice}")
        case ('kő', 'papír') | ('olló', 'papír') | ('kő', 'olló'):
            print("Gratulálok, te nyertél! A gép választása:", cpu_choice)
        case _:
            print("Vesztettél!", cpu_choice)    