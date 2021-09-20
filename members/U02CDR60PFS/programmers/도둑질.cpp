#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int d1[1000001]; // 0번 집 털 경우
int d2[1000001]; // 0번 집 안 턴 경우
int solution(vector<int> money)
{
    int answer = 0;
    int n = money.size();
    d1[1] = money[0];
    for (int i = 1; i < n - 1; i++)
    {
        d1[i + 1] += max(d1[i], d1[i - 1] + money[i]);
    }

    for (int i = 1; i < n; i++)
    {
        d2[i + 1] = max(d2[i], d2[i - 1] + money[i]);
    }

    answer = max(d1[n - 1], d2[n]);
    return answer;
}