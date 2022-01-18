# Setting up
import time
import random
import sys


# Stats = [Base Attack, Def, Name, HP] - Monster Edition
snakeman = [8, 3, "Fiery Snake", 10]
slime = [5, 2, "Slime", 8]
chad = [8, 4, "Snake Ogre", 20]

manSerpent = [10, 4, "Man-Lizard", 12]
stoneSerpent = [1, 7, "Stone Serpent", 10]
locust = [3, 3, "Locust Conjurator", 15]

legionKnight = [10, 7, "Ophidian Legion Knight", 15]
perennialGuardian = [4, 7, "Perennial Guardian", 20]
borealGuardian = [15, 5, "Boreal Serpent Guardian", 20]

generic_monsters = [snakeman, chad, slime]
forest_monsters = [manSerpent, stoneSerpent, locust]
dungeon_monsters = [legionKnight, perennialGuardian, borealGuardian]

current_monsters = []

windy = [15, 3, "Princess Windy", 40]

# Health Values
player_Health = 15
global level
level = 1

# Stats =   [Base Attack, Defense, Name] - Human Edition
Baker = [7, 5, "Baker", "Rolling Pin"]
Warrior = [10, 3, "Warrior", "Sword"]
Sorcerer = [13, 2, "Sorcerer", "Staff"]
possible_characters = [Sorcerer, Warrior, Baker]

# Second Ending - Counts Up every time you pick a 'greedy' option. At the end, if the meter is passed a certain number, you'll get the second ending.
monopoly_meter = 0

friendshipBracelet = False


def windyBattle():
    global level, player_Health, current_monsters, your_monster

    your_monster = windy

    inNotWanderBattle = True

    currentPlayerHealth = player_Health
    currentMonsterHealth = your_monster[3]

    while inNotWanderBattle:
        print("Your HP: " + str(currentPlayerHealth))
        print("Windy's HP " + str(currentMonsterHealth))
        fight_choice = input("What would you like to do?    1. Attack       2. Defend   ")
        print()

        if fight_choice == "1":
            time.sleep(2)

            # currentCharacter[0] - This is your attack.  Random # from -2 to 2 added to damage for some randomness. your_monster[1] is the monsters defense
            damageDealtToMonster = (currentCharacter[0] + random.randint(-2, 2)) - your_monster[1]
            if damageDealtToMonster <= 0:
                damageDealtToMonster = 1
            currentMonsterHealth -= damageDealtToMonster

            print("You did " + str(damageDealtToMonster) + " damage to windy!")
            print()
            time.sleep(1)
            print("\" How dare you attack me!? \"")
            time.sleep(2)

            if currentMonsterHealth <= 20:

                print("\" Enough of this. I don't feel like playing around anymore, begone. \"")
                print()
                time.sleep(1)
                inNotWanderBattle = False
                time.sleep(3)

            else:
                print("Windy has " + str(currentMonsterHealth) + " health left!")
                print()
                time.sleep(2)

                # your_monster[0] -> Monster's attack.  Random # from -2 to 2 added to damage for some randomness. currentCharacter[1] is the your defense
                damageDealtToPlayer = (your_monster[0] + random.randint(-2, 2)) - currentCharacter[1]

                if damageDealtToPlayer <= 0:
                    damageDealtToPlayer = 0
                currentPlayerHealth -= damageDealtToPlayer
                print("Windy smacks you across the cheek for " + str(damageDealtToPlayer) + " damage!")
                print()
                time.sleep(2)

                if currentPlayerHealth <= 0:
                    inNotWanderBattle = False
                    print("You really couldn't beat me? Wow. Weak. Wait, what are you- ")
                    time.sleep(3)

                else:
                    print("You are at " + str(currentPlayerHealth) + " HP!")
                    print()
                    time.sleep(2)

        if fight_choice == "2":
            print("You tried defending against the Windy's smack, but she was too powerful!")
            print()
            time.sleep(1.5)

            damageDealtToPlayer = ((your_monster[0] + random.randint(-2, 2)) - currentCharacter[1]) / 2

            if damageDealtToPlayer <= 0:
                damageDealtToPlayer = 0
            currentPlayerHealth -= damageDealtToPlayer
            print("Windy smacks you across the cheek, albeit with some difficulty, for " + str(
                damageDealtToPlayer) + " damage!")
            print()
            time.sleep(2)

            if currentPlayerHealth <= 0:
                print("You are at 0 HP!")
                print("You blacked out!")
                print()
                inNotWanderBattle = False
                time.sleep(3)
                print("You really couldn't beat me? Wow. Wait, what are you- ")
                time.sleep(2)

            else:
                print("You are at " + str(currentPlayerHealth) + " HP!")
                print()
                time.sleep(2)


