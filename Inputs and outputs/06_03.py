stringFile = open("strings.txt")
outputFile = open("string_output.txt", "w")

result = ""
# for line in stringFile:
#     if line.strip() == "I":
#         result += " " + line.strip()
#     elif line.strip() == "Almdrasa":
#         result += " " + line.strip()
#     else:
#         result += " " + line.strip().lower()

for index, line in enumerate(stringFile):
    if index == 0:
        result += " " + line.strip()
    elif index == 2:
        result += " " + line.strip()
    else:
        result += " " + line.strip().lower()


print(result, file=outputFile)
outputFile.close()
print("I am done")
