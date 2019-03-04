
from random import randint          #imports random function
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN #for rounding

#return the modifier for the proficiency bonus
def profBounsCalc(value):
    calc = (value-10)/2
    if calc < 0:
        profBonus = Decimal(calc).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
    else:
        profBonus = Decimal(calc).quantize(Decimal('1.'), rounding=ROUND_HALF_DOWN)
    return profBonus


clear = "\n" * 100                  #Set to Clear Screen For better viewing
global PlayerHealth                 #Global Variable to control PlayerHealth, 
global playerInventory              #and Player Inventory
global PlayerXP                     #global player XP goes up on kills
global PlayerLevel                  #Player Level goes up incrementally 
global PBonus                       #proficiency bonus, this would go up if you leveled up.

#Your stats
PlayerStrength = profBounsCalc(18)  #determines how likely you are to hit. Modifier value
PlayerLevel = 1                     #player Level
PlayerXP = 0                        #player XP
PBonus = 2
PlayerArmor = 10                    #defends against hits
PlayerHealth = 5000                  #How much HP you have
PlayerLuck = 15                     #How much luck for loot
PlayerOrgHealth = PlayerHealth      #Original Health to show progress
PlayerWeapon = [8, 1, "Long Sword"] #Type of Dice, Name is in Second Position

PlayerAtkBonus = PlayerStrength + PBonus   #How strong your Attack is

print(PlayerStrength)
#Rolls Dice Given the type of dice to roll, x is type of dice, y is how many rolls
def dice(x, y):
    roll = 1                        #roll counter
    total = 0                       #sum total between the rolls
    while roll <= y:
        #print(str(randint(1,x)) + "   " + str(x))
        total += randint(1,x)
        roll += 1
    return total

#display the health
def displayHealth(name, currHealth, totalHealth, armor, weapon):
    health = round(round((currHealth / totalHealth) * 100) / 10) * 2
    spaces = 20 - health
    printout = name.ljust(15) +'[' + '\x1b[3;31;40m' + ('█' * health) + ' ' * spaces +  '\x1b[0m' + '] '  + str(currHealth).ljust(3) + 'HP\n'.ljust(18) +  '\x1b[0;37;44m' + 'AC│╬│:' + str(armor).ljust(2) +  '\x1b[0m' +"  ══╫∞" + '\x1b[0;37;42m' + weapon[2].ljust(20) + ':' + str(weapon[0]).ljust(2) +  '\x1b[0m' 
    print(printout)

#print death
def deathGraphic():
    print('\x1b[1;31;40m' + r"""
               ...                              
             ;::::;                            
           ;::::; :;                               
         ;:::::'   :;                             
        ;:::::;     ;.                                    
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `""" + '\x1b[0m')
   

def displayHit():
    print('\x1b[1;31;40m' + r"""
 `.  :  .'   
   `m$$m     
 ''$$$$$$''  
 .' `$$'`.   
'     :   `  
      :      
""" + '\x1b[0m')

#dispay the enemey
def displayImage(name):
    switch = {
    "Rat" : r"""               
      _  _  .-'   '-.
     (.)(.)/         \   
      /@@             ;
     o_//-mm-......-mm`~~~~~~~~~~~~~~~~`""",
    "Skeleton" : r"""
    ,--.
   ([ oo]
    `- ^\
  _  I`-'
,o(`-V'
|( `-H-'
|(`--A-'
|(`-/_ '\
O `'I `` \
(\  I    |\,
  \-T-"`, |H""",
  "Spider" : r"""
          ^^         |         ^^
          ::         |         ::
   ^^     ::         |         ::     ^^
   ::     ::         |         ::     ::
    ::     ::        |        ::     ::
      ::    ::       |       ::    ::
        ::    ::   _/~\_   ::    ::
          ::   :::/     \:::   ::
            :::::(       ):::::
                  \ ___ /
             :::::/`   `\:::::
           ::    ::\o o/::    ::
         ::     ::  :":  ::     ::
       ::      ::   ` `   ::      ::
      ::      ::           ::      ::
     ::      ::             ::      ::  
     ^^      ::             ::      ^^
             ::             ::
             ^^             ^^
""",
"Stone Giant" : r"""
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \    \     ( '        )(    )
      \    \    \.  _.__ ____( .  |
       \  / \   .(   .'  /\  '.  )
        \(   \.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             ' \ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,""",
"level" : r"""
         ^
        / \
       /   \
      /|   |\ 
       |   |
       |   |
"""
    }
    print(switch.get(name, "No Image"))

