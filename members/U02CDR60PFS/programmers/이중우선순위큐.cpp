#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>
using namespace std;
vector<int> solution(vector<string> operations)
{
    vector<int> answer;
    unordered_map<int, int> um;
    priority_queue<int> min;
    priority_queue<int> max;
    for (string oper : operations)
    {
        char cmd = oper[0];
        int num = stoi(oper.substr(2));
        if (cmd == 'I')
        {
            min.push(-num);
            max.push(num);
            um[num]++;
        }
        else if (num == 1)
        {
            while (!max.empty() && um[max.top()] == 0)
            {
                max.pop();
            }
            if (max.empty())
                continue;
            um[max.top()]--;
            max.pop();
        }
        else if (num == -1)
        {
            while (!min.empty() && um[-min.top()] == 0)
            {
                min.pop();
            }
            if (min.empty())
                continue;
            um[-min.top()]--;
            min.pop();
        }
    }

    while (!max.empty() && um[max.top()] == 0)
        max.pop();
    while (!min.empty() && um[-min.top()] == 0)
        min.pop();

    max.empty() ? answer.push_back(0) : answer.push_back(max.top());
    min.empty() ? answer.push_back(0) : answer.push_back(-min.top());

    return answer;
}