import random, time


def fight(enemy_name, enemy_health, health, max_health, max_damage, potions): 
    print("A",enemy_name,"appears!")
    while enemy_health > 0 and health > 0:
        damage=random.randint(1, max_damage)
        enemy_health -= damage
        print("you dealt", damage,"damage")
        print(enemy_name, "health", enemy_health)
        if enemy_health <=0:
            print("you defeated the", enemy_name,"!")
            break
        enemy_damage= random.randint(1, 25)
        health-=enemy_damage
        print("You took",enemy_damage,"damage you now have",health,"health!")
        if health <= 0:
            print("you died!")
            break
        choice=input("press enter to attack or press h to heal")
        if choice.lower() == "h":
            if not potions:
                print("you dont have any potions.")
            else:
                for index,potion in enumerate(potions, 1):
                    print(index,".",potion)
                potion_choice=input("which potion do you choose?: ")
                if potion_choice.isdigit():
                   potion_choice=int(potion_choice)
                   if 1 <= potion_choice <=len(potions):
                       potion=potions[potion_choice - 1]
                       if potion=="healthminor":
                           health += 20
                           health= min(health, max_damage)
                       elif potion =="healthmajor":
                           health+=50
                           health=min(health, max_health)
                       potions.pop(potion_choice -1)
                       print("you used",potion + "!")
                       print("you now have",health,"health!")
                   else:
                        print("you do not have that potion!")
                else:
                    print("that is not a valid choice!")
    return health