import numpy as np

if __name__ == "__main__":
    safeCount = 0

    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")

    for line in lines:
        split = line.split(" ")

        L = np.array([int(split[i]) - int(split[i - 1]) for i in range(1, len(split))])
        
        if np.sign(int(split[1]) - int(split[0])) == -1:
            # Decreasing
            safeCount += not np.any(False == np.logical_and(L <= -1, L >= -3))
        elif np.sign(int(split[1]) - int(split[0])) == 1:
            # Increasing
            safeCount += not np.any(False == np.logical_and(L >= 1, L <= 3))
        
    print(safeCount)