pass


def puzzle():
    puzzleRealAnswer = "silence"

    inPuzzle = True
    while inPuzzle:
        puzzleChoice = input("What would you like to do?    1. Answer   2. Check hint   ")

        if puzzleChoice == "1":
            puzzlePlayerAnswer = input("Type your answer: ").lower().strip()

            if puzzlePlayerAnswer == puzzleRealAnswer:
                print("A sudden whirring and groaning emanates from the door.")
                print()
                time.sleep(3)

                inPuzzle = False

            else:
                print("Nothing happened. I guess that was wrong.")
                print()
                time.sleep(1)

        elif puzzleChoice == "2":
            print()
            print("What disappears as soon as you say it’s name?")
            print()
            time.sleep(3.5)

        else:
            print('Pick a choice!')
            print()
            time.sleep(1)


pass


def battling(whichMonster):
    global level, player_Health, current_monsters, your_monster

    if whichMonster == 1:
        your_monster = borealGuardian

    inNotWanderBattle = True

    currentPlayerHealth = player_Health
    currentMonsterHealth = your_monster[3]

    while inNotWanderBattle:
        print("Your HP: " + str(currentPlayerHealth))
        print("Monster's HP " + str(currentMonsterHealth))
        fight_choice = input("What would you like to do?    1. Attack       2. Defend   ")
        print()

        if fight_choice == "1":
            time.sleep(2)

            # currentCharacter[0] - This is your attack.  Random # from -2 to 2 added to damage for some randomness. your_monster[1] is the monsters defense
            damageDealtToMonster = (currentCharacter[0] + random.randint(-2, 2)) - your_monster[1]
            if damageDealtToMonster <= 0:
                damageDealtToMonster = 1
            currentMonsterHealth -= damageDealtToMonster

            print("You did " + str(damageDealtToMonster) + " damage to the monster!")
            print()
            time.sleep(2)

            if currentMonsterHealth <= 0:
                level += 1
                player_Health += 3
                currentCharacter[0] += 3

                print("You won the battle!")
                print()
                time.sleep(1)
                print("You leveled up! You gained 3 HP and 3 ATK. ")
                print("You are currently level " + str(level))
                print()
                inNotWanderBattle = False
                time.sleep(3)

            else:
                print("The monster has " + str(currentMonsterHealth) + " health left!")
                print()
                time.sleep(2)

                # your_monster[0] -> Monster's attack.  Random # from -2 to 2 added to damage for some randomness. currentCharacter[1] is the your defense
                damageDealtToPlayer = (your_monster[0] + random.randint(-2, 2)) - currentCharacter[1]

                if damageDealtToPlayer <= 0:
                    damageDealtToPlayer = 0
                currentPlayerHealth -= damageDealtToPlayer
                print("The monster attacks you for " + str(damageDealtToPlayer) + " damage!")
                print()
                time.sleep(2)

                if currentPlayerHealth <= 0:
                    print("You are at 0 HP!")
                    print("You blacked out!")
                    print()
                    inNotWanderBattle = False
                    time.sleep(3)
                    print(
                        'You awaken on the floor, your muscles feel quite stiff but you\'re ready to go out on an adventure again. \n')
                    time.sleep(2)

                else:
                    print("You are at " + str(currentPlayerHealth) + " HP!")
                    print()
                    time.sleep(2)

        if fight_choice == "2":
            print("You defended against the monster's attack!")
            print()
            time.sleep(2)

            currentMonsterHealth -= currentCharacter[1]
            print("It took damage equal to your defense!")
            print()
            time.sleep(2)

            if currentMonsterHealth <= 0:
                player_Health += 3
                currentCharacter[0] += 3
                level += 1

                print("You won the battle!")
                print()
                time.sleep(1)
                print("You leveled up! You gained 3 HP and 3 ATK. ")
                print("You are currently level " + str(level))
                print()
                inNotWanderBattle = False
                time.sleep(3)

            else:
                print("The monster is at " + str(currentMonsterHealth) + " HP!")
                print()
                time.sleep(2)


