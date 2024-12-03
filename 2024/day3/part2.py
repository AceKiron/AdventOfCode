import re

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    total = 0
    enabled = True

    for expr in re.findall("(don\'t\(\)|do\(\)|mul\(\d+,\d+\))", raw):
        if expr == "don't()":
            enabled = False
        elif expr == "do()":
            enabled = True
        elif enabled:
            L, R = re.findall("\d+", expr)
            total += int(L) * int(R)
    
    print(total)