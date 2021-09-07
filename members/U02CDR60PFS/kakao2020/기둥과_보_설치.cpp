#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
bool pillar[102][102];
bool bar[102][102];
bool checkPillar(int x, int y)
{
    if (y == 0 || pillar[y - 1][x])
        return true;
    if ((x > 0 && bar[y][x - 1]) || bar[y][x])
        return true;
    return false;
}

bool checkBar(int x, int y)
{
    if (y > 0 && pillar[y - 1][x] || pillar[y - 1][x + 1])
        return true;
    if (x > 0 && bar[y][x - 1] && bar[y][x + 1])
        return true;
    return false;
}

bool canDelete(int x, int y)
{
    for (int i = max(0, y - 1); i <= y + 1; i++)
    {
        for (int j = max(0, x - 1); j <= x + 1; j++)
        {
            if (pillar[i][j] && !checkPillar(j, i))
                return false;
            if (bar[i][j] && !checkBar(j, i))
                return false;
        }
    }
    return true;
}

vector<vector<int>> solution(int n, vector<vector<int>> build_frame)
{
    vector<vector<int>> answer;
    for (auto build : build_frame)
    {
        int x = build[0], y = build[1];
        int type = build[2], cmd = build[3];
        if (cmd == 1)
        {
            if (type == 0)
            {
                if (checkPillar(x, y))
                    pillar[y][x] = 1;
            }
            else
            {
                if (checkBar(x, y))
                    bar[y][x] = 1;
            }
        }
        else
        {
            if (type == 0)
            {
                pillar[y][x] = 0;
                if (!canDelete(x, y))
                    pillar[y][x] = 1;
            }
            else
            {
                bar[y][x] = 0;
                if (!canDelete(x, y))
                    bar[y][x] = 1;
            }
        }
    }

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (pillar[j][i])
                answer.push_back({i, j, 0});
            if (bar[j][i])
                answer.push_back({i, j, 1});
        }
    }
    return answer;
}