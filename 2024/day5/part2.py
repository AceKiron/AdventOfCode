def func(splitUpdate, m, l):
    for i in range(m, l):
        for j in range(i+1, l):
            L = splitUpdate.copy()
            L[i], L[j] = L[j], L[i]

            rightOrderFound = True

            for k in range(l):
                now = L[k]
                after = L[k+1:]
                
                for afterPart in after:
                    if now not in section1Parsed:
                        rightOrderFound = False
                        break

                    if afterPart not in section1Parsed[now]:
                        rightOrderFound = False
                        break
            
                if not rightOrderFound:
                    break
            
            if rightOrderFound:
                return L, True
            
            y = func(L, i+1, l)
            if y[1]:
                return y

    return None, False

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = file.read()
    file.close()

    lines = raw.split("\n")

    splitIndex = lines.index("")

    section1 = lines[:splitIndex]
    section2 = lines[splitIndex+1:]

    section1Parsed = {}

    for pageOrderingRule in section1:
        key, value = pageOrderingRule.split("|")
        
        if key in section1Parsed:
            section1Parsed[key].append(value)
        else:
            section1Parsed[key] = [value]

    total = 0

    for update in section2:
        splitUpdate = update.split(",")

        rightOrder = True

        for i in range(len(splitUpdate)):
            now = splitUpdate[i]
            after = splitUpdate[i+1:]
            
            for afterPart in after:
                if now not in section1Parsed:
                    rightOrder = False
                    break

                if afterPart not in section1Parsed[now]:
                    rightOrder = False
                    break
            
            if not rightOrder:
                L, _ = func(splitUpdate, 0, len(splitUpdate))
                total += int(L[int(len(L) / 2)])
                break
        
    print(total)