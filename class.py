class person:
    def __init__(self, name):
        self.name = name


person1 = person("Sara")
person2 = person("Jenny")
person1.name = "Sally"

print(person1.name)
print(person2.name)