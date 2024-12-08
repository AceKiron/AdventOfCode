class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")

    height = len(lines)
    width = len(lines[0])

    antinodeVectors = []

    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        nodeVectors = []

        for y in range(height):
            for x in range(width):
                if lines[y][x] == char:
                    nodeVectors.append(Vector(x, y))
        
        for i in range(len(nodeVectors)):
            for j in range(i + 1, len(nodeVectors)):
                delta = nodeVectors[j] - nodeVectors[i]

                pos1 = nodeVectors[i] - delta
                pos2 = nodeVectors[j] + delta

                if pos1.x >= 0 and pos1.y >= 0 and pos1.x < width and pos1.y < height:
                    if (pos1.x, pos1.y) not in antinodeVectors:
                        antinodeVectors.append((pos1.x, pos1.y))

                if pos2.x >= 0 and pos2.y >= 0 and pos2.x < width and pos2.y < height:
                    if (pos2.x, pos2.y) not in antinodeVectors:
                        antinodeVectors.append((pos2.x, pos2.y))

    print(len(antinodeVectors))