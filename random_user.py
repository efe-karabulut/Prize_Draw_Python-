import random

random_gift = ["Araba", "Telefon", "Bilgisayar", "Tablet", "Kulaklık", "PlayStation 5"]


# Her kullanıcı için rastgele ve benzersiz bir ID üret
def create_user(name):
    return {"id": random.randint(10, 1000), "name": name}


# Kullanıcıları oluştur
db = [
    create_user("Irmak"),
    create_user("Ahmet"),
    create_user("Hasan"),
    create_user("Ayşe"),
    create_user("Öykü"),
]

userWin = []

# 3 farklı kullanıcı seç
while len(userWin) < 3:
    chosen_user = random.choice(db)
    if chosen_user not in userWin:
        userWin.append(chosen_user)


# Kazananları ve hediyeleri eşleştir
def winners():
    for winner in userWin:
        prize = random.choice(random_gift)
        print("Winner:", winner["name"], "Prize:", prize)


# Çekilişi başlat
def startRaffle():
    winners()


startRaffle()
