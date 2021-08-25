#include <bits/stdc++.h>
#define endl "\n"
#define __usecin__ ios_base::sync_with_stdio(false); cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
// 1억:1e8
// int_max = 2^31-1 ~= 2.1e9
// llong_max = 2^63-1
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<pair<int, int> > vpii;

struct tomato {
    int x, y, z;
};

int m, n, h; // m: 가로[2,100], n: 세로[2,100], h: 높이[1,100]
int box[101][101][101];  // 세로, 가로, 높이
int day[101][101][101];  // 세로, 가로, 높이
queue<tomato> q;

void getInput() {
    bool alreadyDone = true;
    scanf("%d %d %d", &m, &n, &h);
    for(int hei=0; hei<h; hei++){
        for(int row=0; row<n; row++){
            for(int col=0; col<m; col++){
                scanf("%d", &box[row][col][hei]);
                if(box[row][col][hei] == 1) { q.push(tomato{row,col,hei}); alreadyDone = false; }
                else if(box[row][col][hei] == 0) { day[row][col][hei] = -1; }
            }
        }
    }
}

int bfs() {
    int dx[] = {0, 0, 1, 0, -1, 0};
    int dy[] = {0, 1, 0, -1, 0, 0};
    int dz[] = {1, 0, 0, 0, 0, -1};

    int res = 0;
    while(!q.empty()) {
        auto now = q.front(); q.pop(); 
        for(int i=0; i<6; i++){
            int nx = now.x + dx[i];
            int ny = now.y + dy[i];
            int nz = now.z + dz[i];
            if(0<=nx && nx<n && 0<=ny && ny<m && 0<=nz && nz<h) {
                if(box[nx][ny][nz] != 0) continue;
                if(day[nx][ny][nz] > 0) continue;
                day[nx][ny][nz] = day[now.x][now.y][now.z] + 1;
                res = max(res, day[nx][ny][nz]);
                q.push(tomato{nx,ny,nz});
            }
        }
    }
    return res;
}

bool checkup() {
    for(int hei=0; hei<h; hei++){
        for(int row=0; row<n; row++){
            for(int col=0; col<m; col++){
                if(day[row][col][hei] == -1) return false;
            }
        }
    }
    return true;
}

/*
    모든 토마토를 순회하면서 익은 토마토는 queue에넣는다. -> 입력을 받을 때 바로 넣으면 한 단계 단축.
    순회가 끝나면 한번에 bfs를 돌린다.
*/
int main() {
    getInput();
    int res = bfs();
    if(checkup() == false) res = -1;
    printf("%d", res);
    return 0;
}