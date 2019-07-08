#include <iostream>
#include <vector>

using namespace std;

int solution(vector<vector<int> > land)
{
    int answer = 0;

    int row = (int)land.size();

    //init
    vector<vector<int> > dp(row, vector<int>(4,0));
    for(int x = 0 ; x < 4 ; x++)
        dp[row-1][x]= land[row-1][x];

    for(int y = row-2 ; y >=0 ; y--)
    {
        for(int x = 0 ; x < 4 ; x++)
        {
            //
            int tmp = dp[y+1][x];
            dp[y+1][x] = 0;

            //
            dp[y][x] = max(land[y][x]+dp[y+1][0], land[y][x]+dp[y+1][1]);
            dp[y][x] = max(dp[y][x], land[y][x]+dp[y+1][2]);
            dp[y][x] = max(dp[y][x], land[y][x]+dp[y+1][3]);

            //
            dp[y+1][x] = tmp;
        }
    }

    for(int x = 0 ; x < 4 ; x++)
        answer = max(answer, dp[0][x]);

    return answer;
}

int main() {

// url: https://programmers.co.kr/learn/courses/18/lessons/1880

    vector<vector<int> > land = {{1,2,3,5},
                                 {5,6,7,8},
                                 {4,3,2,1}};

    printf("%d", solution(land));

    return 0;
}