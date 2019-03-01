
from random import randint          #imports random function

clear = "\n" * 100                  #Set to Clear Screen For better viewing
global PlayerHealth                 #Global Variable to control PlayerHealth, 
global playerInventory              #and Player Inventory

#Your stats
PlayerStrength = 5                  #determines how likely you are to hit.
PlayerArmor = 10                    #defends against hits
PlayerHealth = 20                   #How much HP you have
PlayerLuck = 15                     #How much luck for loot
PlayerOrgHealth = PlayerHealth      #Original Health to show progress
PlayerWeapon = [4, "Long Sword"]    #How much damage your weapon adds to your hits, name of weapon
PlayerAttackPower = 6               #How strong your Attack is



#Rolls Dice Given the type of dice to roll, x is type of dice, y is how many rolls
def dice(x, y):
    roll = 1                        #roll counter
    total = 0                       #sum total between the rolls
    #print(str(y) + "How Many Rolls")
    while roll <= y:
        #print(str(randint(1,x)) + "   " + str(x))
        total += randint(1,x)
        roll += 1
    return total

#display the health
def displayHealth(name, currHealth, totalHealth, armor, weapon):
    health = round(round((currHealth / totalHealth) * 100) / 10) * 2
    spaces = 20 - health
    printout = name.ljust(15) +'[' + '\x1b[3;31;40m' + ('█' * health) + ' ' * spaces +  '\x1b[0m' + '] '  + str(currHealth).ljust(3) + 'HP\n'.ljust(18) +  '\x1b[0;37;44m' + 'AC│╬│:' + str(armor).ljust(2) +  '\x1b[0m' +"  ══╫∞" + '\x1b[0;37;42m' + weapon[1].ljust(20) + ':' + str(weapon[0]).ljust(2) +  '\x1b[0m' 
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
def displayEnemey(name):
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
                        /,/,"""

    }
    print(switch.get(name, "No Image"))


#attack  (attacker name, defender name, armor, health, OrigHealth)
def attack(attacker, weapon, Strength, attack, defender, armor, health, OrigHealth, isEnemy):
    print(attacker + " Attacks " + defender)
    if Strength + dice(20, 1) > armor:
        damage = weapon + dice(int(attack), 1)
        health = health - damage
        if health > 0:
            print('\x1b[1;31;40m' + attacker + " Hits for " + str(damage) + '\x1b[0m' )
            displayHit()
            print(defender + " has " + str(health) + " out of " + str(OrigHealth) + " health remaining")
            return health
        else:
            print(attacker + " Killed " + defender + " with " + str(damage) + " damage (✖╭╮✖)")
            if(isEnemy):
                enemyArray[defender][1] = 0 #Update the Enemy health
            else:
                deathGraphic()
                print("You DIED!!!  Game OVER!!!!")
                exit()
            return 0 
    else:
        print('\x1b[1;36;43m' + attacker + " Missed!!" +  '\x1b[0m')
        print(defender + " has " + str(health) + " out of " + str(OrigHealth) + " health remaining")
        return health


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
    switch = {
        1: ["Potion of Healing",dice(4, 2) + 2, "heal"],
        2: ["Potion of Greater Healing",dice(4, 4) + 4, "heal"],
        3: ["Meteor Swarm",dice(6, 20), "spell"],
        4: ["Sheild Of Valor",15, "armor"],
        5: ["King Aurthors Sword",12, "weapon"]
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

#Name, Health (Calls Dice), Strength, armor, attack (what type of dice), weapon
#Dice is how many sides x, and how many rolls y dice(x,y)
enemyArray = {}
enemyArray['Rat'] = ['Rat', dice(4,1), 2, 10, 1, [0, "bite"]]
enemyArray['Spider'] = ['Spider', dice(4,1),2, 12, 1, [0, "bite"]]
enemyArray['Skeleton'] = ['Skeleton', dice(8,2), 10, 13, 6, [4, "axe"]]
enemyArray['Stone Giant'] = ['Stone Giant', dice(12,12), 23, 17, 24, [9,"Huge Club"]]

totalEnemies = len(enemyArray)



while totalEnemies > 0:
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
    EnemyOrigHealth = enemyArray[enemy][1]
    EnemyHealth = enemyArray[enemy][1]
    EnemyName = enemyArray[enemy][0]
    EnemyArmor = enemyArray[enemy][3]
    EnemyStrength = enemyArray[enemy][2]
    EnemyWeapon = enemyArray[enemy][5]
    EnemyAttack = enemyArray[enemy][4]
    
    #print(str(EnemyName) + " has " + str(EnemyHealth) + " Health")
    while EnemyHealth > 0:
        displayEnemey(EnemyName)
        displayHealth(EnemyName, EnemyHealth, EnemyOrigHealth, EnemyArmor, EnemyWeapon)
        displayHealth(PlayerName, PlayerHealth, PlayerOrgHealth, PlayerArmor, PlayerWeapon)
        print("-----------------------")
        choice = input("Choose What to Do: \n I - Inventory \n S - Attack with Sword \n L - Search For Loot \n Your Choice: ")
        type(choice)
        print(clear)
        
        if(choice == "I"):
            print(clear)
            print(PlayerName + " Opens Inventory")
            result = openInventory(PlayerInventory)
            if(result == 0):
                print(clear)
            elif(result.typ == "spell"):
                EnemyHealth = attack(PlayerName, result.amount, PlayerStrength, PlayerAttackPower, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True)
            elif(result.typ == "armor"):
                PlayerArmor = result.amount
                print("Your Armor Has been updated to " + str(result.amount))
            elif(result.typ == "weapon"):
                PlayerWeapon[0] = result.amount
                PlayerWeapon[1] = result.name
                print("Your weapon Has been updated to " + str(result.amount))
        elif(choice == "S"):
            EnemyHealth = attack(PlayerName, PlayerWeapon[0], PlayerStrength, PlayerAttackPower, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True)
        elif(choice == "L"):
            loot(PlayerLuck)

            
        
        
        if(EnemyHealth > 0):
            input('\x1b[0;31;47m' + "Prepare to be attacked!!!! " + '\x1b[0m' + "\n Press Enter to Continue")
            print(clear)
            print("-----------------------")
            PlayerHealth = attack(EnemyName, EnemyWeapon[0], EnemyStrength, EnemyAttack, PlayerName, PlayerArmor, PlayerHealth, PlayerOrgHealth, False)
            input("Press Enter to Continue")
            print(clear)
        else:
            print('\x1b[0;31;47m' + "You Search For Loot" + '\x1b[0m')
            loot(PlayerLuck) #loot the body
    


    