pass


# wandering around
def wander(location=1):
    # The game will have different locations with different enemies
    # if location = 1, the monsters will be generic snake guys
    # if location = 2, the monsters will be ice forest themed
    # if location = 3, the monsters will be ice dungeon themed

    global level, player_Health, current_monsters, friendshipBracelet
    isWandering = True
    while isWandering:
        # 2 in 3 chance to find a monster
        chance_to_find_monster = random.randint(1, 3)
        if chance_to_find_monster >= 2:
            monsterfound = True
        else:
            monsterfound = False

        # Setting the monsters for each location
        if location == 1:
            current_monsters = generic_monsters

        elif location == 2:
            current_monsters = forest_monsters

        elif location == 3:
            current_monsters = dungeon_monsters

        # picks 1 of the 3 possible monsters in the list to fight you
        monster_chance = random.randint(0, len(current_monsters) - 1)
        your_monster = current_monsters[monster_chance]

        if monsterfound:
            time.sleep(2)
            print("After walking around and taking in the scenery you find yourself interrupted by a " + your_monster[
                2] + "!")
            print()
            time.sleep(3)

            wander_choice = input("What would you like to do?    1. Fight          2. Run ")
            if wander_choice == "1":
                print()
                time.sleep(2)

                print("You're fighting the monster!")
                print()
                time.sleep(2)

                inBattle = True

                currentPlayerHealth = player_Health
                currentMonsterHealth = your_monster[3]

                while inBattle:
                    print("Your HP: " + str(currentPlayerHealth))
                    print("Monster's HP " + str(currentMonsterHealth))
                    fight_choice = input("What would you like to do?    1. Attack   2. Defend   3. Run ")
                    print()

                    if fight_choice == "1":
                        time.sleep(2)

                        # currentCharacter[0] - This is your attack.  Random # from -2 to 2 added to damage for some randomness. your_monster[1] is the monsters defense
                        damageDealtToMonster = (currentCharacter[0] + random.randint(-2, 2)) - your_monster[1]
                        if damageDealtToMonster <= 0:
                            damageDealtToMonster = 1
                        currentMonsterHealth -= damageDealtToMonster

                        print("You did " + str(damageDealtToMonster) + " damage to the monster!")
                        print()
                        time.sleep(2)

                        if currentMonsterHealth <= 0:
                            level += 1
                            player_Health += 3
                            currentCharacter[0] += 3

                            print("You won the battle!")
                            print()
                            time.sleep(1)
                            print("You leveled up! You gained 3 HP and 3 ATK. ")
                            print("You are currently level " + str(level))
                            print()
                            time.sleep(3)

                            if (not friendshipBracelet) and (random.randint(0, 100) < 30):
                                print("You notice this monster had a funny looking bracelet on it. You take it for safe-keeping")
                                print()
                                friendshipBracelet = True

                            inBattle = False
                            isWandering = False
                            time.sleep(3)



                        else:
                            print("The monster has " + str(currentMonsterHealth) + " health left!")
                            print()
                            time.sleep(2)

                            # your_monster[0] -> Monster's attack.  Random # from -2 to 2 added to damage for some randomness. currentCharacter[1] is the your defense
                            damageDealtToPlayer = (your_monster[0] + random.randint(-2, 2)) - currentCharacter[1]

                            if damageDealtToPlayer <= 0:
                                damageDealtToPlayer = 0
                            currentPlayerHealth -= damageDealtToPlayer
                            print("The monster attacks you for " + str(damageDealtToPlayer) + " damage!")
                            print()
                            time.sleep(2)

                            if currentPlayerHealth <= 0:
                                print("You are at 0 HP!")
                                print("You blacked out!")
                                print()
                                inBattle = False
                                isWandering = False
                                time.sleep(3)
                                print(
                                    'You awaken on the floor, your muscles feel quite stiff but you\'re ready to go out on an adventure again. \n'
                                )
                                time.sleep(2)

                            else:
                                print("You are at " + str(currentPlayerHealth) + " HP!")
                                print()
                                time.sleep(2)

                    if fight_choice == "2":
                        print("You defended against the monster's attack!")
                        print()
                        time.sleep(2)

                        currentMonsterHealth -= currentCharacter[1]
                        print("It took damage equal to your defense!")
                        print()
                        time.sleep(2)

                        if currentMonsterHealth <= 0:
                            player_Health += 3
                            currentCharacter[0] += 3
                            level += 1

                            print("You won the battle!")
                            print()
                            time.sleep(1)
                            print("You leveled up! You gained 3 HP and 3 ATK. ")
                            print("You are currently level " + str(level))
                            print()
                            isWandering = False
                            inBattle = False
                            time.sleep(3)

                        else:
                            print("The monster is at " + str(currentMonsterHealth) + " HP!")
                            print()
                            time.sleep(2)

                    if fight_choice == "3":
                        print("You attempt to escape from the monster! ")
                        print()
                        time.sleep(1)

                        escapeChance = random.randint(1, 10)
                        if escapeChance != 9:
                            print("You escaped from the monster! ")
                            print()
                            time.sleep(2)
                            return

                        elif escapeChance == 9:
                            print("You couldn't escape the monster! ")

                            # your_monster[0] -> Monster's attack.  Random # from -2 to 2 added to damage for some randomness. currentCharacter[1] is the your defense
                            damageDealtToPlayer = (your_monster[0] + random.randint(-2, 2)) - currentCharacter[1]
                            currentPlayerHealth -= damageDealtToPlayer
                            print("The monster attacks you for " + str(damageDealtToPlayer) + " damage!")
                            print()
                            time.sleep(2)

                            if currentPlayerHealth <= 0:
                                print("You are at 0 HP!")
                                print("You blacked out!")
                                print()
                                inBattle = False
                                isWandering = False
                                time.sleep(3)
                                print(
                                    'You awaken on the floor, your muscles feel quite stiff but you\'re ready to go out on an adventure again. \n'
                                )
                                time.sleep(2)

                            else:
                                print("You are at " + str(currentPlayerHealth) + " HP!")
                                print()
                                time.sleep(2)


            elif wander_choice == "2":
                print()
                time.sleep(0.5)
                print("You fled from the monster!")
                print()
                isWandering = False

        if not monsterfound:

            if location == 2:
                print("It seemed that the area was just as void of life as you originally thought. Still pretty.")
                print()
                time.sleep(1)

            secondWanderChoice = input(
                "You didn't find a monster. Would you like to keep wandering?    1. Yes    2. No \n")
            if secondWanderChoice == "2":

                print()
                print("You decided to stop wandering.")
                print()
                time.sleep(2)

                return
            else:
                print("You keep wandering.")
                print()
                time.sleep(0.5)


