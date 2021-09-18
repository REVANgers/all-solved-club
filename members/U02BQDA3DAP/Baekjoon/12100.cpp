#include <iostream>
#include <queue>
#include <iostream>

using namespace std;

int n;
int board[20][20];
int ans;

void makeMove(int type)

{
    queue<int> q;

    switch (type){
    //왼쪽
    case 0:
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j])
                    q.push(board[i][j]);
                board[i][j] = 0;
            }

            int idx = 0;
            while (!q.empty())
            {
                int data = q.front();
                q.pop();
                if (board[i][idx] == 0)
                    board[i][idx] = data;
                else if (board[i][idx] == data)
                {
                    board[i][idx] *= 2;
                    idx++;
                }

                else
                {
                    idx++;
                    board[i][idx] = data;
                }
            }
        }

        break;

    //오른쪽
    case 1:
        for (int i = 0; i < n; i++)
        {
            for (int j = n - 1; j >= 0; j--)
            {
                if (board[i][j])
                    q.push(board[i][j]);
                board[i][j] = 0;
            }
            int idx = n - 1;
            while (!q.empty())
            {
                int data = q.front();
                q.pop();

                if (board[i][idx] == 0)
                    board[i][idx] = data;
                else if (board[i][idx] == data)

                {
                    board[i][idx] *= 2;
                    idx--;
                }

                else
                {
                    idx--;
                    board[i][idx] = data;
                }
            }
        }

        break;

    //위
    case 2:
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[j][i])
                    q.push(board[j][i]);
                board[j][i] = 0;
            }
            int idx = 0;

            while (!q.empty())
            {
                int data = q.front();
                q.pop();

                if (board[idx][i] == 0)
                    board[idx][i] = data;
                else if (board[idx][i] == data)
                {
                    board[idx][i] *= 2;
                    idx++;
                }

                else
                {
                    idx++;
                    board[idx][i] = data;
                }
            }
        }

        break;

    //아래
    case 3:
        for (int i = 0; i < n; i++)
        {
            for (int j = n - 1; j >= 0; j--)
            {
                if (board[j][i])
                    q.push(board[j][i]);
                board[j][i] = 0;
            }
            int idx = n - 1;

            while (!q.empty())
            {
                int data = q.front();
                q.pop();

                if (board[idx][i] == 0)
                    board[idx][i] = data;
                else if (board[idx][i] == data)
                {
                    board[idx][i] *= 2;
                    idx--;
                }

                else
                {
                    idx--;
                    board[idx][i] = data;
                }
            }
        }
        break;
    }

}



void move(int cnt)
{
    if (cnt == 5)
    {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans = max(ans, board[i][j]);
            }
        }
                
        return;
    }

    int copy[20][20];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            copy[i][j] = board[i][j];

    for (int i = 0; i < 4; i++)
    {
        makeMove(i);
        move(cnt + 1);
   
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = copy[i][j];
            }
        }
    }
}


int main(void)
{
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }

    move(0);

    cout << ans;
}