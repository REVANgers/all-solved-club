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

int v, e; 
vector<int> edge[101];
int check[101];

void getInput() {
    scanf("%d", &v);
    scanf("%d", &e);
    for(int i=0; i<e; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        edge[x].push_back(y);
        edge[y].push_back(x);
    }
}

int bfs() {
    // 1번부터 시작한다.
    int start = 1;
    int count = 0; bool first=true;
    queue<int> q; q.push(start); check[start] = 1;
    while(!q.empty()) {
        int now = q.front(); q.pop();
        if(first) first=false;
        else count++;

        for(int i=0; i<edge[now].size(); i++){
            int next = edge[now][i];
            if(check[next]) continue;
            check[next] = 1;
            q.push(next);
        }
    }
    return count;
}

int main() {
    getInput();
    int count = 0;
    count = bfs();
    printf("%d", count);
    return 0;
}