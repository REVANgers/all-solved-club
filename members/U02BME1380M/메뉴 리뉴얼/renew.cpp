#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;
// N 개의 원소를 갖는 조합을 만들고
// 해당 조합에 대해서 Map 구조를 통해 카운팅
// 풀다가 그냥 JS로 풀이했음.
void mapping(string order, map<string,int>& courseMap, int n){
    string s = "";
    getCombination(courseMap,order,s,n,n,0,0);
}

void getCombination(map<string,int>& courseMap, string order, string res,  const int n, int r, int idx, int depth){
    if(depth==0){
        courseMap[res]++;
    }
    else if(depth==n){
        return;
    }
    else {
        string comb = res + order[idx];
        getCombination(courseMap, order,comb,n,r-1, idx+1, depth+1);
        getCombination(courseMap, order,res,n,r,idx,depth+1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    vector<map<string,int>> mapArr;
    for(const int n : course){
        map<string, int> iMap;
        mapArr.push_back(iMap);
        for(const string order : orders){
            mapping(order,iMap,n);
        }
    }
    for(const map<string,int> map : mapArr){
        int max = 0;
        vector<string> ans;
        for(auto [key,value] : map){
            if(value < max){
                max = value;
                ans.clear();
                ans.push_back(key);
            }
            else if (value == max){
                ans.push_back(key);
            }             
        }
        for(const string s : ans){
            answer.push_back(s);
        }
    }
    sort(answer.begin(),answer.end());
    return answer;
}