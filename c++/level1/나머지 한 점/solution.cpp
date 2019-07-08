#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<vector<int> > v)
{
    vector<int> ans = {0,0};

    for(int i=0; i<3; i++)
    {
        ans[0] ^= v[i][0];
        ans[1] ^= v[i][1];
    }
    return ans;
}

int main() {

// url: https://programmers.co.kr/learn/courses/18/lessons/1878'

// sample
// [[1, 4], [3, 4], [3, 10]] -> [1, 10]
// [[1, 1], [2, 2], [1, 2]] -> [2, 1]

    vector<vector<int> > input_sample = {{1,4},
                                         {3,4},
                                         {3,10}};

    vector<int> output = solve(input_sample);

    printf("[%d, %d]", output[0], output[1]);

    return 0;
}