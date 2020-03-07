def solution(priorities, location):

    answer = 0
    locations = [i for i in range(len(priorities))]

    idx = 0
    cnt = 1
    while True:
        max_num = max(priorities)
        if priorities[idx] == max_num:

            if locations[idx] == location:
                answer = cnt
                break

            cnt += 1
            priorities.pop(idx)
            locations.pop(idx)
            idx = idx % len(priorities)

        else:
            idx = (idx + 1) % len(priorities)

    return answer


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/30/lessons/42587

    # input
    priorities = [1,1,9,1,1,1]
    location = 0
    # solve
    print(solution(priorities, location))
