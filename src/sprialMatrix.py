def spiralMatrix(siz):
    res = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

    if siz == 0: return res

    rowBegin, colBegin = 0, 0
    rowEnd, colEnd = len(res)-1, len(res[0])-1
    num = 0

    while rowBegin <= rowEnd and colBegin <= colEnd:
        
        for a in range(colBegin, colEnd+1):
            num += 1
            res[rowBegin][a] = num
        rowBegin += 1
        num += 1
        # loop the last end columns
        for a in range(rowBegin, rowEnd+1):
            num += 1
            res[a][colEnd] = num
        colEnd -= 1
        num += 1

        if rowBegin <= rowEnd:
            for i in range(colEnd, colBegin - 1, -1):
                num += 1
                res[rowEnd][i] = num
                
        rowEnd -= 1
        num += 1
     
        if colBegin <= colEnd:
            for i in range(rowBegin, rowEnd - 1, -1):
                num += 1
                res[i][colBegin] = num
        colBegin += 1
        num += 1

    print(res)


if __name__ == '__main__':
    spiralMatrix(4)
