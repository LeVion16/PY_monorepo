import os
os.system("cls")

sorok = 0
személy = 0
#keresés = input("mit keresünk?")
keresés2 = False

# 1. feladat
with open("titanic.txt", "r+") as file:
    for line in file:
        sorok += 1
        
        személy += int(line.split(";")[1]) + int(line.split(";")[2])

        """if line.split(";")[0].split("-") == keresés:
            keresés2 = True
            print(line.split(";"))
        else:
           keresés2 = False"""

        if int(line.split(";")[2]) % int(line.split(";")[1]) >= 60:
            print(line)


print("2. feladat:")
print("Az osztályok száma:", sorok)

print("3. feladat:")
print("A személyek száma a titacikon:" , személy)


"""print("4.feladat")
if keresés2 == True:
    print ("van találat!")
elif keresés2 == False:
    print ("nincs találat!")"""