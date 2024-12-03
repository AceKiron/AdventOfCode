import re

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    total = 0

    for expr in re.findall("mul\(\d+,\d+\)", raw):
        L, R = re.findall("\d+", expr)
        total += int(L) * int(R)
    
    print(total)