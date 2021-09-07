#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<vector<string>> rel;
vector<int> v;
vector<bool> sel;
vector<vector<int>> can;
int col, row;

void makePair(){
    map <string, int> check;
    for(int i=0; i<row; i++){
        string s="";
        for(int j=0; j<v.size(); j++){
            s+=rel[i][v[j]];
        }
        check.insert({s, 1});
    }
    
    // 최소성 확인
    if(check.size()==row){
       if(v.size()==1) {
           can.push_back(v);   
       }
        
       else{
            bool c = true;
            for(int i=0; i<can.size(); i++){
                int count=0;
                for(int j=0; j<can[i].size(); j++){
                    int key = can[i][j];
                    if(find(v.begin(), v.end(), key)!=v.end()){
                        count++;
                    }
                }
        
                //이미 있는 후보키를 포함하고 있다면
                if(count==can[i].size()){
                    c = false;
                }
            }
           
           if(c) can.push_back(v);
       }
    }        
}

void makeWord(int idx,int cnt){
    //개수만큼 뽑았다면 map에 넣기
    if(cnt==0){
        makePair();   
        return;
    }
    
    for (int i = idx; i < col; i++) {
        if(sel[i]) continue;
        sel[i]=true;
        v.push_back(i);
        makeWord(i + 1, cnt - 1);
        v.pop_back();
        sel[i]=false;
    }
}

int solution(vector<vector<string>> relation) {

    col = relation[0].size();
    row = relation.size();
    rel = relation;
    
    sel.resize(col, false);
    
    for(int i=1; i<=col; i++){
        makeWord(0,i);   
    }
    
    return can.size();
}