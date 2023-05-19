#07 LISTS(RO'YXATLAR)
# mevalar = ["Olma", "Behi", "Nok", "Anor"]
# narxlar = [18000, 12000, 25000, 10900, 80000]
# sonlar = ["bir", "ikki", 3, 4, 5, 6]
# ismlar = []
# mevalar[1] = "Gilos"
# cars = ["Tiko", "Damas", "Nexia", "Spark", "Cobalt"]


# .Append() metodi - ro'yxat oxiriga element qo'shadi

# mevalar.append("O'rik")
# mevalar.append("Qovun")
# print(mevalar)

# .Insert() metodi qaysi qatorga qo'shilishi aytiladi

# mevalar.insert(2, "Banan")
# mevalar.insert(1, "Ananas")
# mevalar.insert(4, "Tarvuz")
# print(mevalar)

# del metodi - Ko'rsatilgan elementni o'chiradi
# del mevalar[2]
# print(mevalar)

# del cars[0]
# print(cars)

#  .remove() metodi

# cars.remove("Nexia")
# print(cars)
# cars.append("Nexia 3")
# cars.insert(3, "Tiko")
# print(cars)

# cars.remove("Cobalt")
# print(cars)

#  pop() metodi
# bozorlik = ["Yog'", "Un", "Piyoz", "Go'sht", "Banan"]
# print(bozorlik)

# mahsulot = bozorlik.pop(3)
# print(mahsulot)

# print("Men ", mahsulot.lower(), "sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# VAZIFA

#  №1
# ismlar = ["Ahror", "Sardor", "Sarvar"]

# print("Salom ", ismlar[0], ", bugun choyxonaga  borasanmi?")
# print(ismlar[1], "choyxonaga boramizmi?")

#  №2
# sonlar = [2002, -8, 3.14, 99, 5, 21]
# print(sonlar[0] + sonlar[5])

# del sonlar[1]
# print(sonlar)

# sonlar.append(2023)
# sonlar.insert(0, 1)
# print(sonlar)

# sonlar[2] = 777
# print(sonlar)

# t_yil = sonlar.pop(1)
# print(t_yil)

# sonlar.remove(2023)
# print(sonlar)

# #  №3
# t_shaxslar = ["Amir Temur", "Navoiy", "Bobur", "Buxoriy"]
# z_shaxslar = ["Khabib", "Ronaldu", "Bill Gates"]

# t_shaxs = t_shaxslar.pop(1)
# z_shaxs = z_shaxslar.pop(0)

# print(f"Men tarixiy shaxslardan {t_shaxs} bilan, zamonaviy shaxslardan esa {z_shaxs} bilan suxbat qilishni istar edim.")

# №4 
friends = []

friends.append("Sardor")
friends.append("Bobur")
friends.append("Jobir")
friends.append("Ahror")
friends.append("Islom")
friends.append("Sarvar")
friends.append("Qosim")

friends.remove("Qosim")
friends.remove("Islom")

friends.append("Bahrom")
friends.insert(0, "Iskandar")
friends.insert(3, "Asadbek")


mehmonlar = [friends.pop(1), friends.pop(0), friends.pop(3)]
mehmonlar.append(friends.pop(4))

print("Kelgan mehmonlar: ", mehmonlar)



















