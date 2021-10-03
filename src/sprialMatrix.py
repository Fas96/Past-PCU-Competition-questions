def spiralMatrix(siz):
    res = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    ap = []
    if len(res) == 0: return res

    top, bottom = 0, len(res)
    left, right = 0, len(res[0])

    while top <= bottom and left <= right:
        for i in range(left, right):
            ap.append(res[top][i])
        top += 1

        for i in range(top, bottom):
            ap.append(res[i][right - 1])
        right -= 1

        if not (top < bottom and left < right):
            break

        for i in range(right - 1, left - 1, -1):
            ap.append(res[bottom - 1][i])
        bottom -= 1

        for i in range(bottom-1, top - 1, -1):
            ap.append(res[i][left])
        left += 1

    print(ap)


if __name__ == '__main__':
    spiralMatrix(4)
