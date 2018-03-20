from random import randint

N = 10000
success = 0

die = [20, 4]

perception_mod = 0
range_mod = 0
cover_mod = 0 
height_mod = 0

for i in range(N):
    dice = sum( [randint(1, i) for i in die] )

    roll = dice + range_mod + perception_mod
    roll = roll - cover_mod - height_mod
    if roll >= 10:
        success += 1

print("Trials: ", N, "Successes:", success, "Probability:", success / float(N))

