class Screwdriver:
    def __init__(self, color, len, type, doesRotate, doesTest):
        self.color = color
        self.len = len
        self.type = type
        self.doesRotate = doesRotate
        self.doesTest = doesTest

    def rotates(self):
        result = f"I am a {self.len} cm {self.color} {self.type} scredriver"
        if self.doesRotate:
            print(result + "and I rotate")
        else:
            print(result + "and I don't rotate")

    def testsElectricity(self):
        result = f"I am a {self.len} cm {self.color} {self.type} scredriver"
        if self.doesTest:
            print(result + "and I test electricity")
        else:
            print(result + "and I don't test electricity")


list1 = ["ali", "ahmed", "mohamed"]
list1.append("alaa")
print(list1)

name = "Ahmed Fathy"
print(name[:5])

name = "Ahmed Fathy"
print(name[:])

name = "Ahmed Fathy"
print(name[6:])

name = "Ali" * 2 * 3
print(name)

# num = [10, 20, 30, 40, 50]
# num.remove(60)
# print(num)

num = [10, 20, 30, 40, 50]
num.remove(30)
print(num)
