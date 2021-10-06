def matrixMul(matA, matB, sze):
    res = [[]]

    if sze < 2:
        pass
    else:
        sze /= 2
        matrixMul(matA[1][1], matB[1][1], sze) + matrixMul(matA[1][2], matB[2][1], sze)
        matrixMul(matA[1][1], matB[1][2], sze) + matrixMul(matA[1][2], matB[2][2], sze)
        matrixMul(matA[2][1], matB[1][1], sze) + matrixMul(matA[2][2], matB[2][1], sze)
        matrixMul(matA[2][1], matB[1][2], sze) + matrixMul(matA[2][2], matB[2][2], sze)


if __name__ == '__main__':
    matA = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    matB = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    
    sze = 4
    matrixMul(matA, matB, sze)
