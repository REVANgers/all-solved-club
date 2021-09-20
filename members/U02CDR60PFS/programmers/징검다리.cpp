// 어렵다 ㅠ 
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int solution(int distance, vector<int> rocks, int n)
{
    int answer = 0;
    int left = 0, right = distance;
    sort(rocks.begin(), rocks.end());
    while (left <= right)
    {
        int mid = (left + right) / 2;
        int cnt = 0, prev = 0;
        for (int i = 0; i < rocks.size(); i++)
        {
            if (rocks[i] - prev < mid)
                cnt++;
            else
                prev = rocks[i];
        }
        if (distance - prev < mid)
            cnt++;
        if (cnt <= n)
        {
            answer = max(answer, mid);
            left = mid + 1;
        }
        else
            right = mid - 1;
    }
    return answer;
}