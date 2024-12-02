import numpy as np

if __name__ == "__main__":
    distances = []

    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")

    Llist = np.ndarray((len(lines)))
    Rlist = np.ndarray((len(lines)))

    for i in range(len(lines)):
        Llist[i], Rlist[i] = lines[i].split("   ")

    Llist.sort()
    Rlist.sort()

    print(np.sum(np.abs(Rlist - Llist)))