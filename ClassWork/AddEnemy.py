#Name, Health (Calls Dice), StrengthModifier, armor, atackBonus, weapon(dice, name)
#Dice is how many sides x, and how many rolls y dice(x,y)
enemyArray = {}
enemyArray['Rat'] = ['Rat', dice(4,1), -4, 10, 0, [1, "bite"]]
enemyArray['Spider'] = ['Spider', dice(4,1),-4, 12, 4, [1, "bite"]]
enemyArray['Skeleton'] = ['Skeleton', dice(8,2) + 4, 0, 13, 4, [6, "axe"]]
enemyArray['Stone Giant'] = ['Stone Giant', dice(12,11)+55, 6, 17, 9, [8,"Huge Club"]]
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
 
    print("Enemy Name:   " + EnemyName)
    print("Enemy Weapon: " + EnemyWeapon[1])
    print(str(EnemyName) + " has " + str(EnemyHealth) + " Health")
