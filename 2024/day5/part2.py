def func(splitUpdate, i):
    for k in range(i, len(splitUpdate)):
        rightOrder = True
        L = splitUpdate.copy()
        L[i], L[k] = L[k], L[i]

        for j in range(len(splitUpdate)):
            now = L[j]
            after = L[j+1:]
                
            for afterPart in after:
                if now not in section1Parsed:
                    rightOrder = False
                    break

                if afterPart not in section1Parsed[now]:
                    rightOrder = False
                    break

            if not rightOrder:
                break
        
        if rightOrder:
            return L
        
        if j > i:
            return func(L, j)
    
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
                    y = func(splitUpdate, i-1)
                    total += int(y[int(len(y) / 2)])
                    break

                if afterPart not in section1Parsed[now]:
                    rightOrder = False
                    y = func(splitUpdate, i-1)
                    total += int(y[int(len(y) / 2)])
                    break
            
            if not rightOrder:
                break
            
    print(total)