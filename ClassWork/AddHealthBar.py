#display the health
def displayHealth(name, currHealth, totalHealth, armor, weapon):
   health = round(round((currHealth / totalHealth) * 100) / 10) * 2
   spaces = 20 - health
   printout = name.ljust(15) +'[' + '\x1b[3;31;40m' + ('█' * health) + ' ' * spaces +  '\x1b[0m' + '] '  + str(currHealth).ljust(3) + 'HP\n'.ljust(18) +  '\x1b[0;37;44m' + 'AC│╬│:' + str(armor).ljust(2) +  '\x1b[0m' +"  ══╫∞" + '\x1b[0;37;42m' + weapon[1].ljust(20) + ':' + str(weapon[0]).ljust(2) +  '\x1b[0m'
   print(printout)
