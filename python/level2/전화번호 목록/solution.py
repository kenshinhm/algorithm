# from itertools import combinations as c
#
# def solution(phoneBook):
#     answer = True
#     sortedPB = sorted(phoneBook, key=len)
#     for (a, b) in c(sortedPB, 2):
#         if a == b[:len(a)]:
#             answer = False
#     return answer


def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book, key=lambda x: len(x))
    phone_dict = {}

    for item in phone_book:
        for idx in range(len(item) + 1):
            if item[:idx] in phone_dict:
                answer = False
                break

        phone_dict[item] = 1

    return answer


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/30/lessons/42577

    # sample
    # ['119', '97674223', '1195524421'] -> false
    # ['123', '456', '789'] -> true
    # ['12', '123', '1235', '567', '88'] => false

    # input
    input_sample = ['119', '97674223', '1195524421']
    # solve
    print(solution(input_sample))
