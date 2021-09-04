// 나는 for문으로 모든 조건을 고려해주었다. (거리 2 이하인 가로,세로, 대각선)
// bfs로 짜는게 더 깔끔할 것 같다.
#include <string>
#include <vector>
#include <iostream>
using namespace std;
int checkAround(vector<string> place, int r, int c)
{
    int d[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
    for (int i = 0; i < 4; i++)
    {
        for (int j = 1; j <= 2; j++)
        {
            int nr = r + j * d[i][0];
            int nc = c + j * d[i][1];

            if (nr < 0 || nr > 4 || nc < 0 || nc > 4)
                break;

            if (j == 1)
            {
                if (place[nr][nc] == 'P')
                    return 0;
            }
            else
            {
                if (place[nr][nc] == 'P' && place[nr - d[i][0]][nc - d[i][1]] == 'O')
                    return 0;
            }
        }
    }

    for (int i = 4; i < 8; i++)
    {
        int nr = r + d[i][0];
        int nc = c + d[i][1];

        if (nr < 0 || nr > 4 || nc < 0 || nc > 4)
            continue;

        if (place[nr][nc] == 'P' && (place[r + d[i][0]][c] != 'X' || place[r][c + d[i][1]] != 'X'))
            return 0;
    }

    return 1;
}

int check(vector<string> place)
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (place[i][j] == 'P')
            {
                int rst = checkAround(place, i, j);
                if (rst == 0)
                    return 0;
            }
        }
    }
    return 1;
}

vector<int> solution(vector<vector<string>> places)
{
    vector<int> answer;
    for (int i = 0; i < places.size(); i++)
        answer.push_back(check(places[i]));

    return answer;
}