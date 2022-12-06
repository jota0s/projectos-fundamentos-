class item:
    def __init__(self, Name ,price):
        self.Name = Name
        self.price = price

    def display(self):
        print("Name: "+ self.Name)
        print("price to sell: " + str(self.price))

Greatsword = item("Greatsword" , 6500 )
Greatsword.display()

item2= item("arming sword" , 3500)
item2.display()

item3 = item("dagger" , 2500)
item3.display()

print("")
print("")




    
 
###############################################################################################defenir as classes para materiais########################################################################################
class materials:
    def __init__(self, Name ,price):
        self.Name = Name
        self.price = price

    def display(self):
        print("Name: "+ self.Name)
        print("price to sell: " + str(self.price))


class wood(materials):
    def __init__(self):
        super().__init__("wood" , 500)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class iron(materials):
    def __init__(self):
        super().__init__("wood" , 1000)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()


class silver(materials):
    def __init__(self):
        super().__init__("wood" , 1200)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class leather(materials):
    def __init__(self):
        super().__init__("leather" , 250)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class gold(materials):
    def __init__(self):
        super().__init__("gold" , 1500)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class fireinabottle(materials):
    def __init__(self):
        super().__init__("fire in a bottle" , 750)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class iceinabottle(materials):
    def __init__(self):
        super().__init__("ice in a bottle" , 750)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class electricityinabottle(materials):
    def __init__(self):
        super().__init__("electricity in a bottle" , 750)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class recipe:
    def __init__(self, Name ,materialstomake):
        self.Name = Name
        self.materialstomake = materialstomake

    def display(self):
        print("Name: "+ self.Name)
        print("materials to make: " + str(self.materialstomake))

class sword_R(recipe):
    def __init__(self):
        super().__init__(self)

    def display(self):
        print("materials to make : " + str(self.materialstomake))

class  armingsword(sword_R):
    def __init__(self):
        super().__init__("arming sword recipe" , materials.iron + materials.wood)
        print(self.Name + str(self.materialstomake))

    def display(self):
        return super().display()

class  silversword(sword_R):
    def __init__(self):
        super().__init__("silver sword recipe" , materials.silver + materials.wood)
        print(self.Name + str(self.materialstomake))

    def display(self):
        return super().display()

class  dagger(sword_R):
    def __init__(self):
        super().__init__("dagger recipe" , materials.iron + materials.wood)
        print(self.Name + str(self.materialstomake))

    def display(self):
        return super().display()