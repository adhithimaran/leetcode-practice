import math


def minEatingSpeed(piles, h):
    # piles = list of ints (num bananas in each pile)
    # h = hours you have to each all bananas
    #k = b/hr rate (min int that you can eat all bananas within h hour)
    # len(p) <= k
    speed = min(piles)
    while True:
        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile / speed)
        
        if totalTime <= h:
            return speed
        speed += 1
    return speed

piles = [1,4,3,2]
h = 9
print(minEatingSpeed(piles, h)) # 2

piles = [25,10,23,4]
h = 4
print(minEatingSpeed(piles, h)) # 25