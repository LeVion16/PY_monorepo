# 1. Fájl megnyitása olvasásra ('r' = read)
file = open("adat.txt", 'r', encoding='utf-8')


# 2. Tartalom beolvasása
content = file.read()

#Kiíratás
print(content)

# 4. Fájl bezárása
file.close()