import random
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import itertools


nodes = [i for i in range(1, 26)]  # Nodes from 1 to 26

# TODO: Replace 'Fun Fact' with the fun fact of the node, 'Question1' and 'Answer1' as well!
#       Don't touch the '' blanks!
#       You can rearrange the Ladder or Snake nodes and their drop/rise node with the format below as well
#       I have set 4, 10, 11, 17, 24 as the ladder node as you can see, just reverse engineer this format and you will be fine.

snakeAndLaddersNodes = {
    1: ['', 0, '', '', "Fun Fact"],
    2: ['', 0, '', '', "Fun Fact"],
    3: ['', 0, '', '', "Fun Fact"],
    4: ['Ladder', 10, 'Question1', 'Answer1', ''],
    5: ['', 0, '', '', "Fun Fact"],
    6: ['', 0, '', '', "Fun Fact"],
    7: ['', 0, '', '', "Fun Fact"],
    8: ['', 0, '', '', "Fun Fact"],
    9: ['', 0, '', '', "Fun Fact"],
    10: ['Snake', 6, 'Question1', 'Answer1', ''],
    11: ['Ladder', 19, 'Question1', 'Answer1', ''],
    12: ['', 0, '', '', "Fun Fact"],
    13: ['', 0, '', '', "Fun Fact"],
    14: ['', 0, '', '', "Fun Fact"],
    15: ['', 0, '', '', "Fun Fact"],
    16: ['', 0, '', '', "Fun Fact"],
    17: ['Ladder', 23, 'Question1', 'Answer1', ''],
    18: ['', 0, '', '', "Fun Fact"],
    19: ['', 0, '', '', "Fun Fact"],
    20: ['', 0, '', '', "Fun Fact"],
    21: ['', 0, '', '', "Fun Fact"],
    22: ['', 0, '', '', "Fun Fact"],
    23: ['', 0, '', '', "Fun Fact"],
    24: ['Snake', 12, 'Question1', 'Answer1', ''],
    25: ['', 0, '', '', "Fun Fact"]
}


# TODO: 01 02 03 LL 05
#       06 07 08 09 SS
#       LL 12 13 14 15
#       16 LL 18 19 20
#       21 22 23 SS 25

eventNodes = [node for node in snakeAndLaddersNodes if snakeAndLaddersNodes[node][0]]

def boardImage(position):

    # TODO: Replace image link with the background image board that you want (JPG/PNG).

    image_link = "https://media.discordapp.net/attachments/840643585858076713/868525193117700136/unknown.png"
    background_response = requests.get(image_link)
    with Image.open(BytesIO(background_response.content)).convert('RGBA') as my_image:
        background = my_image
        ImageDraw.Draw(background)
        background_draw = ImageDraw.Draw(background)
        w, h = background.size
        blocks = w/5

        coords = []
        n = 0
        k = 0
        for i in range(25):
            x1 = n * blocks
            x2 = (n + 1) * blocks
            y1 = k * blocks
            y2 = (k + 1) * blocks

            n += 1
            coords.append((x1, y1, x2, y2))

            if n == 5:
                n = 0
                k += 1
                continue

        def chunks(l, n):
            n = max(1, n)
            return [l[i:i + n] for i in range(0, len(l), n)]

        rows = chunks(coords, 5)
        rows = reversed([reversed(rows[i]) if i % 2 else rows[i] for i in range(len(rows))])
        rows = list(itertools.chain.from_iterable(rows))

        x1, y1, x2, y2 = rows[position - 1]

        positionFont = ImageFont.truetype(r'BalooChettan-Regular.ttf', 30)
        w, h = background_draw.textsize("X", font=positionFont)

        background_draw.text(((x2 - x1 - w) / 2 + x1, (y2 - y1 - h) / 2 + y1), "X",
                             font=positionFont, fill=(0, 0, 0))

        for i in range(1, 26):
            if i != position:
                x1, y1, x2, y2 = rows[i - 1]
                w, h = background_draw.textsize(f"{i}", font=positionFont)

                background_draw.text(((x2 - x1 - w) / 2 + x1, (y2 - y1 - h) / 2 + y1), f"{i}",
                                     font=positionFont, fill=(0, 0, 0))

        buffer = BytesIO()
        background.save(buffer, "png")
        buffer.seek(0)

        background.show()

    return buffer

