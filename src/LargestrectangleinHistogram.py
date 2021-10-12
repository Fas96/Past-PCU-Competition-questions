def LargestrectangleinHistogram(arr):
    arr = [8, 2, 6, 9, 7, 2]
    mx = -1 * 10 ** 10
    for i in range(len(arr)):
        for j in range(i, len(arr)):

            H = min(arr[i:j + 1])
            W = j - i + 1
            mx = max(mx, H * W)

    return mx


if __name__ == '__main__':
    print(LargestrectangleinHistogram([]))
