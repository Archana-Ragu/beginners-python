def findMin(L, startIndx):
    m = L[startIndx]
    idx = startIndx
    for i in range(startIndx, len(L)):
        x = L[i]
        if x < m:
            m = x
            idx = i
    return m, idx

def swapValues(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

def sortList(L):
    if not(checkIfNotNumeric(L)):
        print("Error: list does not contain numeric values" )
        return
    else:
        c = 0
        for x in L:
            m, idx = findMin(L, c)
            L = swapValues(L, c, idx)
            c += 1
    return L

L2 = sortList([2, 1, 5, 3, -8, 17])
print(L2)
