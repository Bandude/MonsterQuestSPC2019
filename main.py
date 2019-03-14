from random import randint          #imports random function
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN #for rounding


clear = "\n" * 100                  #Set to Clear Screen For better viewing
global playerInventory              #and Player Inventory


#Rolls Dice Given the type of dice to roll, x is type of dice, y is how many rolls
def dice(x, y):
    roll = 1                        #roll counter
    total = 0                       #sum total between the rolls
    while roll <= y:
        total += randint(1,x)
        roll += 1
    return total

#Figures out the modifier
def modCalc(value):                        
    calc = (value-10)/2
    if calc < 0:
        profBonus = int(Decimal(calc).quantize(Decimal('1.'), rounding=ROUND_HALF_UP))
    else:
        profBonus = int(Decimal(calc).quantize(Decimal('1.'), rounding=ROUND_HALF_DOWN))
    return profBonus



#display the health
def displayHealth(name, currHealth, totalHealth, armor, weapon):
    health = round(round((currHealth / totalHealth) * 100) / 10) * 2
    spaces = 20 - health
    if(totalHealth < currHealth): #if over full health just put full bar
        spaces = 0
        health = 20
    printout = name.ljust(15) +'[' + '\x1b[3;31;40m' + ('█' * health) + ' ' * spaces +  '\x1b[0m' + '] '  + str(currHealth).ljust(3) + 'HP\n'.ljust(18) +  '\x1b[0;37;44m' + 'AC│╬│:' + str(armor).ljust(2) +  '\x1b[0m' +"  ══╫∞" + '\x1b[0;37;42m' + weapon[2].ljust(20) + ':' + str(weapon[0]).ljust(2) +  '\x1b[0m' 
    print(printout)


class I_Item:
  def __init__(self, name, value, typ):
    self.name = name
    self.amount = value
    self.typ = typ
    print("You Found " + self.name )

class PlayerClass:   #this is where you create a player
    
    f = {}
    featureCount = 0

    def __init__(self):    
        self.XP = 0
        self.Level = 1
        self.Prof = 2                                   #proficiency bonus
        self.Strength = modCalc(18)
        self.Constitution = modCalc(14)
        self.Dex = modCalc(14)                          #dex
        self.Luck = 15
        response = input("What is your name? ")
        type(response)
        self.Name = response                       
        print(clear)

    def addFeature(self, feature):
        self.featureCount += 1
        self.f[self.featureCount] = [feature[0], feature[1], feature[2], feature[3]]

    def rest(self):
        for key in self.f:
            self.f[key][2] = self.f[key][3]             #update the features to max
        

class Fighter(PlayerClass):

    def initialize(self):
        self.HitDice = 10
        self.Health = self.HitDice + self.Constitution   #staring only
        self.OrigHealth = self.Health
        self.MaxHealth = self.Health
        self.AtkBonus = self.Strength + self.Prof
        self.Armor = 18
        self.Weapon = [8, 1, "Long Sword"] 
        self.printPlayer()
        self.addFeature(["secondWind", "Second Wind", 1, 1])           #second wind on level 1, method name, friendly name, current use, max use

    def printPlayer(self):
        displayHealth(self.Name, self.Health, self.MaxHealth, self.Armor, self.Weapon)

    def secondWind(self, featurePos):
        if(self.f[featurePos][2] > 0):
            roll = dice(self.HitDice, 1)
            print("You Rolled " + str(roll) + " you heal for " + str(roll+self.Level))
            self.Health += roll + self.Level
            if self.Health > self.OrigHealth:
                self.Health = self.OrigHealth
            self.f[featurePos][2] -= 1                                   #use skill
        else:
            print("You need to rest before you can use again")
        

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
    "Worg" : r"""
           _        _
          /\\     ,'/|
        _|  |\-'-'_/_/
   __--'/`           \
       /              \
      /        "o.  |o"|
      |              \/
       \_          ___\
         `--._`.   \;//
              ;-.___,'
             /
           ,'
        _-'
        """,
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
def levelCheck(Player):

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

    while(Player.XP >= L[Player.Level+1][0]):
        Player.Level += 1
        displayImage("level")
        print("You Leveled UP : " + str(Player.Level))
        rollforhealth = input("Do you want to roll for health? (Y or N")
        type(rollforhealth)
        if(rollforhealth == "Y"):
            roll = dice(Player.HitDice, 1)
            Player.Health = ((roll + Player.Constitution) * Player.Level)  + Player.Constitution      #if you roll
            Player.MaxHealth = Player.Health
            print(clear)
            print("You rolled a " + str(roll))
            print("New Health " + str(Player.Health))
        else:
            Player.Health = (((Player.HitDice / 2) + 1 + Player.Constitution) * Player.Level) + Player.Constitution  #if no roll half hit dice plus one plus const
            Player.MaxHealth = Player.Health
            print(clear)
            print("You rolled a " + str(roll))
            print("New Health " + str(Player.Health))
            
        
        Player.Prof = L[Player.Level][2] + Player.Strength #use chart to figure out proficiency bonus
        Player.rest()
        Player.printPlayer()

        
 
    
        

