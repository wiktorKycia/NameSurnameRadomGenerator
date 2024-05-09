import random
import os

class Fireman:
    names = []
    surnames = []
    ranks = [
        "strażak", "starszy strażak", "sekcyjny", "starszy sekcyjny", "ogniomistrz", "starszy ogniomistrz", "młodszy aspirant", "aspirant", "starszy aspirant", "aspirant sztabowy", "młodszy kapitan", "kapitan", "starszy kapitan", "młodszy brygadier", "brygadier", "starszy brygadier", "nadbrygadier", "generał brygady", "niestrażak"
    ]
    phones = []
    
    def __init__(self) -> None:
        self.name = self.getRandomName()
        print("surname")
        self.surname = self.getRandomSurname()
        print("rank")
        self.rank = self.getRandomRank()
        print("date of birth")
        self.dateOfBirth = self.getDateOfBirth()
        print("phone")
        self.phoneNumber = self.getPhone()
        print("id_dyzur")
        self.id_dyzur = self.get_id_dyzur()
        print("hire date")
        self.hireDate = self.getHireDate()
        print("PESEL")
        self.PESEL = self.getPESEL()
        print("email")
        self.email = self.getEmail()

    @staticmethod
    def getRandomName() -> str:
        print("get random name starts")
        i = 0
        with open("./dane_do_generatora/imiona.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                i += 1
                line = line.strip()
                if line != "":
                    Fireman.names.append(line)
                else: continue
        print("lista wypełniona", i)
        index = random.randint(1, len(Fireman.names))
        name = Fireman.names[index]
        Fireman.names.remove(name)
        print("imie wybrane")
        with open("./dane_do_generatora/imiona.txt", "w", encoding="utf-8") as file:
            for imie in Fireman.names:
                file.write(imie + "\n")
        Fireman.names = []
        print("koniec")
        return name

    @staticmethod
    def getRandomSurname() -> str:
        i=0
        with open("./dane_do_generatora/nazwiska.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                i+=1
                line = line.strip()
                if line != "":
                    Fireman.surnames.append(line)
                else: continue
        print(i)
        index = random.randint(1, len(Fireman.surnames))
        surname = Fireman.surnames[index]
        Fireman.surnames.remove(surname)
        with open("./dane_do_generatora/nazwiska.txt", "w", encoding="utf-8") as file:
            for nazwisko in Fireman.surnames:
                file.write(nazwisko + "\n")
        return surname
    
    @staticmethod
    def getDateOfBirth() -> str:
        year = random.randint(1965, 2003)
        month = random.randint(1, 12)
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 28)
        return f"{day:02}.{month:02}.{year}"

    @staticmethod
    def getRandomRank() -> str:
        return random.choice(Fireman.ranks)
    
    def getPhone(self) -> str:
        i = 0
        with open("./dane_do_generatora/telefony.txt", "r",encoding="utf-8") as file:
            for line in file.readlines():
                i+=1
                line = line.strip()
                if line != "":
                    Fireman.phones.append(line)
                else: continue
        print(i)
        index = random.randint(1, len(Fireman.phones))
        phone = Fireman.phones[index]
        Fireman.phones.remove(phone)
        with open("./dane_do_generatora/telefony.txt", "w", encoding="utf-8") as file:
            for telefon in Fireman.phones:
                file.write(telefon + "\n")
        return phone

    def getHireDate(self) -> str:
        year = random.randint(int(self.dateOfBirth[-4:])+19, 2024)
        month = random.randint(1, 12)
        if year == 2024 and month > 5:
            month = random.randint(1, 5)
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 28)
        return f"{day:02}.{month:02}.{year}"

    @staticmethod
    def get_id_dyzur() -> int: 
        return random.randint(2, 7)
    
    def getPESEL(self):
        PESEL = ""
        print(self.dateOfBirth)
        print(self.dateOfBirth[-4:])
        year = int(self.dateOfBirth[-4:])
        print(year)

        PESEL += str(self.dateOfBirth[-2:])
        print(PESEL)
        if year < 2000:
            PESEL += str(self.dateOfBirth[3:5])
        else: 
            PESEL += str(int(self.dateOfBirth[3:5]) + 20)
        print(PESEL)
        PESEL += str(self.dateOfBirth[:2])
        print(PESEL)
        PESEL += str(random.randint(0, 9))
        PESEL += str(random.randint(0, 9))
        PESEL += str(random.randint(0, 9))
        print(PESEL)
        if self.name.endswith("a"):
            PESEL += str(random.choice([0, 2, 4, 6, 8]))
        else:
            PESEL += str(random.choice([1, 3, 5, 7, 9]))
        print(PESEL)
        control = 0
        control += int(PESEL[0]) * 1
        control += int(PESEL[1]) * 3
        control += int(PESEL[2]) * 7
        control += int(PESEL[3]) * 9
        control += int(PESEL[4]) * 1
        control += int(PESEL[5]) * 3
        control += int(PESEL[6]) * 7
        control += int(PESEL[7]) * 9
        control += int(PESEL[8]) * 1
        control += int(PESEL[9]) * 3
        control = control % 10
        PESEL += str(10 - control)
        return PESEL
    
    def getEmail(self):
        return f"{self.name}.{self.surname}@gmail.com"
        