import pyodbc
from Fireman import Fireman
# PESEL, imie*, nazwisko*, data_ur*, stopien*, stanowisko - nie, adres_zamieszkania - nie, nr_tel*, email, data zatrudnienia, id_dyzur*
# najpierw losowo wybierane są imiona, nazwiska i nr_tel z plików tekstowych
# data ur:
''' rok: > 1965 i < 2003
    miesiąc: >= 1  i <= 12
    dzień: zależy od miesiąca
    dla mies = {1, 3, 5, 7, 8, 10, 12}: >= 1 <= 31
    dla mies = {4, 6, 9, 11}: >= 1 <= 30
    dla mies = 2: >= 1 i <= 28'''
# stopien wartosci: strażak, starszy strażak, sekcyjny, starszy sekcyjny, ogniomistrz, starszy ogniomistrz, młodszy aspirant, aspirant, starszy aspirant, aspirant sztabowy, młodszy kapitan, kapitan, starszy kapitan, młodszy brygadier, brygadier, starszy brygadier, nadbrygadier, generał brygady, niestrażak
# email: imie.nazwisko@nazwaRemizy.pl
# data zatrudnienia: +19 lat od daty urodzenia, mies i dzień inne
# id_dyzur: losowy numer >= 2 i <= 7

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=yourdatabase.accdb;'
    conn = pyodbc.connect(con_string)
 
    cursor = conn.cursor()
 
    myuser = (
 
        (6, 'data', 'data@gmail.com'),
        (7, 'python', 'python@gnail.com'),
        (8, 'java', 'java@gmail.com'),
 
    )
    # lista = []
    # for i in range(1):
    #     fireman = Fireman()
    #     lista.extend(
    #         (
    #             fireman.PESEL,
    #             fireman.name,
    #             fireman.surname,
    #             fireman.dateOfBirth,
    #             fireman.rank,
    #             fireman.phoneNumber,
    #             fireman.email,
    #             fireman.hireDate,
    #             fireman.id_dyzur
    #         )
    #     )
    fireman = Fireman()
    # fireman1 = Fireman()
    man = (
            fireman.PESEL,
            fireman.name,
            fireman.surname,
            fireman.dateOfBirth,
            fireman.rank,
            fireman.phoneNumber,
            fireman.email,
            fireman.hireDate,
            fireman.id_dyzur
        )
    #     (
    #         fireman1.PESEL,
    #         fireman1.name,
    #         fireman1.surname,
    #         fireman1.dateOfBirth,
    #         fireman1.rank,
    #         fireman1.phoneNumber,
    #         fireman1.email,
    #         fireman1.hireDate,
    #         fireman1.id_dyzur
    #     )
    # )
 
    cursor.execute(f'INSERT INTO Personel (pesel, imie, nazwisko, data_ur, stopien, nr_tel, email, data_zatrudnienia, id_dyzur) VALUES (?,?,?,?,?,?,?,?,?)', man)
    conn.commit()
    cursor.execute("SELECT * FROM Personel")
    data = cursor.fetchall()
    print(data)
 
# stmt.execute("INSERT INTO ... (?,?,?,?,?)", p1, p2, p3, p4, p5)
except pyodbc.Error as e:
    print("Error in connection", e)
