# from fractions import gcd
#
#
# def nlcm(num):
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)
#
#     return answer

def solution(arr):

    answer = 1
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

    while True:
        finish=True
        for prime in primes:
            tmp = [item % prime for item in arr]

            if tmp.count(0) > 1:
                finish = False
                answer *= prime
                for i, tmp_item in enumerate(tmp):
                    if tmp_item == 0:
                        arr[i] = int(arr[i]/prime)
                break

        # return
        if finish:
            result = 1
            for x in arr:
                result = result * x

            return answer * result


if __name__ == "__main__":
    # url: #

    # input
    input_sample = [2, 6, 8, 14]
    # input_sample = [2,4,9]
    # solve
    print(solution(input_sample))
    # print(solution(input_sample))
