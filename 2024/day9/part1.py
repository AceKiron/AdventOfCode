import numpy as np

if __name__ == "__main__":
    file = open("data.txt", "r")
    raw = [np.int64(i) for i in file.read()]
    file.close()

    blocks = np.zeros(np.sum(raw), dtype=np.uint64)

    spare = []
    add = 0
    
    for x, size in enumerate(raw):
        if x % 2:
            if size:
                spare.extend(range(add, add + size))
        else:
            fileId = np.floor(x / 2)
            blocks[add:add + size] = fileId
        
        add += size

    rdPtr = len(blocks) - 1
    wrPtr = spare.pop(0)

    while rdPtr > wrPtr:
        blocks[wrPtr], blocks[rdPtr] = blocks[rdPtr], 0

        wrPtr = spare.pop(0)
        rdPtr -= 1

        while rdPtr > wrPtr and blocks[rdPtr] == 0:
            rdPtr -= 1
        
    print(np.sum(np.fromiter((x * val for x, val in enumerate(blocks)), dtype=np.uint64)))