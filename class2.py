
class Game:
    variable1 = 'Hello'
    variable2 = 'World!'



class Person:
    def __init__(self,name,age,body_type,location):
        self.name = name
        self.age = age
        self.body_type = body_type
        self.location = location

    def myFunc(self):
        print("My name is: " + self.name)

p1 = Person("Ryan", 28, "Athletic", "Utah")

print(p1.name)
print(p1.age)
print(p1.body_type)
print(p1.location)
print(p1.myFunc())

class Golfer(Person):
    sponser = "Taylormade"
    world_ranking = "1st"


g1 = Golfer("Dustin Johnson",32,"Athetic","Florida")
print(g1.world_ranking)








if __name__ == "__main__":
    x = Game()
    print("{} {}".format(x.variable1, x.variable2))
    
