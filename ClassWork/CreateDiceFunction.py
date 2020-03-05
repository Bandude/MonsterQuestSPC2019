#Rolls Dice Given the type of dice to roll, x is type of dice, y is how many rolls
def dice(x, y):
   roll = 1                        #roll counter
   total = 0                       #sum total between the rolls
   while roll <= y:
       #print(str(randint(1,x)) + "   " + str(x))
       total += randint(1,x)
       roll += 1
   return total
