# def hopscotch(board, size):
#     for i in range(size):
#         if i == size - 1:
#             return max(board[i])
#         for j in range(4):
#             # print j, board[i][:j] + board[i][j + 1:]
#             board[i + 1][j] += max(board[i][:j] + board[i][j + 1:])


def solution(land):

    dp = [[0, 0, 0, 0] for _ in range(len(land))]

    dp[0] = land[0]

    for y in range(1, len(land)):
        for x in range(0, 4):
            for k in range(0, 4):
                if k != x:
                    dp[y][x] = max(dp[y][x], land[y][x]+dp[y-1][k])

    return max(dp[-1])


if __name__ == "__main__":
    # url: #

    # input
    input_sample = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
    # solve
    solution(input_sample)
    # print(solution(input_sample))
