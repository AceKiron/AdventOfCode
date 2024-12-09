import numpy as np

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = [np.int64(i) for i in file.read()]
    file.close()

    blocks = np.zeros(np.sum(raw), dtype=np.uint64)

    files = []
    spare = []
    add = 0

    for x, size in enumerate(raw):
        if x % 2:
            if size:
                spare.append((add, size))
        else:
            fileId = np.floor(x / 2)
            files.append((fileId, add, size))
        
        add += size

    filePtr = len(files) - 1

    while filePtr > 0:
        fileId, add, size = files[filePtr]

        relocate = False
        
        for x, (start, length) in enumerate(spare):
            if length >= size and start < add:
                relocate = True
                break
        
        if relocate:
            files[filePtr] = (fileId, start, size)
            
            if size == length:
                spare.pop(x)
            else:
                spare[x] = (start + size, length - size)
            
        filePtr -= 1
    
    for fileId, add, size in files:
        blocks[add:add + size] = fileId
    
    print(np.sum(np.fromiter((x * val for x, val in enumerate(blocks)), dtype=np.uint64)))