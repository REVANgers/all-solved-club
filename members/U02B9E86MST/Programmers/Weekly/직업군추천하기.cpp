#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>

#define endl '\n'

using namespace std;

// <job, <language, int>>
unordered_map<string, unordered_map<string, int> > mappedTable;

vector<string> split(string str) {
    stringstream ss(str);
    vector<string> splited;
    string buffer;
    bool first = true;
    while(getline(ss, buffer, ' ')) {
        splited.push_back(buffer);
    }
    return splited;
}

void makeMappedTable(vector<string>& table) {
    for(string rankString : table) {
        vector<string> ranks = split(rankString); 
        string job = ranks[0];
        unordered_map<string, int> umap;
        int index = 5; bool first = true;
        for(auto language : ranks) {
            if(first) { first=false; continue; }
            umap[language] = index;
            --index;
        }
        mappedTable[job] = umap;
    }
}

string solution(vector<string> table, vector<string> languages, vector<int> preference) {
    string answer = "";
    makeMappedTable(table);
    
    int maxScore = 0;
    for(auto rt : mappedTable) {
        auto ranks = rt.second;
        int total = 0;
        for(int i=0; i<languages.size(); i++) {
            string language = languages[i];
            auto it = ranks.find(language);
            int score = (it == ranks.end() ? 0 : it->second);
            total += score * preference[i];
        }
        if(maxScore < total) {
            maxScore = total;
            answer = rt.first;
        }else if(maxScore == total) {
            if( answer.compare(rt.first) > 0 ) answer = rt.first;
        }
    }
    
    // 직군별로 map을 작성해서,
    // index = 0 ( language : PYTHON, preference : 7)
    // result += map[PYTHON] * preference
    return answer;
}
