import random
from mpmath import mp

files = 6
numbers_per_file = 12

mp.dps = 100

err_idx = random.randint(1, files - 1)
pi = ""
for i in range(files):
    part = str(mp.pi)[(numbers_per_file * i):(numbers_per_file * (i + 1))]
    new_part = part
    if i == err_idx:
        while new_part == part:
            new_part = new_part.replace(str(random.randint(0, len(part) - 1)), str(random.randint(0, 9)), 1)
    pi += new_part
    with open(f"{i}.txt", "w") as f:
        f.write(pi)

print(pi[:numbers_per_file * files])
print(str(mp.pi)[:numbers_per_file * files])
print(err_idx)

