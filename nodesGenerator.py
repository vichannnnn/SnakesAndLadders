import random

# TODO: To randomly generate snake and ladder nodes, use the commented code block below.

nodes = [i for i in range(1, 101)]  # Nodes from 1 to 100

generatedSnakes = []
generatedLadders = []

for i in range(10):
    chosen = random.choice(nodes)
    while chosen in generatedSnakes or chosen == 100 or chosen < 30:
        chosen = random.choice(nodes)
    generatedSnakes.append(chosen)

for i in range(10):
    chosen = random.choice(nodes)
    while chosen in generatedSnakes + generatedLadders or chosen > 85:
        chosen = random.choice(nodes)
    generatedLadders.append(chosen)

occupiedNodes = generatedSnakes + generatedLadders
goesDown = []
goesUp = []

for n in generatedSnakes:
    goesDownTo = n - random.choice(range(10, 40))

    while goesDownTo <= 0 or goesDownTo in goesUp + goesDown + occupiedNodes:
        goesDownTo = n - random.choice(range(10, 40))
    goesDown.append(goesDownTo)


for n in generatedLadders:
    goesUpTo = n + random.choice(range(10, 40))

    while goesUpTo >= 100 or goesUpTo in goesUp + goesDown:
        if 90 > n > 70:
            goesUpTo = n + random.choice(range(10, 30))
            while goesUpTo >= 100 or goesUpTo in goesUp + goesDown + occupiedNodes:
                goesUpTo = n + random.choice(range(10, 30))

        else:
            goesUpTo = n + random.choice(range(10, 40))
    goesUp.append(goesUpTo)

for n, i in enumerate(generatedSnakes):
    print(f"Snake: {i} -> {goesDown[n]}")

for n, i in enumerate(generatedLadders):
    print(f"Ladder: {i} -> {goesUp[n]}")
