from array import *


def adjacentTree(N):
    letRange = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    N = [
        {'b', 'c', 'd', 'e', 'f'},
        {'c', 'e'},
        {'d'},
        {'e'},
        {'f'},
        {'c', 'g', 'h'},
        {'f', 'h'},
        {'f', 'g'}
    ]

    twod = [[0] * len(letRange) for _ in range(len(letRange))]

    for s in range(len(letRange)):
        for b in range(len(letRange)):
            if str(letRange[b]) in N[s]:
                twod[s][b] = 1

    # if weights are given replace 1
    # for the weights of the graph
    #


# quick recursive merge sort
def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]

    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)

    result = []

    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            result.append(lft.pop())
        else:
            result.append(rgt.pop())
    result.reverse()
    return  (lft or rgt) + result


if __name__ == '__main__':
    adjacentTree([])
    print(mergesort([2,0,3,23,-13,34,23]))