#level check
def levelCheck(PlayerStrength):
    global PlayerLevel
    global PlayerXP
    global PBonus

    L  = {} #LevelArray
    L[1] = [0,1,2]
    L[2] = [300,2,2]
    L[3] = [900,3,2]
    L[4] = [2700,4,2]
    L[5] = [6500,5,3]
    L[6] = [14000,6,3]
    L[7] = [23000,7,3]
    L[8] = [34000,8,3]
    L[9] = [48000,9,4]
    L[10] = [64000,10,4]
    L[11] = [85000,11,4]
    L[12] = [100000,12,4]
    L[13] = [120000,13,5]
    L[14] = [140000,14,5]
    L[15] = [165000,15,5]
    L[16] = [195000,16,5]
    L[17] = [225000,17,6]
    L[18] = [265000,18,6]
    L[19] = [305000,19,6]
    L[30] = [355000,20,6]

    while(PlayerXP >= L[PlayerLevel+1][0]):
        PlayerLevel += 1
        displayImage("level")
        print("You Leveled UP : " + str(PlayerLevel))
        PBonus = L[PlayerLevel][2] + PlayerStrength #use chart to figure out proficiency bonus
 
    
        

#attack  (attacker name, Attacker Weapon hit, Attacker Bonus, strength, defender name, defender armor, defender health, defender OrigHealth)
def attack(attacker, weapon, atkBonus, strength, defender, defArmor, defHealth, defOrigHealth, isEnemy, XP):
    global PlayerXP
    print(attacker + " Attacks " + defender)
    attackRoll = dice(20, 1) #roll D20 for attack
    print("Rolled " + str(attackRoll) + " + " + str(atkBonus) + "(AtkBns) = " + str(atkBonus +  attackRoll))
    if atkBonus +  attackRoll > defArmor or attackRoll == "20":  #if better than armor or d20 critical hit
        if strength < 0:    #weak enemies were hiting for positive health.
            strength = 0
        damage = strength + dice(weapon[0], weapon[1])
        if(attackRoll == "20"):  #if roll 20 Critical HIT add another roll to the damage
            print('\x1b[1;31;40m' + "Critical HIT!!!!!!" + '\x1b[0m')
            damage += dice(weapon[0], weapon[1])
        defHealth = defHealth - damage
        if defHealth > 0:
            print('\x1b[1;31;40m' + attacker + " Hits for " + str(damage) + '\x1b[0m' )
            displayHit()
            print(defender + " has " + str(defHealth) + " out of " + str(defOrigHealth) + " health remaining")
            return defHealth
        else:
            print(attacker + " Killed " + defender + " with " + str(damage) + " damage (✖╭╮✖)")
            if(isEnemy):
                PlayerXP += XP
                levelCheck(strength)
                #enemyArray[defender][1] = 0 #Update the Enemy health
            else:
                deathGraphic()
                print("You DIED!!!  Game OVER!!!!")
                exit()
            return 0 
    else:
        print('\x1b[1;36;43m' + attacker + " Missed!!" +  '\x1b[0m')
        print(defender + " has " + str(defHealth) + " out of " + str(defOrigHealth) + " health remaining")
        return defHealth


def openInventory(playerInventory):
    pi = playerInventory[:]
    if(len(pi) == 0):
        input("You Have No Inventory..Press Enter to Continue")
        return 0
    else:
        o = 1
        for i in pi:
            print(str(o) + ") " + i.name)
            o += 1
        c = int(input("Choose Option: ")) - 1 #array starts at zero
        type(c)
        if(pi[c].typ == "heal"):
            heal(playerInventory[c]) #send player choice to heal funciton
            del(playerInventory[c]) #removes item from inventory
            return pi[c]             #returns the inventory item so you know how to use it
        else:
            del(playerInventory[c]) #deletes the inventory item
            return pi[c]            #returns the inventory item so you know how to use it
    

#healing function 
def heal(item):
    global PlayerHealth             #python needs this so it knows you're using the global variable
    PlayerHealth += item.amount     #add the current player health to the item you used
    print("You have Healed Yourself for " + str(item.amount) + " HP")

#looting funciton
def loot(luck):
    # add [Name, Value (If weapon or spell add [dice,rolls]), type(heal,spell,weapon)]
    # ex> Meteor Swarm spell has 20 dice rolled 500 times
    switch = {
        1: ["Potion of Healing",dice(4, 2) + 2, "heal"],
        2: ["Potion of Greater Healing",dice(4, 4) + 4, "heal"],
        3: ["Meteor Swarm",[4,25], "spell"],   
        4: ["Sheild Of Valor",15, "armor"],
        5: ["King Aurthors Sword",[12,20], "weapon"]
    } 
    maxchance = 15                     #change this if you want to make it harder to find things or you have more items
    itemtotal = len(switch)  
    if(luck > maxchance-itemtotal):    #if your luck is too high it adjust so you always find something
        maxchance = itemtotal
    else: 
        maxchance = 15
        
    chance = dice(maxchance, 1)    #Roll Dice to randomize the chance of an item
    selected = switch.get(chance, "You Found Nothing") #if chance equals one of the switch itmes then you get an item
    if(selected[0] != "You Found Nothing"): 
        newItem = I_Item(selected[0], selected[1], selected[2])  #create the item
        PlayerInventory.append(newItem)  #add that item (object) to the inventory array
    else:
        print("You Found Nothing")
        
    
