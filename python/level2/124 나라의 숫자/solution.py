# def change124(n):
#     if n<=3:
#         return '124'[n-1]
#     else:
#         q, r = divmod(n-1, 3)
#         return change124(q) + '124'[r]


def solution(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


if __name__ == "__main__":
    # https://programmers.co.kr/learn/courses/30/lessons/12899

    # sample
    # 4 -> 11
    # 7 -> 21
    # 13 -> 111
    # 20 -> 142

    # input
    # solve
    print(solution(12))
