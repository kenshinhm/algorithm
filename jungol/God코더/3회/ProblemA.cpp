#include <iostream>
#include <vector>

using namespace std;

int N;
char BALLS[500000];

//int N = 8;
//char BALLS[100] = {"BBRBBBBR"};


int forward(char color_move, char color_stay)
{
    int answer = 999999999;
    int start_idx = -1;

    for (int i = 0; i < N; i++)
    {
        if (BALLS[i] == color_stay)
        {
            start_idx = i;
            break;
        }
    }

    if(start_idx >= 0)
    {
        answer = 0;
        for (int i = start_idx; i < N; i++)
        {
            if (BALLS[i] == color_move) {
                answer = answer + 1;
            }
        }
    }

    return answer;
}


int backward(char color_move, char color_stay)
{
    int answer = 999999999;
    int start_idx = -1;

    for (int i = N-1; i >= 0; i--)
    {
        if (BALLS[i] == color_stay)
        {
            start_idx = i;
            break;
        }
    }

    if(start_idx >= 0)
    {
        answer = 0;
        for (int i = start_idx; i >= 0; i--)
        {
            if (BALLS[i] == color_move) {
                answer = answer + 1;
            }
        }
    }

    return answer;
}


int main() {

    std::cin >> N;

    for (int i = 0; i < N; i++) {
        std::cin >> BALLS[i];
    }

    int answer = std::min(std::min(forward('R', 'B'), forward('B', 'R')),
                         std::min(backward('R', 'B'), backward('B', 'R')));

    std::cout << answer;

    return 0;
}