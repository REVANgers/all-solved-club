#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(vector<int> people, int limit)
{
    int answer = 0;
    sort(people.begin(), people.end(), greater<int>());
    int s = 0, e = people.size() - 1;

    while (s <= e)
    {
        if (people[s] + people[e] <= limit)
        {
            s++;
            e--;
        }
        else
        {
            s++;
        }
        ++answer;
    }

    return answer;
}