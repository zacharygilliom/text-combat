import random
from time import sleep

# class Weapon:

#     def __init__(self, att_modifier, def_modifier, weap_type):
#         self.weap_type = weap_type
#         self.att_modifier = att_modifier
#         self.def_modifier = def_modifier


class Monster:
    
    def __init__(self, kind, health, loot):
        self.kind = kind
        self.health = health
        self.loot = loot
    
    def add_loot(self, item):
        self.loot.append(item)


class Character:
    
    def __init__(self, name, race, profession, gender, health, equipped=None):
        self.name = name
        self.race = race
        self.profession = profession
        self.gender = gender
        self.items = []
        self.health = health
        self.equipped = equipped

    def add_inventory(self, item):
        self.items.append(item)

    def subtract_inventory(self, item):
        self.items.remove(item)

    def equip_item(self, item):
        self.equipped = item


def choose_move():
    move = input("Please choose one of the following moves:\n\n 1. Quick Attack. \n 2. Power Attack.\n 3. Heal.\n*************************************\n")
    return move


def quick_attack(attack_player, defense_player_health):
    damage = random.randint(15, 22)
    defense_player_health -= damage
    print(attack_player + " has dealt " + str(damage) + " damage.")
    return defense_player_health


def power_attack(attack_player, defense_player_health):
    damage = random.choice(['miss', 'miss', 'miss', 'miss', random.randint(25, 35), random.randint(25, 35),
                            random.randint(25, 35), random.randint(25, 35), random.randint(25, 35),
                            random.randint(25, 35)])
    if damage == 'miss':
        print(attack_player + " has missed their power attack!")
    else:
        defense_player_health -= damage
        print(attack_player + " has dealt " + str(damage) + " damage.")
    return defense_player_health


def heal(attack_player, attack_player_health):
    heal_amount = random.randint(17, 24)
    attack_player_health += heal_amount
    print(attack_player + " has healed for " + str(heal_amount) + " points")
    return attack_player_health


def check_health(player_health):
    if player_health <= 0:
        return True
    if player_health > 0:
        return False

def loot_monster(slain):
    if slain.health <= 0:
        print("The Monster has been defeated!\nCollect your loot hero!")
        print("The Monster has dropped a " + str(slain.loot) + "\nClaim your prize victor!")

    else:
        print(user.name + " has died\nThe battle is now over")
    return slain

def get_monster_move(monst):
    if monst >= 67:
        a = random.choice([1, 1, 1, 2, 2, 2, 3])
    elif 37 < monst < 67:
        a = random.choice([1, 1, 2, 2, 3, 3])
    else:
        a = random.choice([1, 2, 3, 3, 3, 3, 3])
    return a

def battle(userChar, monsterChar):
    for x in range(0, 100):
        if x % 2 == 0:
            print("*************************************")
            print("It is now " 
                + userChar.name
                + "'s turn.")
            a = choose_move()
            if a == '1':
                monsterChar.health = quick_attack(attack_player=userChar.name,defense_player_health=monsterChar.health)
                print("The Monster now has " 
                    + str(monsterChar.health)
                    + " health.")
                end_game = check_health(player_health=monsterChar.health)
                if end_game:
                    return True
            elif a == '2':
                monsterChar.health = power_attack(attack_player=userChar.name, defense_player_health=monsterChar.health)
                print("The Monster now has " 
                    + str(monsterChar.health)
                    + " health.")
                end_game = check_health(player_health=monsterChar.health)
                if end_game:
                    return True
            elif a == '3':
                userChar.health = heal(attack_player_health=userChar.health, attack_player=userChar.name)
                print(userChar.name + " now has " + str(userChar.health) + " health.\n")          
        sleep(1)   
        if x % 2 == 1:
            print("*************************************")
            print("It is now the Monster's turn.")
            a = get_monster_move(monsterChar.health)
            if a == 1:
                userChar.health = quick_attack(attack_player="Monster", defense_player_health=userChar.health)
                print(userChar.name + " now has " + str(userChar.health) + " health.")
                end_game = check_health(player_health=userChar.health)
                if end_game:
                    return True
            elif a == 2:
                userChar.health = power_attack(attack_player="Monster", defense_player_health=userChar.health)
                print(user.name + " now has " + str(userChar.health) + " health.")
                end_game = check_health(player_health=userChar.health)
                if end_game:
                    return True
            elif a == 3:
                monsterChar.health = heal(attack_player="Monster", attack_player_health=monsterChar.health)
                print("The Monster now has " + str(monsterChar.health) + " health.\n")

def get_game_status(status):
    end_game = status
    while end_game is False:
        end_game = battle(userChar=user, monsterChar=monster)

def equip_item(userChar, item):
    userChar.equip_item(item)
    return userChar.equipped

if __name__ == "__main__":

    monster = Monster(kind=random.choice(['Demon', 'Lizard', 'Humanoid', 'Beast']),
                    health=random.choice([100, 105, 95, 100, 90, 110, 100, 90, 95]),
                    loot=random.choice(['Magic Sword', 'Magic Bow'])
                    )

    user = Character(gender='Male',
         profession='Archer',
         race='Elf', 
         name=input('Please Enter Your Name\n'), 
         health=100
         )

    print("Welcome to the Battle Royale between two players:\n" + user.name + " vs. The Monster\n")
    get_game_status(status=False)
    print("The battle has now ended")
    # loot_monster(slain=monster)

    if loot_monster(slain=monster) == monster:
            user.add_inventory(monster.loot)
    
    print("Items in " + str(user.name) + "'s inventory : " +  str(user.items))
    print(str(user.name) + " has equipped the following item: " + str(equip_item(userChar=user, item=monster.loot)))
    

