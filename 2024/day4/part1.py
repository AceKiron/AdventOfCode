import re

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get(lines, x, y, width, height):
    if x < 0 or x >= width or y < 0 or y >= height:
        return None
    
    return lines[y][x]

def check(lines, width, height, posVector, moveVector):
    return \
        get(lines, posVector.x + moveVector.x, posVector.y + moveVector.y, width, height) == "M" and \
        get(lines, posVector.x + moveVector.x * 2, posVector.y + moveVector.y * 2, width, height) == "A" and \
        get(lines, posVector.x + moveVector.x * 3, posVector.y + moveVector.y * 3, width, height) == "S"

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
            if lines[y][x] == "X":
                posVector = Vector2(x, y)

                total += check(lines, width, height, posVector, Vector2(-1, -1))
                total += check(lines, width, height, posVector, Vector2(0, -1))
                total += check(lines, width, height, posVector, Vector2(1, -1))

                total += check(lines, width, height, posVector, Vector2(-1, 0))
                total += check(lines, width, height, posVector, Vector2(1, 0))

                total += check(lines, width, height, posVector, Vector2(-1, 1))
                total += check(lines, width, height, posVector, Vector2(0, 1))
                total += check(lines, width, height, posVector, Vector2(1, 1))
    
    print(total)