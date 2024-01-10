#towers of hanoi

def moveTower(height, fromPole, toPole, withPole):
    if height == 1 :
        print("moving disk from", fromPole, "to", toPole)
    else:
        moveTower(height-1, fromPole, withPole, toPole)
        moveTower(1, fromPole, toPole, withPole)
        moveTower(height-1, withPole, toPole, fromPole)

moveTower(3, "A", "B", "C")