# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result


def solution(answers):

    problem_num = len(answers)
    first_answer = ([1, 2, 3, 4, 5] * problem_num)[0:problem_num]
    second_answer = ([2, 1, 2, 3, 2, 4, 2, 5] * problem_num)[0:problem_num]
    third_answer = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * problem_num)[0:problem_num]

    correct_cnt = {1: 0, 2: 0, 3: 0}

    for i, answer in enumerate(answers):
        correct_cnt[1] = correct_cnt[1] + 1 if answer == first_answer[i] else correct_cnt[1]
        correct_cnt[2] = correct_cnt[2] + 1 if answer == second_answer[i] else correct_cnt[2]
        correct_cnt[3] = correct_cnt[3] + 1 if answer == third_answer[i] else correct_cnt[3]

    sort_correct_cnt = sorted(correct_cnt.items(), key=lambda x: x[1], reverse=True)
    max_val = sort_correct_cnt[0][1]
    ret = [item[0] for item in sort_correct_cnt if item[1] == max_val]

    return ret


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/30/lessons/42840'

    # sample
    # [1,2,3,4,5] -> [1]
    # [1,3,2,4,2] -> [1,2,3]

    # input
    answers = [1,2,3,4,5]

    # output
    print(solution(answers))
