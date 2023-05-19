#  08. RO'YXATLAR BILAN ISHLASH. O'ZGARMAS RO'YXATLAR (Tuples)

# RO'YXATNI TARTIBLASH .sort()

# cars = ["bnw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]

# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# SORTER()

# mehmonlar = ["Ahror", "Sardor", "Sarvar", "Bobur", "Qobil"]
# print(sorted(mehmonlar))
# print(sorted(mehmonlar, reverse=True))

# sonlar = [999, 25, -9, 1, 2002, 36]
# print(sorted(sonlar))

# sonlar.sort(reverse=True)
# print(sonlar)

# RO'YXATNI TESKARI AYLANTIRISH. .revarse() metodi

# mehmonlar.reverse()
# print(mehmonlar)

# RO'YXATNING UZUNLIGINI O'LCHASH. len

# print(len(mehmonlar))

# print(len(sonlar))

# range() metodi

# raqamlar = list(range(1,101))
# print(raqamlar)

# toq_sonlar = list(range(1,100,2))
# print(toq_sonlar)

# juft_sonlar = list(range(0,100,2))
# print(juft_sonlar)

# sanash = list(range(0,101,10))
# print(sanash)

#  eng katta qiymatni topish. max

# max_qiymat = max(raqamlar)
# print(max_qiymat)

# MISOL

# narxlar = [22000, 15000, 32500, 1000, 98000]
# qimmat = max(narxlar)
# arzon = min(narxlar)
# jami = sum(narxlar)
# print(f"Eng arzon narx {arzon}, eng qimmat narx {qimmat}, jami: {jami}")

# RO'YXATNI KESISH
# cars = ["bnw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]

# kerarli_qism = cars[1:4]
# print(kerarli_qism)

# RO'YXATDAN NUSXA OLISH

# my_cars = cars[:]

# my_cars.remove("volvo")
# my_cars.insert(2,"gm")
# print(my_cars)
# print(cars)

# O'ZGARMAS RO'YXAT. TUPLE

# toys = ("bus", "car", "bear", "dino", "snake", "lizard")
# print(toys)

# VAZIFA

# BIRINCHI

# davlatlar = ["USA", "Russia", "UK", "Germany", "Spain", "Brasil"]
# print(davlatlar)
# print(len(davlatlar))

# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))

# print(davlatlar)

# davlatlar.reverse()
# print(davlatlar)

# davlatlar.sort()
# print(davlatlar)

# davlatlar.sort(reverse=True)
# print(davlatlar)



# IKKINCHI
# raqamlar = list(range(120, 1201, 2))
# print(raqamlar)

# umumiy = sum(raqamlar)
# print(umumiy)

# eng_katta = max(raqamlar)
# eng_kichik = min(raqamlar)
# print(eng_katta - eng_kichik)

# print(len(raqamlar))

# print(raqamlar[0:21])
# print(raqamlar[250:271])
# print(raqamlar[520:541])


# taomlar = ["Osh", "Norin", "Sho'rva", "Kabob", "Mastava"]

# nonushta = taomlar[:]

# nonushta.remove("Osh")
# nonushta.append("Quymoq")
# nonushta.insert(0, "Non")

# print(nonushta)
# print(taomlar)

# nonushta = tuple(nonushta)

# nonushta[0] = "Non va qaymoq"





