class Nodes:
    def __init__(self, node):
        self.Event = 1 if node in eventNodes else 0
        self.EventType = snakeAndLaddersNodes[node][0] if self.Event == 1 else None
        self.MoveTo = snakeAndLaddersNodes[node][1] if self.Event == 1 else None
        self.Question = snakeAndLaddersNodes[node][2] if self.Event == 1 else None
        self.Answer = snakeAndLaddersNodes[node][3] if self.Event == 1 else None
        self.FunFacts = snakeAndLaddersNodes[node][4] if self.Event == 0 else None


# def boardCreation(currentPosition: int = None):
#     rows = [[f'{(n + 1) + (i * 5):4}' if (n + 1) + (i * 5) != currentPosition else f"{'  X':4}" for n in range(5)] for i in range(5)]
#     print(rows)
#     rows = reversed([reversed(rows[i]) if i % 2 else rows[i] for i in range(len(rows))])
#
#     for row in rows:
#         print(' | '.join(row))
#
# boardCreation()

# TODO: Game Logic

Playing = True

stepsTaken = 0
currentNode = 1

while Playing:
    description = 'Please type "roll" to start rolling the dice! Type "end" to end the game.\n'
    description += f"You're currently at Position {currentNode}.\n\n"
    userInput = input(description)

    if userInput.lower() == "end":
        Playing = False
        break

    if currentNode >= 25:
        print(f"Congratulations! You've completed the Snake & Ladders in {stepsTaken} steps.")
        Playing = False
        break

    stepsTaken += 1
    diceRoll = random.choice(range(1, 7))
    currentNode += diceRoll
    nodeObject = Nodes(currentNode)
    boardImage(currentNode)
    eventCheck = nodeObject.Event


    if eventCheck:
        eventType = nodeObject.EventType
        if eventType == "Snake":
            description = f"You've rolled {diceRoll} and moved up {diceRoll} step(s) to Position {currentNode}.\n"
            description += f"Oh no! You've encountered a Snake, now you risk moving downwards unless you get the question correct, in which you " \
                           f"stay at the same position if you do.\n\n"
            description += f"Question: {nodeObject.Question}\n\n"
            answerInput = input(description)

            if answerInput == nodeObject.Answer:
                print("You've answered the question correctly and you will stay at your current position!")
                continue

            currentNode = nodeObject.MoveTo
            boardImage(currentNode)
            print(
                f"Oh no! You've answered the question wrongly and was moved back down to Position {nodeObject.MoveTo}")
            continue

        if eventType == "Ladder":
            description = f"You've rolled {diceRoll} and moved up {diceRoll} step(s) to Position {currentNode}.\n"
            description += f"Yay! You've encountered a Ladder, now you have an opportunity to move upwards unless you get the question wrong, " \
                           f"in which you stay at the same position if you do.\n\n"
            description += f"Question: {nodeObject.Question}\n\n"

            answerInput = input(description)

            if answerInput != nodeObject.Answer:
                print(f"Oh no! You've answered the question wrongly and you will stay at your current position!")
                continue

            currentNode = nodeObject.MoveTo
            boardImage(currentNode)
            print(f"You've answered the question correctly and was moved up to Position {nodeObject.MoveTo}!")
            continue

    print(f"You've rolled {diceRoll} and moved up {diceRoll} step(s) to Position {currentNode}.")

    if nodeObject.FunFacts:
        print(nodeObject.FunFacts)


a = input("Enter any key to exit\n")