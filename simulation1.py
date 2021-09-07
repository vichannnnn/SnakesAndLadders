import random


# TODO: Script to simulate playing the game 10000 times and checks the average steps taken to finish the game.
#       This is assuming they got the answers all wrong.

nodes = [i for i in range(1, 101)]  # Nodes from 1 to 100

snakeAndLaddersNodes = {
    38: ['Snake', 11, 'Question1', 'Answer1'],
    40: ['Snake', 12, 'Question1', 'Answer1'],
    41: ['Snake', 4, 'Question1', 'Answer1'],
    44: ['Snake', 13, 'Question1', 'Answer1'],
    78: ['Snake', 49, 'Question1', 'Answer1'],
    15: ['Snake', 2, 'Question1', 'Answer1'],
    80: ['Snake', 51, 'Question1', 'Answer1'],
    17: ['Snake', 7, 'Question1', 'Answer1'],
    50: ['Snake', 31, 'Question1', 'Answer1'],
    5: ['Ladder', 43, 'Question1', 'Answer1'],
    42: ['Ladder', 57, 'Question1', 'Answer1'],
    72: ['Ladder', 91, 'Question1', 'Answer1'],
    79: ['Ladder', 93, 'Question1', 'Answer1'],
    86: ['Ladder', 98, 'Question1', 'Answer1'],
    23: ['Ladder', 53, 'Question1', 'Answer1'],
    25: ['Ladder', 48, 'Question1', 'Answer1'],
    30: ['Ladder', 66, 'Question1', 'Answer1']

}

eventNodes = [node for node in snakeAndLaddersNodes]


class Nodes:
    def __init__(self, node):
        self.Event = 1 if node in eventNodes else 0
        self.EventType = snakeAndLaddersNodes[node][0] if self.Event == 1 else None
        self.MoveTo = snakeAndLaddersNodes[node][1] if self.Event == 1 else None
        self.Question = snakeAndLaddersNodes[node][2] if self.Event == 1 else None
        self.Answer = snakeAndLaddersNodes[node][3] if self.Event == 1 else None

games = []

for game in range(999999):
    Playing = True

    stepsTaken = 0
    currentNode = 1

    while Playing:
        if currentNode == 100:
            print(f"Congratulations! You've completed the Snake & Ladders in {stepsTaken} steps.")
            Playing = False
            games.append(stepsTaken)
            break

        stepsTaken += 1
        diceRoll = random.choice(range(1, 7))
        currentNode += diceRoll
        nodeObject = Nodes(currentNode)
        eventCheck = nodeObject.Event

        if currentNode > 100:
            overshot = currentNode - 100
            currentNode = 100 - overshot
            continue

        if eventCheck:
            eventType = nodeObject.EventType
            if eventType == "Snake":
                answerInput = "a"

                if answerInput == nodeObject.Answer:
                    continue

                currentNode = nodeObject.MoveTo
                continue

            if eventType == "Ladder":
                answerInput = "a"

                if answerInput != nodeObject.Answer:
                    continue

                currentNode = nodeObject.MoveTo
                continue

from statistics import mode

def most_common(List):
    return mode(List)


longestGame = max(games)
shortestGame = min(games)
averageGame = sum(games) / len(games)
mostFrequent = most_common(games)
print("Longest Game: ", longestGame)
print("Shortest Game: ", shortestGame)
print("Average Steps per Game: ", averageGame)
print("Most occurrence steps taken: ", mostFrequent)

a = input("Enter any key to exit\n")