import math
import random
import numpy as np
import matplotlib.pyplot as plt

def average_error(n, time, epsilon):
    N = n
    time_window = time
    time_step = time_window / float((N - 1))

    tt = np.linspace(0, time_window, N)
    r = np.zeros(N)

    u = np.log(tt + 5) + 0.4 * tt
    rexact = 1.0 / (tt + 5) + 0.4
    ep = epsilon
    uep = u + ep * (1 - 2 * np.random.rand(N))

    for k in range(N - 1):
        r[k] = (uep[k + 1] - uep[k]) / time_step

    r[N - 1] = r[N - 2]
    Q = np.mean(np.abs(r - rexact))

    return Q


if __name__ == "__main__":

    N = 10000
    closest = [float('inf'), float('inf'), float('inf')]

    for i in range(N):
        A = abs(average_error(95, 30, 0.001))
        B = abs(average_error(13, 30, 0.05))

        C = abs(B / A)

        if C < closest[-1]:
            closest = [A, B, C, abs( B / A - math.sqrt(50) )]

    

    print( 'A: {}\nB: {}\nA / B: {}\nC: {}'.format(closest[0], closest[1], closest[2], closest[3]) )


