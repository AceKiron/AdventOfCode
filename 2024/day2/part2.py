import numpy as np

def advanced(split):
    for i in range(len(split)):
        L = split.copy()
        del L[i]
        
        R = np.array([int(L[j]) - int(L[j - 1]) for j in range(1, len(L))])

        if np.sign(int(L[1]) - int(L[0])) == -1:
            # Decreasing
            if not np.any(False == np.logical_and(R <= -1, R >= -3)):
                return True
        elif np.sign(int(L[1]) - int(L[0])) == 1:
            # Increasing
            if not np.any(False == np.logical_and(R >= 1, R <= 3)):
                return True
    
    return False

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
            if np.any(False == np.logical_and(L <= -1, L >= -3)):
                safeCount += advanced(split)
            else:
                safeCount += 1
        elif np.sign(int(split[1]) - int(split[0])) == 1:
            # Increasing
            if np.any(False == np.logical_and(L >= 1, L <= 3)):
                safeCount += advanced(split)
            else:
                safeCount += 1
        else:
            safeCount += advanced(split)

    print(safeCount)