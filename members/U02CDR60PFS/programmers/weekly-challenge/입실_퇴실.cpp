#include <string>
#include <vector>
#include <iostream>
using namespace std;
int e[1001];
int l[1001];
vector<int> solution(vector<int> enter, vector<int> leave)
{
    int n = enter.size();
    vector<int> answer(n);

    for (int i = 0; i < n; i++)
    {
        e[enter[i]] = i;
        l[leave[i]] = i;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = i + 1; j <= n; j++)
        {
            if ((e[i] - e[j]) * (l[i] - l[j]) < 0)
            {
                answer[i - 1]++;
                answer[j - 1]++;
            }
            else
            {
                int a = e[i] < e[j] ? e[j] : e[i];
                int b = l[i] < l[j] ? l[i] : l[j];

                for (int k = 1; k <= n; k++)
                {
                    if (e[k] > a && l[k] < b)
                    {
                        answer[i - 1]++;
                        answer[j - 1]++;
                        break;
                    }
                }
            }
        }
    }

    return answer;
}