pass


def optionMenuFunction(wanderchoice, textVariable):
    global whatToDo
    if textVariable == 1:
        whatToDo = "< 1. Continue on your path forwards >"
    elif textVariable == 2:
        whatToDo = "< 1. Oh! Some challenges for my journey. My middle name is practically Danger > "
    optionMenu = True
    while optionMenu:
        optionChoice = input(
            "What would you like to do?  " + whatToDo + "  < 2. Wander around for a bit >  \n")
        print()

        if optionChoice == "1":
            optionMenu = False
            print("You chose to continue forth on your path.")
            print()
            time.sleep(1.5)

        if optionChoice == "2":
            print("You chose to wander around a bit.")
            print()
            time.sleep(0.5)

            wander(wanderchoice)


pass

print("Welcome to Generic Land! \n")
print()

name = input("Hello, player. Before the game starts, what is your name? \n")
print()

print("     ()-() \n "
      "     | | \n "
      "  | (o_o) \n "
      " | |/   \ \n"
      "  | |_____\ \n"
      "   |  | |   \n")
print(" ")
print("       /// \n "
      "  /\  // \n "
      "  ||(===) \n "
      "  ||/   \ \n"
      "   ==_____\ \n"
      "    | | |   \n")
print(" ")
print("       /\ \n "
      "    _/_\_  \n "
      "  O (o_o) \n "
      "  | /   \ \n"
      "   |/_____\ \n"
      "   |  | |   \n")
print(" ")
playerCharacterChoice = input("Which character would you like to use? \n"
                              "1. Baker - Low Attack, High Defense \n"
                              "2. Warrior - Medium Attack, Medium Defense \n"
                              "3. Sorcerer - High Attack, Low Defense \n")
print()

global currentCharacter

