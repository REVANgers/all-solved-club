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

struct point {
    int x, y;
};

int arr[25][25];
int marked[25][25];
int n;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

int bfs(point start, int num) {
    int count = 0;
    queue<point> q; q.push(start); marked[start.x][start.y] = num;
    while(!q.empty()) {
        point now = q.front(); q.pop();
        count++;
        for(int i=0; i<4; i++){
            int nx = now.x + dx[i];
            int ny = now.y + dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<n) {
                if(arr[nx][ny]==0) continue; // 집이 없다.
                if(marked[nx][ny]!=0) continue; // 이미 다른 단지에 소속되어있다.
                marked[nx][ny]=num;
                q.push(point{nx,ny});          
            }
        }
    }
    return count;
}

void getInput() {
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            scanf("%1d", &arr[i][j]);
        }
    }
}

int main() {
    getInput();
    int num=0;
    vector<int> res;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(arr[i][j]==0) continue;
            if(marked[i][j]!=0) continue;
            int count = 0;
            num++;
            count = bfs(point{i,j}, num);
            res.push_back(count);
        }
    }
    sort(res.begin(), res.end());
    printf("%d\n", num);
    for(auto cnt : res) {
        printf("%d\n", cnt);
    }
    return 0;
}