class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

DIRECTION_UP = Vector(0, -1)
DIRECTION_LEFT = Vector(-1, 0)
DIRECTION_DOWN = Vector(0, 1)
DIRECTION_RIGHT = Vector(1, 0)

class MapObject(Vector):
    def __init__(self, x, y):
        super().__init__(x, y)

class Guard(MapObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.direction = DIRECTION_UP
        self.visited = [[x, y]]
    
    def move(self, obstacles, empties):
        if [self.x + self.direction.x, self.y + self.direction.y] in obstacles:
            self.direction = Vector(-self.direction.y, self.direction.x)
        else:
            self.x += self.direction.x
            self.y += self.direction.y
            
            vec = [self.x, self.y]
            if vec not in self.visited:
                self.visited.append(vec)

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")

    width = len(lines[0])
    height = len(lines)

    obstacles = []
    empties = []
    guard = None

    for y in range(height):
        for x in range(width):
            if lines[y][x] == "#":
                obstacles.append([x, y])
            elif lines[y][x] == ".":
                empties.append([x, y])
            else:
                guard = Guard(x, y)
    
    while True:
        guard.move(obstacles, empties)
        if guard.x < 0 or guard.y < 0 or guard.x >= width or guard.y >= height:
            break
    
    print(len(guard.visited) - 1)