import numpy as np

# This is a simple code which will calculate the biggest product of tree factors, which itself sum up to 2020.
# I was lazy which is why this algorithm has an runtime of O(n^3).
x = np.genfromtxt(r"input.txt")

maxMulti = 0
currentFirst = 0
currentMiddle = 0
currentLast = 0

for f in x:
    for m in x:
        for l in x:
            if (f + m + l) == 2020:
                if (f * m * l) > maxMulti:
                    maxMulti = f * m * l
                    currentFirst = f
                    currentMiddle = m
                    currentLast = l

print(maxMulti)
print(currentFirst)
print(currentMiddle)
print(currentLast)
