import random
from mpmath import mp

files = 6
mp.dps = 100
TRUE_PI = str(mp.pi)
for i in range(files):
    try: 
        with open(f"{i}.txt", "r") as f:
            pi = f.read()
            true_pi_part = TRUE_PI[:len(pi)]
            print(i, pi == true_pi_part)
    except FileNotFoundError:
        break
