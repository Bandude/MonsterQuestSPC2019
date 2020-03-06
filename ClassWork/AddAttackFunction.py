#attack  (attacker name, Attacker Weapon hit, Attacker Bonus, strength, defender name, defender armor, defender health, defender OrigHealth)
def attack(attacker, weapon, atkBonus, strength, defender, defArmor, defHealth, defOrigHealth, isEnemy):
   print(attacker + " Attacks " + defender)
   if atkBonus + dice(20, 1) > defArmor:
       if strength < 0:
           strength = 0
       damage = strength + dice(int(weapon), 1)
       defHealth = defHealth - damage
       if defHealth > 0:
           print('\x1b[1;31;40m' + attacker + " Hits for " + str(damage) + '\x1b[0m' )
           #displayHit()
           print(defender + " has " + str(defHealth) + " out of " + str(defOrigHealth) + " health remaining")
           return defHealth
       else:
           print(attacker + " Killed " + defender + " with " + str(damage) + " damage (✖╭╮✖)")
           if(isEnemy):
               enemyArray[defender][1] = 0 #Update the Enemy health
           else:
               #deathGraphic()
               print("You DIED!!!  Game OVER!!!!")
               exit()
           return 0
   else:
       print('\x1b[1;36;43m' + attacker + " Missed!!" +  '\x1b[0m')
       print(defender + " has " + str(defHealth) + " out of " + str(defOrigHealth) + " health remaining")
       return defHealth
