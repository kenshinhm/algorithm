def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        if prices[i+1] < prices[i]:
            answer.append(1)
        else:
            for j in range(i, len(prices)):
                if prices[j] < prices[i]:
                    break
            answer.append(j - i)

    answer.append(0)
    return answer

if __name__ == "__main__":
    # https://programmers.co.kr/learn/courses/30/lessons/42584

    # input
    prices = [1, 2, 3, 2, 3]
    # solve -> [4, 3, 1, 1, 0]
    print(solution(prices))

