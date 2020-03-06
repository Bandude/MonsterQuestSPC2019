    while EnemyHealth > 0:
        print("-----------------------")
        choice = input("Choose What to Do: \n S - Attack with Sword \n Your Choice: ")
        type(choice)
        print(clear)
      
        if(choice == "S"):
            EnemyHealth = attack(PlayerName, PlayerWeapon[0], PlayerAtkBonus, PlayerStrength, EnemyName, EnemyArmor, EnemyHealth, EnemyOrigHealth, True)


