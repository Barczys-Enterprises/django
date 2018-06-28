age = 48
name = "Chris"

if age >= 40 and age <= 50:
    print("You are in your forty's.")
else:
    print("You are not in your fourty's")


def hello(yourName="DEFAULT", yourAge=0):
    print("Hello {} you are {} years old".format(yourName, yourAge))


hello("Chris", 48)
hello("Ryan", 8)
hello("Gideon", 1)


dogNames = ["Fido", "Fluffy", "Cosmo", "Shithead"]

for dog in dogNames:
    print(dog)

for x in range(1, 11):
    print(x)

y = 1
while y <= age:
    print(y)
    y += 1
