import re

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get(lines, x, y, width, height):
    if x < 0 or x >= width or y < 0 or y >= height:
        return None
    
    return lines[y][x]

def checkA(lines, width, height, posVector):
    return \
        get(lines, posVector.x - 1, posVector.y - 1, width, height) == "M" and get(lines, posVector.x + 1, posVector.y + 1, width, height) == "S" and \
        get(lines, posVector.x - 1, posVector.y + 1, width, height) == "M" and get(lines, posVector.x + 1, posVector.y - 1, width, height) == "S"

def checkB(lines, width, height, posVector):
    return \
        get(lines, posVector.x - 1, posVector.y - 1, width, height) == "M" and get(lines, posVector.x + 1, posVector.y + 1, width, height) == "S" and \
        get(lines, posVector.x - 1, posVector.y + 1, width, height) == "S" and get(lines, posVector.x + 1, posVector.y - 1, width, height) == "M"

def checkC(lines, width, height, posVector):
    return \
        get(lines, posVector.x - 1, posVector.y - 1, width, height) == "S" and get(lines, posVector.x + 1, posVector.y + 1, width, height) == "M" and \
        get(lines, posVector.x - 1, posVector.y + 1, width, height) == "M" and get(lines, posVector.x + 1, posVector.y - 1, width, height) == "S"

def checkD(lines, width, height, posVector):
    return \
        get(lines, posVector.x - 1, posVector.y - 1, width, height) == "S" and get(lines, posVector.x + 1, posVector.y + 1, width, height) == "M" and \
        get(lines, posVector.x - 1, posVector.y + 1, width, height) == "S" and get(lines, posVector.x + 1, posVector.y - 1, width, height) == "M"

def check(lines, width, height, posVector):
    return \
        checkA(lines, width, height, posVector) or \
        checkB(lines, width, height, posVector) or \
        checkC(lines, width, height, posVector) or \
        checkD(lines, width, height, posVector)

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")
    width = len(lines[0])
    height = len(lines)

    total = 0

    for y in range(height):
        for x in range(width):
            if lines[y][x] == "A":
                posVector = Vector2(x, y)

                total += check(lines, width, height, posVector)
    
    print(total)