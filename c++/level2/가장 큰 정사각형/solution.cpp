#include <iostream>
#include <vector>
using namespace std;

int dp[1001][1001] = {0};

int solution(vector<vector<int>> board)
{
    int ans = 0;
    int row = board.size();
    int col = board[0].size();
    for (int i = 1; i <= row; ++i)
    {
        for (int j = 1; j <= col; ++j)
        {
            if(board[i-1][j-1] != 0 )
            {
                dp[i][j] = min(dp[i][j-1], min(dp[i-1][j], dp[i-1][j-1])) + 1;
                ans = max(ans, dp[i][j]);
            }
        }
    }
    return ans*ans;
}

int main() {

// url: https://programmers.co.kr/learn/courses/18/lessons/1879'

// sample
// [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]] -> 9
// [[0,0,1,1],[1,1,1,1]] -> 	4

    vector<vector<int> > input_sample = {{0,1,1,1},
                                         {1,1,1,1},
                                         {1,1,1,1},
                                         {0,0,1,0}};

    printf("%d", solution(input_sample));

    return 0;
}