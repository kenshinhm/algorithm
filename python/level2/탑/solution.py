# def solution(h):
#     ans = [0] * len(h)
#     for i in range(len(h)-1, 0, -1):
#         for j in range(i-1, -1, -1):
#             if h[i] < h[j]:
#                 ans[i] = j+1
#                 break
#     return ans


def solution(heights):
    answer = []

    for i, height in enumerate(heights):

        for j in reversed(range(-1, i)):
            if j == -1:
                answer.append(0)
                break
            if heights[j] > height:
                answer.append(j+1)
                break

    return answer


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/30/lessons/42588

    # sample
    # [6,9,5,7,4]-> [0,0,2,2,4]
    # [3,9,9,3,5,7,2] -> [0,0,0,3,3,3,6]
    # [1,5,3,6,7,6,5] => [0,0,2,0,0,5,6]

    # input
    input_sample = [6, 9, 5, 7, 4]
    # solve
    print(solution(input_sample))
