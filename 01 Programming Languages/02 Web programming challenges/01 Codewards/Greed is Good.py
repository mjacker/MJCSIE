# not the best solution, but well...
def score(dice):
    pass # your code here
    counts = [(dice).count(y) for y in [x for x in range(1, 7, 1)]]
    puntos = 0
    while sum(counts) > 0:
          # for case 1
        if counts[0] > 2:
            counts[0] -=3
            puntos += 1000
        if counts[1] > 2:
            counts[1] -= 3
            puntos += 200
        if counts[2] > 2:
            counts[2] -= 3
            puntos += 300
        if counts[3] > 2:
            counts[3] -= 3
            puntos += 400
        if counts[4] > 2:
            counts[4] -= 3
            puntos += 500
        if counts[5] > 2:
            counts[5] -= 3
            puntos += 600
        
          # for other cases
        if counts[0] > 0:
            counts[0] -=1
            puntos += 100
        if counts[4] > 0:
            counts[4] -=1
            puntos += 50
        if counts[1] > 0:
            counts[1] -= 1
        if counts[2] > 0:
            counts[2] -= 1
        if counts[3] > 0:
            counts[3] -= 1
        if counts[5] > 0:
            counts[5] -= 1
    return puntos

print(score([1, 1, 1, 3, 1]))
