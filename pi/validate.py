from mpmath import mp
import sys
mp.dps = 100
TRUE_PI = str(mp.pi)
f = open(f"pi/pi.txt", "r")
pi = f.read()
f.close()
true_pi_part = TRUE_PI[:len(pi)]
print(pi)
print(true_pi_part)
print(pi == true_pi_part)
if pi == true_pi_part:
    sys.exit(0)
else:
    sys.exit(1)

