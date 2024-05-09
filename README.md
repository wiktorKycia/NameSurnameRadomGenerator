# Random Person data generator
This is more of a help project, that is meant to help me generate the data to my Access database
It generates random names, surnames, phone numbers from text files
And also other stuff via random module built in python

### Main problem
- The biggest problem I had was, that the files from which I randomized
the names, surnames and phones, contained hundreds of thousands lines.
- Another thing was that in the file with surnames some rows contained
not only surnames, but also many spaces (around 200) and a name afterwards.
- So the structure of this file looked a little bit like this:
```
surname
surname                              name
surname                              name
surname
surname                              name
```
#### Solution
So basically what this code does is:
- first it creates lists for surnames and names and connects to a file
- iterates for every line in the file
- if it does not contains any weird spaces, it then appends it to the surnames list on condition that there is no such surname already there
- if it does have those weird spaces, then it looks for the first index of a white space, removes all the spaces from the string, then name has all characters from that index to the end, and the surname - all the characters from the beginning to the index-1
- then it appends name and surname to the corresponding lists
```python
valid_surnames = []
names = []
file = open("./dane_do_generatora/nazwiska.txt", "r", encoding="utf-8")
surnames = file.readlines()
for surname in surnames:
    if not " " in surname:
        if not surname in valid_surnames:
            valid_surnames.append(surname)
    else:
        index = surname.find(" ")
        surname = surname.replace(" ", "")
        name = surname[index:]
        surname = surname[:index-1]
        names.append(name)
        valid_surnames.append(surname)
file.close()
```
I was about to try this code, then I realised it would take too much time to execute it
I calculated, that this code has a complexity of n^3
```python
for surname in surnames: # n
    if not " " in surname: # * n
        if not surname in valid_surnames: # * n
```
Since every iteration or even 'in' keyword nested in each other multiplies the time complexity by n

Hence I looked into the data and analyzed it more
and I invented this:
```python
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
```
before writing this, I ran the previous code, but at the end calculated the max length of a surname from the list and it was 17 characters long
When I looked into those weird rows, I saw that the names were starting somewhere about 255th character of a line

Instead of iterating for every line in the list of lines just to find the space
I just used 'try ... except' block to force the check if the string has a high index (for example 70), therefore if it has those weird spaces
'except' in this example is used as some kind of 'else' statement for 'try', due to the fact, in 'except', we are certain, that the line has only the surname and nothing more, so we can add it to the list if the list does not contain it
However, when the line has this index of 70, the program slices the string into the two variables:
- last: for lastname; it takes characters from the beginning to the 20th index, why not 17th? As I wasn't sure whether it will cut the last letter or leave the space at the end, so it was safer to just strip it afterwards
- first: for firstname; it takes characters from the 250th to the end, why? the same as with lastname, but with space at the beginning not the end

at the end, it appends last, and first variables to the corresponding lists on condition, that there aren't any identical strings
