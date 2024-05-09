# import threading

# print(threading.active_count())
# print(threading.enumerate())

# if __name__ == "__main__":
#     t1 = threading.Thread(target=, args=(15,))
#     t2 = threading.Thread(target=, args=(15,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("Done!")


# nazwiska.txt looks sth like this:
'''
surname
surname     many spaces     name
surname
'''

valid_surnames = []
names = []
file = open("./dane_do_generatora/nazwiska.txt", "r", encoding="utf-8")
surnames = file.readlines()
for surname in surnames:
    try:
        if surname[70] == " ": # 70th index is definitely a white space between surname and name
            last = surname[:20] # the longest surname ends at 17th or 18th index
            first = surname[250:] # names start at 256th or 255th index
            last = last.rstrip()
            first = first.lstrip()
            if last not in valid_surnames:
                valid_surnames.append(last)
            if first not in names:
                names.append(first)
    except Exception as e:
        if surname not in valid_surnames:
            valid_surnames.append(surname)
file.close()
file = open("./dane_do_generatora/nazwiska2.txt", "w", encoding="utf-8")
for surname in valid_surnames:
    file.write(surname+"\n")
file.close()
file = open("./dane_do_generatora/imiona2.txt", "a+", encoding="utf-8")
for name in names:
    file.write(name+"\n")
file.close()