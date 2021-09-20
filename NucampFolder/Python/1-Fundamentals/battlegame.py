# Set up your game variables: the game characters and their stats.

wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

wizard_hp = 80
elf_hp = 60
human_hp = 50
dragon_hp = 75
orc_hp = 70

wizard_damage = 100
elf_damage = 100
human_damage = 100
dragon_damage = 100
orc_damage = 100

# Prompt the player to choose from a list of options.
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    print("5) Exit")
    print("Choose your character: ")
    userChoose = input()
    if userChoose == "1" or userChoose.lower() == "Wizard".lower():
        character = wizard
        my_damage = wizard_damage
        my_hp = wizard_hp
        break
    elif userChoose == "2" or userChoose.lower() == "Elf".lower():
        character = elf
        my_damage = elf_damage
        my_hp = elf_hp
        break
    elif userChoose == "3" or userChoose.lower() == "Human".lower():
        character = human
        my_damage = human_damage
        my_hp = human_hp
        break
    elif userChoose == "4" or userChoose.lower() == "Orc".lower():
        character = orc
        my_damage = orc_damage
        my_hp = orc_hp
        break
    elif userChoose == "5":
        exit()
    else:
        print("Unknown character")
print(character)
print("Health: ", my_hp)
print("Health: ", my_damage)

my_hp = wizard_hp
my_damage = human_damage


# Battle with the Dragon!
while True:
    dragon_hp -= my_damage
    print("The", character, "damaged the Dragon!")
    print("Dragon's hitpoints are now ", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The", character, "was damaged by the Dragon")
    if my_hp < 0:

        print("The", character, "'s hitpoints are now ", my_hp)
        print("The", character, "lost the battle")
while True:
    print("Would you like to play again?")
    userChoose = input()
    if userChoose.lower() == "No".lower():
        exit()
