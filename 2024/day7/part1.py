def func2(l0, oper, l1, r):
    return (l0 + l1 if oper else l0 * l1)

def func3(L, result, oper, i, r):
    if i >= len(L):
        return False

    y = func2(result, oper, L[i], r)
    return y == r or func3(L, y, False, i+1, r) or func3(L, y, True, i+1, r)

def func(L, r):
    return func3(L, L[0], False, 1, r) or func3(L, L[0], True, 1, r)

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")

    total = 0

    for line in lines:
        r, L = line.split(": ")
        L2 = list(map(int, L.split(" ")))
        r2 = int(r)

        if func(L2, r2):
            total += r2

    print(total)