pickingCharacter = True
while pickingCharacter:
    if playerCharacterChoice == "1":
        currentCharacter = Baker
        pickingCharacter = False

    elif playerCharacterChoice == "2":
        currentCharacter = Warrior
        pickingCharacter = False

    elif playerCharacterChoice == "3":
        currentCharacter = Sorcerer
        pickingCharacter = False

    elif playerCharacterChoice != "1" or "2" or "3":
        playerCharacterChoice = input("Pick a number from 1 to 3! ")
        print()
        time.sleep(1)

print("Your character is a: " + str(currentCharacter[2]))
print()

time.sleep(3)
print("There has been a recent outrage in the kingdom of Ais (pronounced Ice), a cold city \n"
      "located near the top of a mountain. You decided such a town was “cool” and stopped in \n"
      "to take another quest or two, and perhaps sight-see")
print(" ")
print("    /\ \n "
      "  /  \   /\ \n"
      "  /    \_/  \ \n")
time.sleep(8)

print()

print("King Berger’s daughter has been missing as of recent.")
time.sleep(4)

print()

print("Walking around the festive streets and hearing the locals’ gossip has been enough to \n"
      "inform you that princess Windy (Pronounced Wendy) has been kidnapped by a dragon. \n"
      "The last part piqued your interest and off you went to attempt to aid the king.\n")

time.sleep(8)

print()

print("King Berger was more than willing to offer you a hefty sum of money, as no one else \n"
      "was as eager to help save his daughter.")
time.sleep(4)

print()

kingBergerChoice = input("Choose: \n"
                         "1. < Keep the money, burger boy! Justice is my reward > \n"
                         "2. < How much are we talking? > \n")
print()
if kingBergerChoice == "1":
    print("While the king is pleasantly surprised with the lack of a need to spend a \n"
          "fortune, he is also put off by your extreme passion")
    time.sleep(3.5)
    print()

elif kingBergerChoice == "2":
    print("The king makes a lot of hand signals with… his hands, before sighing and giving \n"
          "you a large enough number to get you fully on board")
    monopoly_meter += 1
    time.sleep(3.5)
    print()

optionMenuFunction(1, 1)

print("~~~")
print(" ")
print("You set off to save princess Windy, heading towards the most likely location for a \n"
      "dragon to hoard treasures (and hostages). The tip of the mountain! \n")
print()
time.sleep(3.5)

print("While the kingdom is near the tip of the mountain, there is still a journey to get there.\n "
      "A large forest of mostly snowed over trees presents itself as a buffer in your path. A howling \n"
      "breeze and a few strange noises can be heard as you walk into the tundra. \n")
print()
time.sleep(4.5)

print("While cold, empty, and being something that fuels the loneliness in your heart, the forest is actually quite pretty.")
print()
time.sleep(4)

print("It makes you miss your time spent in your busy hometown…")
print()
print()

optionMenuFunction(2, 1)

print("After going on so many quests and adventures, your navigational abilities have gotten exceptionally good. \n"
      "Currently, your mental map was leading you to a change in the scenery.")
print()
time.sleep(4)

print("The frost on the dark gray stones chaotically placed around was not enough \n"
      "to stop it from contrasting greatly with the white snow.")
print()
time.sleep(4)

print("~~~")
print("As you continue to walk towards them you realize that they are misplaced stones \n"
      "from the very long stone ruins that stretches as far as the eye could see.")
print(" \n"
      "     oo   ____  \n "
      "    ___ /    \___      ooo \n"
      "____/     I  I    \_____________ \n"
      "    |     I  I       <>  <>  <> \n ")
print()
time.sleep(4)

iceRuinChoice = input("Choose: \n"
                      "1. < “Oh! Some challenges for my journey. My middle name is practically Danger.” > \n"
                      "2. < “I might find something valuable as I've heard.” > \n")
print()

if iceRuinChoice == "2":
    monopoly_meter += 1

print("You enter the ruins, not having much else of an option as going around would take far too long… \n"
      "If there was an end to these ruins in the first place. \n")
print()
time.sleep(4.5)

print("The chilly air sharply leaves you, a moist and humid atmosphere taking its place. \n"
      "You notice tons of armored statues situated on the walls, most of them have rusted over time. ")
print()
time.sleep(4.5)

print("You think to yourself...")
print()
time.sleep(2)

