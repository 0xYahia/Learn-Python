valuesFile = open("values.txt", "rt")
outputFile = open("output.txt", "wt")

print("Start reading from file")

sum = 0

for line in valuesFile:
    sum += int(line)
    print(line.rstrip(), file=outputFile)

print("Sum: " + str(sum), file=outputFile)
outputFile.close()
print("I am done")
