# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]


import math


def solution(progresses, speeds):

    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]

    min_day = days[0]
    count = 0
    answer = []
    for day in days:
        if day <= min_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            min_day = day

    answer.append(count)
    return answer


if __name__ == "__main__":
    # https://programmers.co.kr/learn/courses/30/lessons/42586

    # sample
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]

    # solve
    print(solution(progresses, speeds))
