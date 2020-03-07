# def solution(A, B):
#     return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))


def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        answer += a*b

    return answer


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/30/lessons/12941

    # sample
    # A: [1, 4, 2], B: [5, 4, 4] => 29
    # A: [1, 2], B: [3, 4] => 10

    # input
    A = [1, 4, 2]
    B = [5, 4, 4]
    # solve
    print(solution(A, B))
