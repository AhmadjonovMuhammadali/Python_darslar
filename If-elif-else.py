#11 If-elif-else

# yosh = int(input("Yoshingiz nechada?>>> "))

# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5000so'm")
# elif yosh<=18:
#     print("Sizga kirish 8000so'm")
# else:
#     print("Sizga kirish 10000so'm")



# Or operatori

# kun = input("Bugun nima kun?>>> ")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")



# And operatori

# kun = input("Bugun nima kun?>>> ")
# harorat = float(input("Havo harorati qanday?>>> "))

# if kun.lower() == "yakshanba" and harorat >= 30:
#     print("Cho'milgani ketdik.")
# elif kun.lower() == "yakshanba" and harorat < 30:
#     print("Uyda dam olamiz.")
# else:
#     print("Bugun dam olish kuni emas.")



# Or va And operatorlari

# kun = input("Bugun nima kun?>>> ")
# harorat = float(input("Havo harorati qanday?>>> "))
    
# if (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat >= 30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat < 30:
#     print("Uyda dam olamiz!")
# else:
#     print("Bugun dam olish kuni emas!")


# True-False

# narh = 15000
# choy = False
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000

# print(f"Jami: {narh} so'm")



# Har bir shartni alohida tekshiradi va bir biriga bog'liq emas

# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000

# if salat:
#     print("Mijoz salat sotib oldi.")
#     narh = narh + 5000

# if non:
#     print("Mijoz non sotib oldi.")
#     narh = narh + 2000

# if kompot:
#     print("Mijoz kompot sotib oldi.")
#     narh = narh + 5000

# if assorti:
#     print("Mijoz assorti sotib oldi.")
#     narh = narh + 15000

# print(f"Jami: {narh} so'm")



# in operatori

# menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# ovqat = input("Nima ovqat yeysiz?>>> ")

# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")



# menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor.")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q.")