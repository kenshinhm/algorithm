def solution(arr):
    answer = True

    # arr = [0] * 100
    arr.sort()

    for i in range(1, len(arr)+1):
        if i != arr[i-1]:
            answer = False
            break

    return answer


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/18/lessons/1877'

    # sample
    # [4,1,3,2] -> true
    # [4,1,3] -> false

    # input
    input_sample = [4, 1, 3, 2]
    # solve
    output = solution(input_sample)
    # output
    print(output)
