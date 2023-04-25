fruits = ["apples", "bananas", "grapes", "mangos", "nectrines", "pears"]

# for fruit in fruits:
#     print("My favorite fruit is", fruit)

index = 0
# while index <= 3:
#     print(fruits[index])
#     index += 1

# while fruits[index] != "nectrines":
#     print(fruits[index])
#     index += 1

for fruit in fruits:
    if fruits[index] != "nectrines":
        print(fruit)
        index += 1

for fruit in fruits:
    if fruit == "nectrines":
        break
    print(fruit)
    index += 1
