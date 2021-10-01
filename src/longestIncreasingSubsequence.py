def longestIncreasingSubsequence(lst):
    lst = [0, 4, 12, 2, 10, 6, 9, 13, 3, 11, 7, 15]
    lens = [1] * len(lst)
    indexs = [0] * len(lst)
    # print(indexs)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[j] < lst[i]:
                lens[i] = max(lens[j] + 1, lens[i])
                indexs[i] = j

    print(lens)
    print(indexs)


if __name__ == '__main__':
    longestIncreasingSubsequence("THis si fas")
