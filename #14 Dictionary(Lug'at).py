#14 Lug'at (Dictionary)

# car_0 = {"model" : "ferrari", "rang" : "qizil"}
# print(car_0["model"])
# print(car_0["rang"])



# eng_uz = {"apple" : "olma", "apricot" : "o'rik", "banana" : "banan"}
# print(eng_uz["apricot"])



# mevalar = {"olma":10000, "tarvuz":8000, "qovun":10000}
# print(f"Olmaning narxi {mevalar['olma']} so'm")



# talaba_0 = {"ism":"murod olimov", "t_yil":2002, "yosh":21}
# print(f"Talaba, {talaba_0['ism'].title()} {talaba_0['t_yil']}-yilda tug'ilgan, u hozir {talaba_0['yosh']} yoshda.")



# # Lug'atga yangi kalit so'z qo'shish va o'zgartirish

# talaba_0["kurs"] = 3
# talaba_0["fakultet"] = "Informatika"
# talaba_0["ism"] = "ahmadjonov muhammadali"

# print(talaba_0)



# # Bo'sh lug'at

# talaba_1 = {}
# print(talaba_1)
# talaba_1["ism"] = "behzod"
# talaba_1["kurs"] = 4
# talaba_1["fakultet"] = "matematika"
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['fakultet']} fakultetida o'qiydi, u {talaba_1['kurs']}-kurs.")



# Lug'atdan qiymatni o'chirish
# talaba_2 = {"ism":"murod olimov", "t_yil":2002, "yosh":21}
# del talaba_2["yosh"]
# print(talaba_2)



# Lug'atlarni bir necha qatorga yozish
telefonlar = {
    'bobur':'iphone x',
    'salim':'galaxy 9',
    'olim':'redmi 10c',
    'qobil':'nokia 3310'
    }

print(telefonlar['bobur'])
phone = telefonlar.get('hasan', 'mavjud emas')
print(phone)




























