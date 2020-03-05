import random


class Monster:
    def __init__(self, kind, health, loot):
        self.kind = kind
        self.health = health
        self.loot = loot
    

    def add_loot(self, item):
        self.loot.append(item)


class Character:
    def __init__(self, name, race, profession, gender, health):
        self.name = name
        self.race = race
        self.profession = profession
        self.gender = gender
        self.items = []
        self.health = health

    def add_inventory(self, item):
        self.items.append(item)

    def subtract_inventory(self, item):
        self.items.remove(item)


def choose_move():
    move = input("Please choose one of the following moves:\n\n 1. Quick Attack. \n 2. Power Attack.\n 3. Heal.\n")
    return move


def quick_attack(attack_player, defense_player_health):
    damage = random.randint(15, 22)
    defense_player_health -= damage
    print(attack_player + " has dealt " + str(damage) + " damage.\n")
    return defense_player_health


def power_attack(attack_player, defense_player_health):
    damage = random.choice(['miss', 'miss', 'miss', 'miss', random.randint(25, 35), random.randint(25, 35),
                            random.randint(25, 35), random.randint(25, 35), random.randint(25, 35),
                            random.randint(25, 35)])
    if damage == 'miss':
        print(attack_player + " has missed their power attack!\n")
    else:
        defense_player_health -= damage
        print(attack_player + " has dealt " + str(damage) + " damage.\n")
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

monster = Monster(kind=random.choice(['Demon', 'Lizard', 'Humanoid', 'Beast']),
                health=random.choice([100, 105, 95, 100, 90, 110, 100, 90, 95]),
                loot=random.choice(['Magical Axe', 'Magical Sword', 'Magical Bow']))

user = Character(gender='Male', profession='Archer', race='Elf', name='', health=100)
user.name = input("Please enter your name\n")

print("Welcome to the Battle Royale between two players:\n" + user.name + " vs. The Monster\n")

end_game = False

while not end_game:
    for x in range(0, 100):
        if x % 2 == 0:
            print("*************************************")
            print("It is now " + user.name + "'s turn.")
            a = choose_move()
            if a == '1':
                monster.health = quick_attack(attack_player=user.name, defense_player_health=monster.health)
                print("The Monster now has " + str(monster.health) + " health.")
                end_game = check_health(player_health=monster.health)
                if end_game:
                    break
            if a == '2':
                monster.health = power_attack(attack_player=user.name, defense_player_health=monster.health)
                print("The Monster now has " + str(monster.health) + " health.")
                end_game = check_health(player_health=monster.health)
                if end_game:
                    break
            if a == '3':
                b = heal(attack_player_health=user.health, attack_player=user.name)
                print(user.name + " now has " + str(b) + " health.\n")
        if x % 2 == 1:
            print("*************************************")
            print("It is now the Monster's turn.")
            if monster.health >= 67:
                a = random.choice([1, 1, 1, 2, 2, 2, 3])
            elif 37 < monster.health < 67:
                a = random.choice([1, 1, 2, 2, 3, 3])
            else:
                a = random.choice([1, 2, 3, 3, 3, 3, 3])
            if a == 1:
                user.health = quick_attack(attack_player="Monster", defense_player_health=user.health)
                print(user.name + " now has " + str(user.health) + " health.")
                end_game = check_health(player_health=user.health)
                if end_game:
                    break
            if a == 2:
                user.health = power_attack(attack_player="Monster", defense_player_health=user.health)
                print(user.name + " now has " + str(user.health) + " health.")
                end_game = check_health(player_health=user.health)
                if end_game:
                    break
            if a == 3:
                b = heal(attack_player="Monster", attack_player_health=monster.health)
                print("The Monster now has " + str(b) + " health.\n")

print("The battle has now ended")

if end_game is True:
    if monster.health <= 0:
        print("The Monster has been defeated!\nCollect your loot hero!")
        print("The Monster has dropped a " + str(monster.loot) + "\nClaim your prize victor!")

    else:
        print(user.name + " has died\nThe battle is now over")
