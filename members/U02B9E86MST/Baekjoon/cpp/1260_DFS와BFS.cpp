#include <bits/stdc++.h>
#define endl "\n"
#define __usecin__                    \
    ios_base::sync_with_stdio(false); \
    cin.tie(nullptr);                 \
    cout.tie(nullptr);
using namespace std;
// 1억:1e8
// int_max = 2^31-1 ~= 2.1e9
// llong_max = 2^63-1
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<pair<int, int> > vpii;

const int MAX_NODE = 1000;

set<int> node[1001];
int check[MAX_NODE+1];

void getInput(int &n, int &m, int &v) {
    scanf("%d %d %d", &n, &m, &v);
    for (int i = 0; i < m; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        node[x].insert(y);
        node[y].insert(x);
    }
}

void dfs(int now) {
    printf("%d ", now);
    check[now] = 1;

    for(auto it = node[now].begin(); it != node[now].end(); ++it) {
        if(check[*it]) continue;
        dfs(*it);
    }
    // for(int i=0; i<node[now].size(); i++){ 
    //     int next = node[now][i];
    //     if(check[next]) continue;
    //     dfs(next);
    // }
}

void bfs(int v)
{
    queue<int> q;
    q.push(v);
    check[v]=1;
    while (!q.empty())
    {
        int now = q.front(); 
        q.pop();
        printf("%d ", now);
        for(auto it = node[now].begin(); it != node[now].end(); ++it) {
            if(check[*it]) continue;
            check[*it] = 1;
            q.push(*it);
        }
        // for(int i=0; i<node[now].size(); i++){
        //     int next = node[now][i];
        //     if(check[next]) continue;
        //     check[next]=1;
        //     q.push(next);
        // }
    }
}

int main()
{
    int n, m, v;
    getInput(n, m, v);
    dfs(v);
    memset(check, 0, sizeof(check));
    printf("\n");
    bfs(v);
}