import math


def solution(n):
    ret = 0

    while n > 0:
        ret += n % 10
        n = math.floor(n/10)

    ret += n

    return ret


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/18/lessons/1876'

    # sample
    # 123 -> 6
    # 987 -> 24

    # input
    input_sample = 123
    # solve
    output = solution(input_sample)
    # output
    print(output)
