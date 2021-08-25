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

int n, x, y; // n: 전체사람수, x, y: 촌수를 계산해야하는 두 사람의 번호
int m; // m: 주어지는 관계의 개수

vector<int> connection[101]; 
int check[101];

void getInput() {
    scanf("%d", &n);
    scanf("%d %d", &x, &y);
    scanf("%d", &m);
    for(int i=0; i<m; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        connection[a].push_back(b);
        connection[b].push_back(a);
    }
}

int bfs() {
    memset(check, 0, sizeof(check));
    queue<int> q; q.push(x); check[x] = 0;
    while(!q.empty()) {
        int now = q.front(); q.pop();
        if(now == y) return check[now];
        for(int i=0; i<connection[now].size(); i++){
            int next = connection[now][i];
            if(check[next] != 0) continue;
            q.push(next);
            check[next] = check[now] + 1;
        }
    }
    return -1;
}

int main() {
    getInput();
    int count = bfs();
    printf("%d", count);
    return 0;
}