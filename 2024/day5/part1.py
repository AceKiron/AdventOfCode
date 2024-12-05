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
        
        if rightOrder:
            total += int(splitUpdate[int(len(splitUpdate) / 2)])
        
    print(total)