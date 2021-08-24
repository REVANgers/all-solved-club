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

int n, m;
int maze[101][101];
int dist[101][101];

struct point {
    int x, y;
};

void getInput() {
    scanf("%d %d", &n, &m);
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            scanf("%1d", &maze[i][j]);
        }
    }   
}

void bfs() {
    int dx[] = {0,1,0,-1};
    int dy[] = {1,0,-1,0};
    
    point start{1,1};
    dist[1][1] = 1;
    queue<point> q; q.push(start);
    while(!q.empty()) {
        point now = q.front(); q.pop();
        for(int i = 0; i < 4; i++){
            int nx = now.x + dx[i];
            int ny = now.y + dy[i];
            if(0<nx && nx<=n && 0<ny && ny<=m) {
                if( maze[nx][ny] == 0 ) continue;
                if( dist[nx][ny] > 0 ) continue;
                dist[nx][ny] = dist[now.x][now.y] + 1;
                q.push(point{nx, ny});
            }
        }
    }
}

void print() {
    for(int i=1; i<n; i++){
        for(int j=1; j<m; j++){
            printf("%d ", dist[i][j]);
        }
        printf("\n");
    }
}

int main() {
    getInput();
    bfs();
    printf("%d", dist[n][m]);
    return 0;
}