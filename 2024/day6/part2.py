class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

class MapObject(Vector):
    def __init__(self, x, y):
        super().__init__(x, y)

class Guard(MapObject):
    def __init__(self, x, y, direction):
        super().__init__(x, y)
        self.direction = direction
        self.visited = [[x, y, self.direction.x, self.direction.y]]
    
    def move(self, obstacles, empties, width, height):
        while True:
            if [self.x + self.direction.x, self.y + self.direction.y] in obstacles:
                self.direction = Vector(-self.direction.y, self.direction.x)
            else:
                self.x += self.direction.x
                self.y += self.direction.y
                
                if self.x < 0 or self.y < 0 or self.x >= width or self.y >= height:
                    return False

                vec = [self.x, self.y, self.direction.x, self.direction.y]
                
                if vec in self.visited:
                    return True
                
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
                guard = Guard(x, y, Vector(0, -1))

    loops = 0

    i = 0
    j = 0

    for x, y in empties:
        L_obstacles = obstacles.copy()
        L_empties = empties.copy()
        L_guard = Guard(guard.x, guard.y, guard.direction)

        L_obstacles.append([x, y])
        del L_empties[L_empties.index([x, y])]

        if L_guard.move(L_obstacles, L_empties, width, height):
            loops += 1
        
        i += 1
        j += 1
        
        if i >= len(empties) / 1000:
            i -= len(empties) / 1000
            print(j / len(empties) * 100)
        
    print(loops)