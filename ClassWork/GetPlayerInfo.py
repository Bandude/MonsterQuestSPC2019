from random import randint          #imports random function

clear = "\n" * 100                 	 #Set to Clear Screen For better viewing
global PlayerHealth                	 #Global Variable to control PlayerHealth, 
global playerInventory             	 #and Player Inventory

#Gets the Name of the Char
PlayerName = input("What is your name? ")
type(PlayerName)

print('Welcome ' + PlayerName + ' your adventure begins now')

#Your stats
PlayerStrength = 3                  #determines how likely you are to hit. Modifier value
PBonus = 2                          #proficiency bonus, this would go up if you leveled up.
PlayerArmor = 10                    #defends against hits
PlayerHealth = 20                   #How much HP you have
PlayerLuck = 15                     #How much luck for loot
PlayerOrgHealth = PlayerHealth      #Original Health to show progress
PlayerWeapon = [8, "Long Sword"]    #Type of Dice, Name is in Second Position

PlayerAtkBonus = PlayerStrength + PBonus   #How strong your Attack is
