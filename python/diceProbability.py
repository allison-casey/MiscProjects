
if __name__ == '__main__':
    from random import randint
    import sys
    
    import argparse
    parser = argparse.ArgumentParser(description='Calculates the probability of a successful dice roll')

    parser.add_argument('dice', type=int, nargs='+', metavar='Dice',
            help="types of dice to roll given as a list of space separated ints")
    parser.add_argument('-N', type=int, metavar='',
            help='number of trials to roll for')
    parser.add_argument('-s', '--success', type=int, metavar='',
            help='number to pass in order to succeed')
    parser.add_argument('-m', '--modifiers', type=int, nargs=4, metavar='',
            help='''Modifiers that are applied to the dice post initial roll.
                    Order is as such: Perception Range Cover Height''')
    parser.add_argument('--advantage', type=int, choices=[0, 1],
            help='First role is rolled with advantage. Max(2d?)')
    args = parser.parse_args()

    # Statistics Variables
    N           = args.N        if args.N       != None else 10000
    threshold   = args.success  if args.success != None else 10
    die         = args.dice
    
    # Roll Modifiers
    perception_mod, range_mod, cover_mod, height_mod = \
            args.modifiers if args.modifiers != None else [0, 0, 0, 0]

    successes = 0
    for i in range(N):
        dice = 0
        if args.advantage == 1:
            dice += max(randint(1, die[0]), randint(1, die[0])) + sum( [randint(1, i) for i in die[1:]] )
        else:
            dice = sum( [randint(1, i) for i in die] )

        roll = dice + range_mod + perception_mod
        roll = roll - cover_mod - height_mod
        if roll >= threshold:
            successes += 1
    
    output = """
    Modifiers----------------------------------------------
    Perception: {}
    Range: {}
    Cover: {}
    Height: {}
    Base Hit Chance: {}
               
    Result-------------------------------------------------
    Trials: {} Success: {} Probability: {}\n\n""".format(
                        perception_mod, range_mod, cover_mod, height_mod, threshold, 
                        N, successes, successes/(float(N)))
    sys.stdout.write(output)

