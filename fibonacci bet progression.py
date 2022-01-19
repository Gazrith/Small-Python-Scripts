#practrice functions gv 19/01/22

min_bet = int(input('Enter minmum bet: '))
max_bet = int(input('Enter max bet: '))
bet_sequence = []

def all_bets(min_bet, max_bet):
    for i in range(min_bet, max_bet+1):
        print(i)

#all_bets(min_bet, max_bet)

def make_fib(min_bet, max_bet):

    x = min_bet
    y = min_bet
    z = min_bet
    bet_sequence.append(z)
    bet_sequence.append(z)
    
    
    counter = 0
    while z < max_bet:
        z = x + y
        if z <= max_bet:
            bet_sequence.append(z)
            x = y
            y = z
            
        

make_fib (min_bet, max_bet)
print (bet_sequence)
        

        
    
