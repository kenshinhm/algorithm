#include <iostream>
#include <vector>

using namespace std;

//int N, K;
//int TILES[50][50];

int N = 6;
int K = 0;

int TILES[6][6] = {
        {5, 3, 5, 4, 0, 1},
        {1, 4, 2, 3, 5, 5},
        {0, 3, 0, 5, 5, 1},
        {4, 5, 4, 5, 1, 4},
        {4, 2, 4, 1, 4, 4},
        {2, 5, 3, 0, 2, 2},
};

void input()
{
    std::cin >> N >> K;

    for (int h = 0; h < N; h++)
    {
        for (int w= 0; w < N; w++)
        {
            std::cin >> TILES[h][w];
        }
    }
}

int solve(){


}

int main() {

//    input();

    std::cout << solve();

    return 0;
}