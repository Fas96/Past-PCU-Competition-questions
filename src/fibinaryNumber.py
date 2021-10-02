def fib(num):
    st = 1
    sec = 2
    res = [0] * num
    res[0] = st
    res[1] = sec
    for i in range(2, num):
        res[i] = st + sec
        st = sec
        sec = res[i - 1] + res[i - 2]

    return res


def soln(num):
    fi = fib(num)
    ls = [i for i in fi if i < num]
    ls = sorted(ls, reverse=True)
    rlt = [0] * len(ls)
    rlt[0] = 1
    for n in range(0, len(ls)):
        if num - ls[n] >= 0:
            rlt[n] = 1
            num -= ls[n]

    print(rlt)


if __name__ == '__main__':
    soln(500)
