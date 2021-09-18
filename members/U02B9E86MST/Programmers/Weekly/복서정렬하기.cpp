#include <bits/stdc++.h>

using namespace std;

/*
1부터 n번까지 번호가 있음.
1. 승률이 높을수록 앞쪽으로. 전적이 없으면 승률은 0%
2. 자신보다 더 무거운 복서를 많이 이길수록 앞쪽
3. 더 무거운 복서가 앞쪽
4. 더 작은 번호가 앞쪽
*/
struct profile {
    int num;
    int weight;
    int win;
    int totalMatchCount;
    int defeatHeavier;
};

bool compare(profile a, profile b){
    if(a.win * b.totalMatchCount == b.win * a.totalMatchCount) { // 승수가 동률이면
        if(a.defeatHeavier == b.defeatHeavier) { // 무거운 사람 승수가 동률이면
            if(a.weight == b.weight) { // 무게가 동률이면
                return a.num < b.num;
            }else {
                return a.weight > b.weight;
            }
        }else {
            return a.defeatHeavier > b.defeatHeavier;
        }
    }else {
        return a.win * b.totalMatchCount > b.win * a.totalMatchCount;
    }
}


vector<int> solution(vector<int> weights, vector<string> head2head) {
    vector<int> answer;
    int len = weights.size();
    vector<profile> datas(len);
    
    for(int i=0; i<len; i++) {
        datas[i].num = i+1;
        datas[i].weight = weights[i];
        
        string result = head2head[i]; // i의 경기결과 문자열
        for(int j=0; j<len; j++) {
            if(result[j] != 'N') { ++datas[i].totalMatchCount; } // 승부가 났다면 매치 수를 늘려준다.
            if(result[j] == 'W') { // 상대를 이겼다.
                ++datas[i].win;
                if(weights[i] < weights[j]) { // 상대가 더 무겁다.
                    ++datas[i].defeatHeavier;
                }
            }
        }
       // printf("win : %d, defeatHeavier : %d\n", datas[i].win, datas[i].defeatHeavier);
    }
    sort(datas.begin(), datas.end(), compare);
    for(auto data : datas) {
        answer.push_back(data.num);
    }
    return answer;
}
