#importar as bibliotecas para o processo random e de fila
import random
from collections import deque
#defenir as classes dos items 
money = 10

class item:
    def __init__(self, Name ,price):
        self.Name = Name
        self.price = price

    def display(self):
        print("Name: "+ self.Name)
        print("price to sell: " + str(self.price))
        
class sword(item):
    def __init__(self):
        super().__init__(self)
    
    def display(self):
        print("price to sell: " + str(self.price))        
    
class armingsword(sword):
    def __init__(self):
        super().__init__("arming sword", 3500)
        print(self.Name + str(self.price))
        
    def display(self):
        return super().display()

class dagger(sword): 
    def __init__(self):
        super().__init__("dagger", 2500)
        print(self.Name + str(self.price))
        
    def display(self):
      return super().display()

class  steelsword(sword):
    def __init__(self):
        super().__init__("steel sword" , 5000)
        print(self.Name + str(self.price))

    def display(self):
      return super().display()

       
class Bow(item):
    def __init__(self):
        super().__init__(self)
    
    def display(self):
        print("price to sell: " + str(self.price))    

class  crossbow(Bow):
    def __init__(self):
        super().__init__("crossbow" , 2000)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class  firebow(Bow):
    def __init__(self):
        super().__init__("firebow" , 3050)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class  longbow(Bow):
    def __init__(self):
        super().__init__("longbow" , 3950)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class spear(item):
    def __init__(self):
        super().__init__(self)
    
    def display(self):
        print("price to sell: " + str(self.price)) 

class  icespear(spear):
    def __init__(self):
        super().__init__("ice spear" , 6300)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()


class  firespear(spear):
    def __init__(self):
        super().__init__("fire spear" , 6200)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class powerspear(spear):
    def __init__(self):
        super().__init__("power spear" , 7000)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class Armor(item):
    def __init__(self):
        super().__init__(self)

    def display(self):
        print("price to sell: " + str(self.price)) 

class helm(Armor):
    def __init__(self):
        super().__init__(self)

    def display(self):
        print("price to sell: " + str(self.price)) 

class bronzehelm(Armor):
    def __init__(self):
        super().__init__("bronze helm" , 3000)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class silverhelm(Armor):
    def __init__(self):
        super().__init__("silver helm" , 3500)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class ironhelm(Armor):
    def __init__(self):
        super().__init__("iron helm" , 3300)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class Chestplate(Armor):
    def __init__(self):
        super().__init__(self)

    def display(self):
        print("price to sell: " + str(self.price))

class bronzechestplate(Armor):
    def __init__(self):
        super().__init__("bronze chestplate" , 5000)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class ironchestplate(Armor):
    def __init__(self):
        super().__init__("iron chestplate" , 5100)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class silverchestplate(Armor):
    def __init__(self):
        super().__init__("silver chestplate" , 5500)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class feetarmor(Armor):
    def __init__(self):
        super().__init__(self)

    def display(self):
        print("price to sell: " + str(self.price))

class bronzefeetarmor(Armor):
    def __init__(self):
        super().__init__("bronze feet armor" , 2200)
        print(self.Name + str(self.price))

    def display(self):
        return super().display() 

class ironfeetarmor(Armor):
    def __init__(self):
        super().__init__("iron feet armor" , 2600)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class silverfeetarmor(Armor):
    def __init__(self):
        super().__init__("silver feet armor" , 3000)
        print(self.Name + str(self.price))

    def display(self):
        return super().display() 

class Hammer(item):
    def __init__(self):
        super().__init__(self)  

    def display(self):
        print("price to sell: " + str(self.price)) 

class Bronzehammer(Hammer):
    def __init__(self):
        super().__init__("Bronze hammer" , 4500)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class ironhammer(Hammer):
    def __init__(self):
        super().__init__("iron hammer" , 5500)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

class silverhammer(Hammer):
    def __init__(self):
        super().__init__("silver hammer" , 5900)
        print(self.Name + str(self.price))

    def display(self):
        return super().display()

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

#function for verify money
def verify_money(money):

    if (money==0):
        print("you don't have money")  

    else:
         print("you have: " + money) 

print("Welcome to this game")

#cycle one day
while money<100000 and money>0:
    while (True):
        print("show items to buy")
        print("show items price")

        x=input("")

        if x=="No" or x=="no":
            break
    print("acabou") 

    while (True):
        print("show items to Crafting")
        print(" ")

        x=input("")

        if x=="No" or x=="no":
            break
    print("acabou")   

    while (True):
        print("show items to sell")
        print(" ")

        x=input("")

        if x=="No" or x=="no":
            break
    print("acabou")   


        

               












        








    





        
        
        






