# with open("./dane_do_generatora/imiona.txt", "r",encoding="utf-8") as file:
#     for line in file.readlines():
#         line = line.strip()
#         if line != "":
#             print(line)
# import random
# lista = []
# with open("./dane_do_generatora/nazwiska.txt", "r", encoding="utf-8") as nazwiska:
#     nazwiska2 = open("./dane_do_generatora/nazwiska2.txt", "a+", encoding="utf-8")
#     for line in nazwiska:
#         line = line.strip()
#         if line != "":
#             lista.append(line)
#         else: continue
#     for i in range(1000):
#         print(len(lista))
#         index = random.randint(0, len(lista)-1)
#         print(index, type(index))
#         surname = lista[index]
#         print(surname, type(surname))
#         nazwiska2.write(surname + "\n")
#         lista.remove(surname)

# with open("./dane_do_generatora/nazwiska.txt", "r", encoding="utf-8") as file:
#     nazwiska2 = open("./dane_do_generatora/nazwiska2.txt", "a+", encoding="utf-8")
#     for line in file:
#         line = line.strip()
#         if line.find(" "):
#             print("spacja")
#         else:
#             nazwiska2.write(line + "\n")

            # lista.append(line)
# with open("./dane_do_generatora/nazwiska2.txt", "w", encoding="utf-8") as file:
#     for line in lista:
#         file.write(line + "\n")
# maximum = 0
# with open("./dane_do_generatora/nazwiska.txt", "r", encoding="utf-8") as file:
#     for line in file.readlines():
#         if line.find(" "):
#             if line.find(" ") > maximum:
#                 maximum = line.find(" ")
#                 print(maximum)
# print("stop")
# print(maximum)

# file = open("./dane_do_generatora/imiona2.txt", "r", encoding="utf-8")
# file2 = open("./dane_do_generatora/imiona.txt", "a+", encoding="utf-8")
#
# for line in file.readlines():
#     line = line.strip()
#     if line != "" or line is not None or line != "\n":
#         file2.write(line+"\n")
#
# file.close()
# file2.close()
names = []
file = open("./dane_do_generatora/telefony.txt", "r", encoding="utf-8")
for line in file.readlines():
    line = line.strip()
    if line not in names:
        names.append(line)
file.close()
file2 = open("./dane_do_generatora/telefony.txt", "w", encoding="utf-8")
for name in names:
    file2.write(name+"\n")
file2.close()