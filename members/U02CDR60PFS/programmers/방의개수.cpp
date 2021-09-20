#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;
int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int solution(vector<int> arrows)
{
    int answer = 0;
    map<pair<int, int>, bool> node;
    map<pair<pair<int, int>, pair<int, int>>, bool> edge;

    int x = 0, y = 0;
    node[{x, y}] = true;
    for (int arrow : arrows)
    {
        for (int i = 0; i < 2; i++)
        {
            int nx = x + dx[arrow];
            int ny = y + dy[arrow];

            if (node[{nx, ny}] == true && edge[{{x, y}, {nx, ny}}] == false)
            {
                answer++;
            }
            node[{nx, ny}] = true;
            edge[{{x, y}, {nx, ny}}] = true;
            edge[{{nx, ny}, {x, y}}] = true;
            x = nx;
            y = ny;
        }
    }

    return answer;
}