# def solution(skill, skill_trees):
#     answer = 0
#
#     for skills in skill_trees:
#         skill_list = list(skill)
#
#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1
#
#     return answer


def is_pass(skill, skill_tree):
    cur_skill = skill.pop(0)

    for item in skill_tree:
        if item in skill:
            return 0
        if item == cur_skill:
            if not skill:
                break
            cur_skill = skill.pop(0)

    return 1


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        answer += is_pass(list(skill), list(skill_tree))

    return answer


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/30/lessons/49993

    # sample
    # "CBD", ["BACDE", "CBADF", "AECB", "BDA"] -> 2

    # input
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    # solve
    print(solution(skill, skill_trees))