class I_Item:
  def __init__(self, name, value, typ):
    self.name = name
    self.amount = value
    self.typ = typ
    print("You Found " + self.name )

#Gets the Name of the Char
PlayerName = input("What is your name? ")
type(PlayerName)
print('Welcome ' + PlayerName + ' your adventure begins now')

#Inventory, starts with single healing potion.
PlayerInventory = [I_Item("Potion of Healing",dice(4,2) + 2, "heal")]    

#Name, Health (Calls Dice), StrengthModifier, armor, atackBonus, weapon(dice, how many dice, name), XP
#Dice is how many sides x, and how many rolls y dice(x,y)
#Make sure enemy weapon has 3 values, [Dice, HowManyRolls, Name]
enemyArray = {}
enemyArray['Rat'] = ['Rat', dice(4,1), -4, 10, 0, [1, 1, "bite"], 10]
enemyArray['Spider'] = ['Spider', dice(4,1),-4, 12, 4, [1, 1, "bite"], 10]
enemyArray['Skeleton'] = ['Skeleton', dice(8,2) + 4, 0, 13, 4, [6, 1, "axe"], 50]
enemyArray['Stone Giant'] = ['Stone Giant', dice(12,11)+55, 6, 17, 9, [8, 3, "Huge Club"], 2900]

totalEnemies = len(enemyArray)



while totalEnemies > 0:
    print("Your XP: "+ str(PlayerXP) + " | Level:" + str(PlayerLevel))  
    print("==============================================") 
    for i in enemyArray:
        n = i
        if(enemyArray[n][1] != 0):
            print('\x1b[1;31;40m' + n +  '\x1b[0m')
        else:
            totalEnemies -= 1
    

    #Choos enemy    
    enemy = ""
    while enemy == "":
        enemy = input("Pick Your Enemy: ")
        type(enemy)
        if enemy in enemyArray:
            continue
        else:
            print("No Enemy Selected, Try Again")
            enemy = ""
    
    print(clear)
    
    #Sets All the Enemy Stats
    EnemyName = enemyArray[enemy][0]
    EnemyOrigHealth = enemyArray[enemy][1]
    EnemyHealth = enemyArray[enemy][1]
    EnemyStrength = enemyArray[enemy][2]
    EnemyArmor = enemyArray[enemy][3]
    EnemyAttack = enemyArray[enemy][4]
    EnemyWeapon = enemyArray[enemy][5]
    EnemyXP = enemyArray[enemy][6]
    
    #print(str(EnemyName) + " has " + str(EnemyHealth) + " Health")
    while EnemyHealth > 0:
        displayImage(EnemyName)
        displayHealth(EnemyName, EnemyHealth, EnemyOrigHealth, EnemyArmor, EnemyWeapon)
        displayHealth(PlayerName, PlayerHealth, PlayerOrgHealth, PlayerArmor, PlayerWeapon)
        print("-----------------------")
        #List Options
        menu = {
                "I": "Inventory",
                "A": "Attack with " + PlayerWeapon[2],
                "L": "Loot"
        } 
        for key, value in menu.items():
            print(key + "-" + value)
        choice = input("Your Choice: ")
        type(choice)
        selected = menu.get(choice, "You Selected Nothing")

        print(clear)
        
        if(choice == "I"):  #If inventory
            print(clear)
            print(PlayerName + " Opens Inventory")
            result = openInventory(PlayerInventory)
            if(result == 0):
                print(clear)
            elif(result.typ == "spell"):
                tempWeapon = [int(result.amount[0]), int(result.amount[1]), result.name]  #Sets the Spell as A weapon for one turn
                EnemyHealth = attack(PlayerName, tempWeapon, 50, PlayerStrength, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True, EnemyXP)
            elif(result.typ == "armor"):
                PlayerArmor = result.amount
                print("Your Armor Has been updated to " + str(result.amount))
            elif(result.typ == "weapon"):
                PlayerWeapon[0] = result.amount[0] #dice
                PlayerWeapon[1] = result.amount[1] #roll Amount
                PlayerWeapon[2] = result.name      #weapon Name
                print("Your weapon Has been updated to " + str(result.amount))
        elif(choice == "A"): #If attack
            EnemyHealth = attack(PlayerName, PlayerWeapon, PlayerAtkBonus, PlayerStrength, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True, EnemyXP)
        elif(choice == "L"): #If Loot
            loot(PlayerLuck)

        
        if(EnemyHealth > 0):
            input('\x1b[0;31;47m' + "Prepare to be attacked!!!! " + '\x1b[0m' + "\n Press Enter to Continue")
            print(clear)
            print("-----------------------")
            PlayerHealth = attack(EnemyName, EnemyWeapon, EnemyAttack, EnemyStrength, PlayerName, PlayerArmor, PlayerHealth, PlayerOrgHealth, False, 0)
            input("Press Enter to Continue")
            print(clear)
        else:
            print('\x1b[0;31;47m' + "You Search For Loot" + '\x1b[0m')
            loot(PlayerLuck) #loot the body
    


