if __name__ == "__main__":
    total = 0

    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")

    Llist = []
    Rlist = []

    for i in range(len(lines)):
        L, R = lines[i].split("   ")
        Llist.append(int(L))
        Rlist.append(int(R))
    
    for L in Llist:
        total += L * Rlist.count(L)
    
    print(total)