optionMenuFunction(2, 1)

print("As you make your way through the corridors, you step on a stone plate that sinks into the floor. \n"
      "The floor begins shaking as the layer of dust on a large statue blows off in plumes.")
print()
time.sleep(4.5)

print(
    "After the rumbling stops, the statue of a knight in armor steps forward off of it's platform! He slowly walks \n"
    "towards you and readies his weapon.")
print()
time.sleep(5)

battling(1)

print("With the knight gone, you continue forth. All the rumbling had exposed a crevice that you could crawl into")
print()
time.sleep(4)

print(
    "The crevice leads you into a room, you can see what looks like an exit locked behind some sort of contraption.")
print()
time.sleep(4)

print("You also see another path that seems to lead nowhere.")
print()
time.sleep(3.5)

optionMenuFunction(3, 1)

print("You eventually step up to the contraption and notice a set of buttons with the alphabet \n"
      "on them. A piece of glass above it says “password: _”.")
print()
time.sleep(4)

print("Great. There wasn’t anyone to shake around for the password to the door, \n"
      "but you do happen to notice a yellow piece of paper with something written on it attached to the glass.")
print()
time.sleep(4)

print("The paper reads \"What disappears as soon as you say it’s name?\"? ")
print()
time.sleep(5)

print("A hint, how handy. You ready your fingers, or other limbs if you prefer, to type… \n")
print()
time.sleep(2.5)

puzzle()

print("~~~")
print("As the door lifts up, a bright light and cold air rushes in. \n"
      "You see a familiar, storybook-like spire on the horizon")
print(" ")
print(" ooo \n"
      "      / \ \n "
      "    /   \  ooo \n"
      "     |   | \n"
      "     |   | \n"
      "_____| D |_____ \n")
print()
time.sleep(4.5)

print(
    "The spire is situated at the center of an old, rundown town, untouched by the cold as the other frostbitten buildings are.")
print()
time.sleep(4)

print("A roaring hiss coming from the giant tower breaks through the sound of the wind.")
print()
time.sleep(3)

princessWindyChoice = input("You think to yourself… \n"
                            "1. < “I better hurry, princess Windy may be hurt.” >\n"
                            "2. < “The gold better be worth it.” >\n")

if princessWindyChoice == "2":
    monopoly_meter += 1

print("You run up to the spire, " + str(currentCharacter[3]) + " in hand. \n"
      "You bust through the door, the lock snapping easily, and run up the countless stairs.")
print()
time.sleep(6.5)


if friendshipBracelet:

    print("~~~")
    print("You walk up the stairs and open the door to find the princess with a broom in her hand,\n"
          " whacking a dragon, who is more scared than angry.")
    print("")
    print("         __/\__       ______ \n "
          "   ____/  __  \     / \  \   \  \n "
          "   \_____      \   /  _\  \   \  \n"
          "         \       \_/ / /_____ \n "
          "         |                  \         /\ \n"
          "       _______       ___/    \________/ |  \n"
          "      /__________|__/__________________/")
    print()
    time.sleep(5)

    print("You look at the quarreling duo and then at the friendship bracelets you had picked up earlier.")
    print()
    time.sleep(4)

    print(" With a gleam in your eye you sling-shot each band onto the princess’s hand and the tail of the dragon.")
    print()
    time.sleep(4)

    print("Suddenly, they stop fighting and start speaking to each other… As well as they can. ")
    print()
    time.sleep(3)

    print("The princess mumbles something and the dragon either gives a snort or a huff. How do they understand each other? I guess that’s the power of friendship, baby.")
    print()
    time.sleep(5)

    print("Eventually you butt in to explain your situation to the princess and the two begin having a conversation again.")
    print()
    time.sleep(5)

    print("“My dragon plan is working smoothly, I didn’t need your intervention, but thank you nonetheless.”")
    print()
    time.sleep(5)

    print("You glance at the bracelets but decide not to mention it")
    print()
    time.sleep(4.5)

    print(" You return to Ais with the princess following behind.\n"
          "King Berger is extremely happy, hosting a celebration and giving you a few extra foodstuff treats as a reward.")
    print()
    time.sleep(6)

    print("A job well done, as anticlimactic as it was.")
    print()
    time.sleep(2.5)

    print("The king occasionally sends a letter begging for you to come back after you made your departure because the princess occasionally goes missing.")
    print()
    time.sleep(5)


    print(" It’s followed up by another letter announcing her arrival and the dismissal of the last, emotion filled letter.\n"
          "You learn to ignore them, the princess has it sorted out.")
    print()
    time.sleep(6.5)


    print("The End")
    print()
    time.sleep(10)


