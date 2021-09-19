/* 내가 짠거
#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
bool compare(vector<int> a, vector<int> b){
    if(a[0] == b[0])
        return a[1] < b[1];
    return a[0] < b[0];
}
int solution(vector<vector<int>> jobs) {
    int answer = 0;
    priority_queue<pair<int,int>> pq;
    sort(jobs.begin(), jobs.end(), compare); // 시간 순으로 정렬

    int t = 0;
    for(int i=0; i<jobs.size();) {
        while(i < jobs.size() && t >= jobs[i][0]) {
            pq.push({-jobs[i][1], -jobs[i][0]});
            i++;
        }
        if(pq.empty()){
            t = jobs[i][0] + jobs[i][1];
            answer += jobs[i][1];
            i++;
        }
        else {
            int time = -pq.top().first;
            int request = -pq.top().second;
            pq.pop();
            answer += (time + (t-request));
            t += time; 
        }
    }
    while(!pq.empty())
    {
            int time = -pq.top().first;
            int request = -pq.top().second;
            pq.pop();
            answer += (time + (t-request));
            t += time; 
    }
    return answer / jobs.size();
}
*/

// 개선
#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
bool compare(vector<int> a, vector<int> b)
{
    if (a[0] == b[0])
        return a[1] < b[1];
    return a[0] < b[0];
}
int solution(vector<vector<int>> jobs)
{
    int answer = 0;
    priority_queue<pair<int, int>> pq;
    sort(jobs.begin(), jobs.end(), compare); // 시간 순으로 정렬

    int t = 0, i = 0;
    while (i < jobs.size() || !pq.empty())
    {
        if (i < jobs.size() && t >= jobs[i][0])
        {
            pq.push({-jobs[i][1], -jobs[i][0]});
            i++;
            continue;
        }
        if (!pq.empty())
        {
            int time = -pq.top().first;
            int request = -pq.top().second;
            pq.pop();
            answer += (time + (t - request));
            t += time;
        }
        else
            t = jobs[i][0];
    }
    return answer / jobs.size();
}