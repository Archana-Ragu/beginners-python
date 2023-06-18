def findMin(L, startIndx):
    m = L[startIndx]
    idx = startIndx
    for i in range(startIndx, len(L)):
        x = L[i]
        if x < m:
            m = x
            idx = i
    return m, idx

print(findMin([-2, -3], 0))
