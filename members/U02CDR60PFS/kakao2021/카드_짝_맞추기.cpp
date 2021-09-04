#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
vector<vector<int>> Board;
int INF = 100000000;

struct Point
{
    int r, c;
};

int bfs(Point s, Point e)
{
    int d[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    bool visited[4][4] = {
        false,
    };
    visited[s.r][s.c] = true;
    queue<pair<Point, int>> q;
    q.push({s, 0});

    while (!q.empty())
    {
        Point cur = q.front().first;
        int dist = q.front().second;
        q.pop();
        if (cur.r == e.r && cur.c == e.c)
        {
            return dist;
        }

        for (int i = 0; i < 4; i++)
        {
            int nr = cur.r + d[i][0];
            int nc = cur.c + d[i][1];

            if (nr < 0 || nr > 3 || nc < 0 || nc > 3)
                continue;
            if (!visited[nr][nc])
            {
                visited[nr][nc] = true;
                q.push({{nr, nc}, dist + 1});
            }

            for (int j = 0; j < 2; j++)
            {
                if (Board[nr][nc])
                    break;
                if (nr + d[i][0] < 0 || nr + d[i][0] > 3 || nc + d[i][1] < 0 || nc + d[i][1] > 3)
                    break;

                nr += d[i][0];
                nc += d[i][1];
            }

            if (!visited[nr][nc])
            {
                visited[nr][nc] = true;
                q.push({{nr, nc}, dist + 1});
            }
        }
    }
}

int permutate(Point p)
{ // 어떤 순서로 지울까
    int ret = INF;
    for (int k = 1; k <= 6; k++)
    {
        vector<Point> card;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (Board[i][j] == k)
                {
                    card.push_back({i, j});
                }
            }
        }

        if (card.empty())
            continue;

        int dist1 = bfs(p, card[0]) + bfs(card[0], card[1]) + 2;
        int dist2 = bfs(p, card[1]) + bfs(card[1], card[0]) + 2;

        Board[card[0].r][card[0].c] = 0, Board[card[1].r][card[1].c] = 0;

        ret = min(ret, permutate(card[1]) + dist1);
        ret = min(ret, permutate(card[0]) + dist2);

        Board[card[0].r][card[0].c] = k, Board[card[1].r][card[1].c] = k;
    }
    if (ret == INF)
        return 0;
    return ret;
}

int solution(vector<vector<int>> board, int r, int c)
{
    int answer = 0;
    Board = board;

    return permutate({r, c});
}