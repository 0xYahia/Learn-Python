firstName = "abo bakr"
lastName = "Al-siddiq"
title = "The Caliph of Muslims"
title = "the, caliph, of, muslims"


print(firstName.capitalize())
print(lastName.lower())
print(title.find("Muslims"))
print(title.replace("Muslims", "Islam"))
print(title[4:])

parts = title.split(",")

for part in parts:
    print(part.strip().capitalize())
