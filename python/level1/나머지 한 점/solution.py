def solution(arr):

    x_array = [x[0] for x in arr]
    y_array = [x[1] for x in arr]

    for x in x_array:
        if x_array.count(x) == 1:
            ret_x = x

    for y in y_array:
        if y_array.count(y) == 1:
            ret_y = y

    return [ret_x, ret_y]


if __name__ == "__main__":
    # url: https://programmers.co.kr/learn/courses/18/lessons/1878'

    # sample
    # [[1, 4], [3, 4], [3, 10]] -> [1, 10]
    # [[1, 1], [2, 2], [1, 2]] -> [2, 1]

    # input
    input_sample = [[1, 4], [3, 4], [3, 10]]
    # solve
    output = solution(input_sample)
    # output
    print(output)
