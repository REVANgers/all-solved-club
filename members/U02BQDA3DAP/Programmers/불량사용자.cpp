#include <string>
#include <vector>
#include <set>
#include <iostream>

using namespace std;
set<string> ans;
bool visited[8];
vector<string> user;
vector<string> ban;

void find(int idx){
    if(idx==ban.size()){
        string s = "";
        for(int i=0; i<8; i++){
            if(visited[i]) {s += user[i];}
        }
        ans.insert(s);
        return;    
    }
    
    for(int i=0; i<user.size(); i++){
        //이미 결과에 포함
        if(visited[i]) {continue;}
        
        else{
            bool check = true;

            //길이가 다르면 불가능
            if(user[i].size()!=ban[idx].size()) {continue;}
            
            //같다면 비교
            else{
                for(int j=0; j<ban[idx].length(); j++){
                    if(ban[idx][j]=='*') continue;
                    else if(ban[idx][j]!=user[i][j]) {
                        check=false;
                    }
                }
       
                //답이라면 추가
                if(check){
                    visited[i]=true;
                    find(idx+1);
                    visited[i]=false;
                }
                
            }
        }
    }
    
 
}
int solution(vector<string> user_id, vector<string> banned_id) {
    int answer = 0;
    user = user_id;
    ban = banned_id;
    
    //banned_id의 0번째 index부터 확인
    find(0);

    answer = ans.size();
    return answer;
}