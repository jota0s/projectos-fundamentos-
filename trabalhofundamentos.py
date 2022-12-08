import random
from collections import deque


#########################################################################################definir variaveis e dicionarios e classes###########################################################################################################################
money=100000
gamecycle=True
day=0
material_inventory =  {
    "wood" : 0,
    "iron" : 0,
    "silver" : 0,
    "leather" : 0,
    "gold" : 0,
    "fire in a bottle" : 0,
    "ice in a bottle" : 0,
    "electricity in a bottle" : 0
}

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
        super().__init__("armingsword", 3500)
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
        super().__init__("steelsword" , 5000)
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
        super().__init__("icespear" , 6300)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()


class  firespear(spear):
    def __init__(self):
        super().__init__("firespear" , 6200)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class powerspear(spear):
    def __init__(self):
        super().__init__("powerspear" , 7000)
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
        super().__init__("bronzehelm" , 3000)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class silverhelm(Armor):
    def __init__(self):
        super().__init__("silverhelm" , 3500)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class ironhelm(Armor):
    def __init__(self):
        super().__init__("ironhelm" , 3300)
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
        super().__init__("bronzechestplate" , 5000)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class ironchestplate(Armor):
    def __init__(self):
        super().__init__("ironchestplate" , 5100)
        print(self.Name + str(self.price))
    
    def display(self):
      return super().display()

class silverchestplate(Armor):
    def __init__(self):
        super().__init__("silverchestplate" , 5500)
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
        super().__init__("bronzefeetarmor" , 2200)
        print(self.Name + str(self.price))

    def display(self):
        print("price to sell: " + str(self.price)) 

class ironfeetarmor(Armor):
    def __init__(self):
        super().__init__("ironfeetarmor" , 2600)
        print(self.Name + str(self.price))

    def display(self):
        print("price to sell: " + str(self.price)) 

class silverfeetarmor(Armor):
    def __init__(self):
        super().__init__("silverfeetarmor" , 3000)
        print(self.Name + str(self.price))

    def display(self):
        print("price to sell: " + str(self.price)) 

class Hammer(item):
    def __init__(self):
        super().__init__(self)  

    def display(self):
        print("price to sell: " + str(self.price)) 

class Bronzehammer(Hammer):
    def __init__(self):
        super().__init__("Bronzehammer" , 4500)
        print(self.Name + str(self.price))

    def display(self):
        print("price to sell: " + str(self.price)) 

class ironhammer(Hammer):
    def __init__(self):
        super().__init__("ironhammer" , 5500)
        print(self.Name + str(self.price))

    def display(self):
        print("price to sell: " + str(self.price)) 

class silverhammer(Hammer):
    def __init__(self):
        super().__init__("silverhammer" , 5900)
        print(self.Name + str(self.price))

    def display(self):
        print("price to sell: " + str(self.price))

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

class add_items_to_inventory():
    
    def itemdder(self, items):
        pass

################################################################################################function for verify money#####################################################################   

def verify_money(money):
    if money==0:
        print("you don't have money")  
    else:
        print("you have: " + str(money)) 


print("The sun rises is a new day")

#day cycle  
while gamecycle:
    print("would you like to check your money today?")
    x=input("(No or yes):")
    if x.lower()=="yes":
        print("you have: " + str(money))
    print("welcome to the resource shop do u want to buy something?")
    x=input("(No or yes):")
    y=input("(write the name of the material you want to buy \n wood \n iron \n silver \n leather \n gold \n fire in a bottle \n ice in abottle \n electricity in a bottle  )")
    G=input("")

    if x.lower() =="yes":
            if y.lower() =="wood":
                print("the wood costs 500 money are you sure want to buy?")
            if y.lower() =="iron":
                print("the iron costs 1000 money are do you want to buy?")
            if y.lower() =="silver":
                print("the silver costs 1200 money are you sure want to buy?")
            if y.lower() =="gold":
                print("the gold costs 1500 money are you sure want to buy?")
            if y.lower() =="leather":
                print("the leather costs 250 money are you sure want to buy?")
            if y.lower() =="fire in a bottle":
                print("the fire in a bottle costs 7500 money are you sure want to buy?")
            if y.lower() =="ice in a bottle":
                print("the ice in a bottle costs 7500 money are you sure want to buy?")
            if y.lower() =="electricity in a bottle":
                print("the electricity in a bottle costs 7500 money are you sure want to buy?")
    elif x.lower() == "no":
            print("you left the shop")
    print("you return to your crafting shop")
    print("there are many items i want to craft which onde should i choose?")
    if G.lower()== "armingsword":
        print()

    
        

      
    
        
 
            
           
    
    


        
    if money >= 100000:
        gamecycle=False
    else:
        day += 1

