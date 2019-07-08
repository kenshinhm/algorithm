import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

def solution(participant, completion):

    answer = ''

    participant.sort()
    completion.sort()

    for i, item in enumerate(participant):
        if i == len(participant)-1:
            answer = item
            break

        if item is not completion[i]:
            answer = item
            break

    return answer


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/30/lessons/42576'

    # sample
    # [mislav, stanko, mislav, ana] / [stanko, ana, mislav] -> 'mislav'
    # [leo, kiki, eden] / [eden, kiki] -> 'leo'

    # input
    participant = ['leo', 'kiki', 'eden']
    completion = ['eden', 'kiki']

    # output
    print(solution(participant, completion))
