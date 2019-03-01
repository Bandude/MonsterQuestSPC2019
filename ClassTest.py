from random import randint          #imports random function

clear = "\n" * 100                 	 #Set to Clear Screen For better viewing
global PlayerHealth                	 #Global Variable to control PlayerHealth, 
global playerInventory             	 #and Player Inventory

#Gets the Name of the Char
PlayerName = input("What is your name? ")
type(PlayerName)

print('Welcome, ' + PlayerName + ', your adventure begins now!')

#Your stats
PlayerStrength = 5                  #determines how likely you are to hit.
PlayerArmor = 10                    #defends against hits
PlayerHealth = 20                   #How much HP you have
PlayerLuck = 15                     #How much luck for loot
PlayerOrgHealth = PlayerHealth      #Original Health to show progress
PlayerWeapon = [4,"Sword"]                    #How much damage your weapon adds to your hits
PlayerAttackPower = 6               #How strong your Attack is


#Rolls Dice Given the type of dice to roll, x is type of dice, y is how many rolls
def dice(x, y):
   roll = 1                        #roll counter
   total = 0                       #sum total between the rolls
   while roll <= y:
       total += randint(1,x)
       roll += 1
   return total

#attack  (attacker name, defender name, armor, health, OrigHealth)
def attack(attacker, weapon, Strength, attack, defender, armor, health, OrigHealth, isEnemy):
   print(attacker + " attacks " + defender)
   if Strength + dice(20, 1) > armor:
       damage = weapon + dice(int(attack), 1)
       health = health - damage
       if health > 0:
           print('\x1b[1;31;40m' + attacker + " Hits for " + str(damage) + '\x1b[0m' )
           print(defender + " has " + str(health) + " out of " + str(OrigHealth) + " health remaining")
           return health
       else:
           print(attacker + " Killed " + defender + " with " + str(damage) + " damage (✖╭╮✖)")
           if(isEnemy):
               enemyArray[defender][1] = 0 #Update the Enemy health
           else:
               print("You DIED!!!  Game OVER!!!!")
               exit()
           return 0
   else:
       print('\x1b[1;36;43m' + attacker + " Missed!!" +  '\x1b[0m')
       print(defender + " has " + str(health) + " out of " + str(OrigHealth) + " health remaining")
       return health


#Name, Health (Calls Dice), strength, armor, attack (what type of dice), weapon
#Dice is how many sides x, and how many rolls y dice(x,y)
enemyArray = {}
enemyArray['Rat'] = ['Rat', dice(4,1), 2, 10, 1, [0, "bite"]]
enemyArray['Spider'] = ['Spider', dice(4,1),2, 12, 1, [0, "bite"]]
enemyArray['Skeleton'] = ['Skeleton', dice(8,2), 10, 13, 6, [4, "axe"]]
enemyArray['Stone Giant'] = ['Stone Giant', dice(12,12), 23, 17, 24, [9,"Huge Club"]]

totalEnemies = len(enemyArray)

while totalEnemies > 0:
   print("==============================================")
   for e in enemyArray:
       if(enemyArray[e][1] != 0):
           print('\x1b[1;31;40m' + e +  '\x1b[0m')
       else:
           totalEnemies -= 1

   #Choose enemy   
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

   print(EnemyName)
   print(EnemyWeapon[1])
   print(str(EnemyName) + " has " + str(EnemyHealth) + " Health ")


   while EnemyHealth > 0:
       print("-----------------------")
       choice = input("Choose What to Do: \n S - Attack with Sword \n Your Choice: ")
       type(choice)
       print(clear)
      
       if choice == "S":
           EnemyHealth = attack(PlayerName, PlayerWeapon[0], PlayerStrength, PlayerAttackPower, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True)


       if(EnemyHealth > 0):
           input('\x1b[0;31;47m' + "Prepare to be attacked!!!! " + '\x1b[0m' + "\n Press Enter to Continue")
           print(clear)
           print("-----------------------")
           PlayerHealth = attack(EnemyName, EnemyWeapon[0], EnemyStrength, EnemyAttack, PlayerName, PlayerArmor, PlayerHealth, PlayerOrgHealth, False)
           input("Press Enter to Continue")
           print(clear)


