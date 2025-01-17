# class -> keyword
# convention -> class names are Capitalize

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The cat {self.name} is {self.age} years old"

# Creating objects
cat_object1 = Cat("Rino", 5.5)
print(cat_object1)
print(type(cat_object1))

a_string = str(cat_object1)
print("Converted string:", a_string)

print(cat_object1.age)

cat_object2 = Cat("Pierre", 7.5)
print(cat_object2)
print(cat_object2.name)
print(cat_object2.age)


