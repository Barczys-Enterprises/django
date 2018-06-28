class Dog:
    def __init__(self, name="DEFAULT", age=999, furcolor="DEFAULT"):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self):
        print("BARK!")


myDog = Dog("Fido", 12, "Black")
myDog.bark()
print(myDog.age)
