##################################################################################importar as bibliotecas para o processo random e de fila#########################################################################################################
import random
from collections import deque
from lista_classes import *


#########################################################################################definir variaveis e dicionarios###########################################################################################################################
money=10
gamecycle=True
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

while material_inventory["wood"] <500:
    material_inventory["wood"] += 1
    print(material_inventory)

while material_inventory["iron"] <500:
    material_inventory["iron"] += 1
    print(material_inventory)

while material_inventory["silver"] <500:
    material_inventory["silver"] += 1
    print(material_inventory)

while material_inventory["leather"] <500:
    material_inventory["leather"] += 1
    print(material_inventory)

while material_inventory["gold"] <500:
    material_inventory["gold"] += 1
    print(material_inventory)

while material_inventory["ice in a bottle"] <500:
    material_inventory["ice in a bottle"] += 1
    print(material_inventory)

while material_inventory["electricity in a bottle"] <500:
    material_inventory["electricity in a bottle"] += 1
    print(material_inventory)

################################################################################################function for verify money#########################################################################################################################
def verify_money(money):

    if (money==0):
        print("you don't have money")  

    else:
         print("you have: " + money) 

print("Welcome to this game")

#cycle one day
while gamecycle == True:
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


        

               












        








    





        
        
        






