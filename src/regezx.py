import  re
class Test:
    def numbers(n):
        te="지각된 가치와 만족도 태도 행동의도 관계에 관련한 대부분의 연구에서는 지각된 가치가 만족도 태도 행동의도에 유의한 영향을 미치는 것으로 나타났다[3][4][5][8][9][18][19][23][25][28][31][38][42][43][51]."
        t1="맥과이어(MｃGuire)는 노인에 대한 편견과 인식이 12-13세까지 형성되어 가는데 한번 형성된 인식은 보다 긍정적으로 변화되기 어렵기 때문에 아동의 노인에 대한 인식형성기는 매우 중요하다고 하였다[33]."
        t2="그리고 대인관계의 장애 등을 유발한다고 하였다[22-33]다."
        sentence="These findings were consistent with those in [41] for the KOSDAQ listed firms and in [42] for the U.S.[12-12]사용하였다."
        return re.search(n,sentence)


if __name__ == '__main__':
    print(Test.numbers("[\-.\d+]|\[.\d+]$"))
    print(Test.numbers("\d+]$"))
    print(Test.numbers("\d+]$"))
    print(Test.numbers("^.+(\\다\\.)$"))
    print(Test.numbers("^.+(\\다.)$"))
    print(Test.numbers("^.+(\\d+]\\.)$"))
    print(Test.numbers("^.+(\\d+]\\.)$") )