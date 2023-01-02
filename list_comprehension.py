numbers = []

for i in range(10):
    numbers.append(i)
print(numbers)

numbers = [i * 2 for i in range(10)]
print(numbers)

liste = [3, 8, 5, 12, 40]

numbers = [i * 2 for i in liste]

isim = "ferda"
isimler = ["Ferda", "Ali", "Mehmet", "Veli"]
sonuc = [a.upper() for a in isim]
sonuc = [i.lower() for i in isimler]
sonuc = [b.upper() for b in isimler]


print(sonuc)
