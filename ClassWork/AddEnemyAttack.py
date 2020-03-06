        if(EnemyHealth > 0):
            input('\x1b[0;31;47m' + "Prepare to be attacked!!!! " + '\x1b[0m' + "\n Press Enter to Continue")
            print(clear)
            print("-----------------------")
            PlayerHealth = attack(EnemyName, EnemyWeapon[0], EnemyAttack, EnemyStrength, PlayerName, PlayerArmor, PlayerHealth, PlayerOrgHealth, False)
            input("Press Enter to Continue")
            print(clear)