#attack  (attacker name, Attacker Weapon hit, Attacker Bonus, strength, defender name, defender armor, defender health, defender OrigHealth)
def attack(attacker, weapon, atkBonus, strength, defender, defArmor, defHealth, defOrigHealth, isEnemy, XP, Player):
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
                Player.XP += XP
                levelCheck(Player)
                #enemyArray[defender][1] = 0 #Update the Enemy health
            else:
                deathGraphic()
                print("You DIED!!!  Game OVER!!!!")
                exit()
            return 0 
    else:
        print('\x1b[0;31;47m' + attacker + " Missed!!" +  '\x1b[0m')
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
        del(playerInventory[c]) #deletes the inventory item
        return pi[c]            #returns the inventory item so you know how to use it
    

# open selection for using a specific feature
def selectFeature(Player):
    actions = {}
    for key, value in Player.f.items():
        actions.update({key:value[0]})
        print(str(key) + ") " + value[1])
    choice = input("Your Choice: ")
    type(choice)
    getattr(Player, actions[int(choice)])(int(choice))

#healing function 
def heal(item):
    print("You have Healed Yourself for " + str(item.amount) + " HP")
    return item.amount     #add the current player health to the item you used

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
        


#Init Player and Player's class
Player = Fighter()
Player.initialize()
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
enemyArray['Worg'] = ['Worg', dice(10, 4) + 4, 3, 13, 5, [6, 2, "Bite"], 100]

totalEnemies = len(enemyArray)



while totalEnemies > 0:
    print("Your XP: "+ str(Player.XP) + " | Level:" + str(Player.Level))  
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
        Player.printPlayer()
        print("-----------------------")
        #List Options
        menu = {
                "A": "Attack with " + Player.Weapon[2],
                "F": "Use Feature",
                "I": "Inventory",
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
            print(Player.Name + " Opens Inventory")
            result = openInventory(PlayerInventory)
            if(result == 0):
                print(clear)
            elif(result.typ == "heal"):
                Player.Health = heal(result)
            elif(result.typ == "spell"):
                tempWeapon = [int(result.amount[0]), int(result.amount[1]), result.name]  #Sets the Spell as A weapon for one turn
                EnemyHealth = attack(Player.Name, tempWeapon, 50, Player.Strength, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True, EnemyXP, Player)
            elif(result.typ == "armor"):
                Player.Armor = result.amount
                print("Your Armor Has been updated to " + str(result.amount))
            elif(result.typ == "weapon"):
                Player.Weapon[0] = result.amount[0] #dice
                Player.Weapon[1] = result.amount[1] #roll Amount
                Player.Weapon[2] = result.name      #weapon Name
                print("Your weapon Has been updated to " + str(result.amount))
        elif(choice == "A"): #If attack
            EnemyHealth = attack(Player.Name, Player.Weapon, Player.AtkBonus, Player.Strength, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True, EnemyXP, Player)
        elif(choice == "L"): #If Loot
            loot(Player.Luck)
        elif(choice == "F"):
            selectFeature(Player)

        
        if(EnemyHealth > 0):
            input('\x1b[0;31;47m' + "Prepare to be attacked!!!! " + '\x1b[0m' + "\n Press Enter to Continue")
            print(clear)
            print("-----------------------")
            Player.Health = attack(EnemyName, EnemyWeapon, EnemyAttack, EnemyStrength, Player.Name, Player.Armor, Player.Health, Player.MaxHealth, False, 0, Player)
            input("Press Enter to Continue")
            print(clear)
        else:
            print('\x1b[0;31;47m' + "You Search For Loot" + '\x1b[0m')
            loot(Player.Luck) #loot the body
    