elif monopoly_meter >= 3 and (not friendshipBracelet):
    print("~~~")
    print("You make your way up the stairs, cursing at the fact that a dragon could just fly up here. \n"
          "You open the door to find said dragon with its head on the floor, now staring at you. The princess is standing on top of it.")
    print(" ")
    print("         __/\__       ______ \n "
          "   ____/  __  \     / \  \   \  \n "
          "   \_____      \   /  _\  \   \  \n"
          "         \       \_/ / /_____ \n "
          "         |                  \         /\ \n"
          "       _______       ___/    \________/ |  \n"
          "      /__________|__/__________________/")
    print()
    time.sleep(8)

    print("“Who are you? Let me guess, Berger sent you to get me.“")
    print()
    time.sleep(4)

    print("“I’m getting paid for it.“")
    print()
    time.sleep(4)

    print("“Is that so? I can pay you more than he did if you forget about this quest of yours.")
    print()
    time.sleep(3)

    print("I’ll make it back” She taps her foot on the dragon’s scales.\n"
          "“These go for a good bit of coin, and guess what? It’ll keep regrowing them.”")
    print()
    time.sleep(7)

    print("“Deal.”")
    print()
    time.sleep(4)

    print("The dragon gives you a look of distaste despite its lack of humanoid facial expressions.")
    print()
    print()
    print()
    time.sleep(3)

    print("You take your share of the money and leave the spire as well as the kingdom of Ais, \n"
          "searching for your next job to add to your hoard of gold.")
    print()
    time.sleep(4.5)

    print("You don't go without hearing about princess Windy’s escapades.")
    print()
    time.sleep(3)

    print(
        "It turns out she didn’t factor in that when there are more scales in the market, they aren’t worth ‘a good bit of coin’ anymore.")
    print()
    time.sleep(6)

    print("The End")
    time.sleep(10)

else:
    print("~~~")
    print(
        "You bolt up the copious amount of stairs and find yourself face to face with a giant dragon with a chain around it’s leg.\n"
        "It releases a puff of steam as it looks down at you.")
    print(" ")
    print("         __/\__       ______ \n "
          "   ____/  __  \     / \  \   \  \n "
          "   \_____      \   /  _\  \   \  \n"
          "         \       \_/ / /_____ \n "
          "         |                  \         /\ \n"
          "       _______       ___/    \________/ |  \n"
          "      /__________|__/__________________/")
    print()
    time.sleep(7.5)

    print("“Where is the princess, fiend?!”")
    print()
    time.sleep(3.5)

    print("“Right over here!”")
    print()
    time.sleep(3)

    print("The dragon lowered it’s head, revealing princess Windy standing on top.")
    print()
    time.sleep(4.5)

    print("“I’ve come to rescue you!” You yell out.")
    print()
    time.sleep(3)

    print("“Read the room, buddy. I’m perfectly fine.” She looks down at the dragon, \n"
          "“This dragon won’t be after I sell every scale off of it!”")
    print()
    time.sleep(6.5)

    print("“So… It's the dragon that needs rescuing?”")
    print()
    time.sleep(3.5)

    print("Princess Windy looks down at you with a very confused look.")
    print()
    time.sleep(5)

    print("“I guess…? However, you won’t be stopping me-”")
    print()
    time.sleep(5)

    windyBattle()

    print("While Windy is distracted, you throw your " + currentCharacter[
        3] + " at her (don't worry it's just the handle) knocking her out.")
    print()
    time.sleep(4.5)

    print(
        "You notice that the locks here are really brittle for some reason as you break through the chains on the dragon’s leg, freeing it. ")
    print()
    time.sleep(5)

    print("It huffs as it rams through the wall of the spire and glides through the air. Another job well done.")
    print()
    time.sleep(4)

    print(
        "You can see the dragon fly it’s way to Ais and begin to rampage. It looks like your quest for justice isn’t over yet.")
    print()
    time.sleep(5)

    print("The End")
    print()
    time.sleep(10)