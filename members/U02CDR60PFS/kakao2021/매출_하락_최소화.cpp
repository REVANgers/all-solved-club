#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int cost[300001][2];
vector<int> Sales;
vector<int> children[300001];
int INF = 987654321;

void traversal(int node)
{
    cost[node][0] = 0;
    cost[node][1] = Sales[node - 1];

    if (children[node].empty())
        return;

    int extraCost = INF;
    for (auto child : children[node])
    {
        traversal(child);

        if (cost[child][0] < cost[child][1])
        {
            cost[node][0] += cost[child][0];
            cost[node][1] += cost[child][0];
            extraCost = min(extraCost, cost[child][1] - cost[child][0]);
        }
        else
        {
            cost[node][0] += cost[child][1];
            cost[node][1] += cost[child][1];
            extraCost = 0;
        }
    }
    cost[node][0] += extraCost;
}

int solution(vector<int> sales, vector<vector<int>> links)
{
    Sales = sales;
    for (auto link : links)
    {
        children[link[0]].push_back(link[1]);
    }

    traversal(1);

    return min(cost[1][0], cost[1][1]);
}