def largestRectAreaHistogram(arr):
    arr = [8, 2, 6, 9, 7, 2]
    stk, mx = [], -1 * 10 ** 9

    for i, val in enumerate(arr + [0]):
        while stk and arr[stk[-1]] > val:
            H = arr[stk.pop()]
            if not stk:
                W = i
            else:
                W = i - stk[-1] - 1
            mx = max(mx, W * H)

        stk.append(i)
    return mx


if __name__ == '__main__':
    print(largestRectAreaHistogram([]))
