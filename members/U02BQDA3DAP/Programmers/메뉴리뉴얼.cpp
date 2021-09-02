#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

map <string, int> m;

void findAll(string s, int n, string ans, int idx){
    if(ans.size()==n) {
        
        //없다면
        if(m.find(ans)==m.end()){
            m.insert({ans, 1});
        }
        
        //존재한다면 개수 추가
        else{
            m.find(ans)->second++;
        }
        return;
    }
    
    // 모든 조합 찾기
    for(int i=idx; i<s.length(); i++){
        findAll(s, n, ans+s[i], i+1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    
    for(int i=0; i<course.size(); i++){
        for(int j=0; j<orders.size(); j++){
            
            // 중복 방지를 위해 정렬
            sort(orders[j].begin(), orders[j].end());
            
            if(orders[j].size()>=course[i]){
                findAll(orders[j], course[i], "", 0);
            }
        }
    } 

  
    for(int i=0; i<course.size(); i++){
        int maxSize = 0;
         auto iter = m.begin();
         while(iter!=m.end()){
            if(course[i]==iter->first.size()){
                if(iter->second>maxSize) maxSize=iter->second;
            }
            ++iter;
         }
        
        iter = m.begin();
        while(iter!=m.end()){
            if(course[i]==iter->first.size()){
                if(iter->second==maxSize&&iter->second>1) answer.push_back(iter->first);
            }
            ++iter;
         }
    }
    
    sort(answer.begin(), answer.end());
    return answer;
}