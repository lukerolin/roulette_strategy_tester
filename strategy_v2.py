# Program for testing different roulette strategies
# in European Roulette with a given number of spins
# and starting bank

import random
# list of variables that never change on the game

numbers = list(range(0,38))
first_third = list(range(1,13))
second_third = list(range(13,24))
third_third = list(range(25,37))
odds = list(range(1,37,2)) 
evens = list(range(2,37,2))
reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
blacks = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
first_half = list(range(1,19))
second_half = list(range(19,37))




def rominovsky():
    start = int(input("How much did you come to the table with?"))
    win = int(input("What is your goal amount to walk away with?"))
    lose =int(input("How much are you willing to lose?"))
    chip_val=int(input("Will you bet with $5 chips, $10 chips or $25 chips?"))
    bank = start
    max_loss = bank - lose
    spins = 1000
    quads = [1,2,4,5,8,9,11,12]
    lose_nums = [0,3,6,7,10]
    wins = 0
    bust = 0
    while spins > (wins + bust):
        if bank >=win:
            wins += 1
            bank = start;
            pass;
        elif bank < max_loss:
            bust += 1
            bank = start;
            pass;
        elif bank >= max_loss and bank <=win - 1:
            if chip_val == 5:
                bank -= 40;
            elif chip_val == 10:
                bank -= 80;
            else:
                bank -= 800;
            wheel = random.randint(0,37)
            if wheel in lose_nums:
                pass;
            elif wheel in second_third:
                if chip_val == 5:
                    bank += 45;
                elif chip_val == 10:
                    bank += 90;
                else:
                    bank += 900;
            elif wheel in third_third:
                if chip_val == 5:
                    bank += 45;
                elif chip_val == 10:
                    bank += 90;
                else:
                    bank += 900;
                
            elif wheel in quads:
                if chip_val == 5:
                    bank += 45;
                elif chip_val == 10:
                    bank += 90;
                else:
                    bank += 900;
                
        else:
            print('An Error Has Occured')
    quotient = (wins / 1000) * 100
    print("You Won ",quotient, "percent of the time. \n","Win: ",wins, "\n","Busted:" ,bust )    
    
 
rominovsky()
