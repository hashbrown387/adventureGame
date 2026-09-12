import random
import time
from combat import fight
buffs = []
potions = []
max_damage=40




print("THE FORGOTTEN CASTLE")
print()

health=100
max_health=100
print("you have", health, "health.")
print("you stand in the ancient gates of a long lost castle")
print("there are 2 paths ahead of you")
print()
print("1. enter the castle")
print("2. enter the forest next to the castle")

choice = input("where do you head?")

if choice == "1":
    health -= 20
    print("A trap hits you!")
    print("you now have", health, "health")

    if health <= 0:
        print("You have no health left!")
        print("game over!")
    else:
        print("You survived the trap!")
    print("you see 2 doors one metal one wood")
    print("1. open the wooden door")
    print("2. open the metal one")
    door=input("which door do you choose?")

    if door == "1":
        print("you found a treasure room that is guarded by a dragon!")
        choice=input("do you fight yes or no?: ")
        if choice=="no":
            print("you got skewered")
        elif choice=="yes":
            fight("dragon", 125,health,max_health,max_damage,potions)
            health = 200
            max_health = 200
            print("you have found a health crystal and use it increasing your health and maxhealth to",max_health,"!")
    elif door == "2":
        fight_choice=input("do you fight yes or no: ")
        if fight_choice=="no":
           print("you got murdered")
        elif fight_choice == "yes":
            fight("goblin",50,health,max_health,max_damage,potions)
        else:
            print("you got murdered")
        time.sleep(1)
        potions.append("healthminor")
        print("after defeating the goblin it drops a minor health potion and you realize you are in a doungeon with 2 chests their is a old one and a odd looking one.")
        print("1.odd looking one")
        print("2.old one")
        choice=input(int("which one do you pick?: "))
        if choice == 1:
            max_damage += 25
            potions.append("healthmajor")
            buffs.append("electro_whip")
            print("you have found the legendary electro whip granting you +25 extra damage and a major health potion!")
        elif choice == 2:
            max_health += 20
            health=max_health
            print("you found a minor health crystal increasing your health/maxhealth to",max_health,"!")

elif choice == "2":
    print("you enter into the forest and get lost.")
else:
    print("you died by freezing because you could not make your mind up")