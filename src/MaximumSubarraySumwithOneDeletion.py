def MaximumSubarraySumwithOneDeletion(arr) -> int:
    mx = -1 * (10 ** 9)
    lmx = arr[0]

    for i in range(1,len(arr)):
        mx = max(arr[i], mx + lmx)
        mx = max(arr[i], mx + lmx)
        if lmx > mx:
            mx = lmx
    return mx


if __name__ == '__main__':
    print(MaximumSubarraySumwithOneDeletion([1, -2, 0, 3]))
