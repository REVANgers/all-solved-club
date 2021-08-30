#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = INT32_MAX;
    if(s.length()==1) return 1;
    for(int n=1; n<s.length();n++){
        string temp = s;
        string pattern = "";
        string curPatternStr = "";
        int count = 0;
        while(temp.length()>=n){
            string sub = temp.substr(0,n);
            temp = temp.substr(n,temp.length()); 
            if(sub == pattern){
                ++count;
            }
            else{
                curPatternStr += (count>1 ? to_string(count) : "") + pattern;
                pattern = sub;
                count = 1;
            }
            if(temp.length() < n){
                curPatternStr += (count>1 ? to_string(count) : "") + pattern;
            }
        }
        if(!temp.empty()) curPatternStr += temp;
        if(answer>curPatternStr.length()) answer=curPatternStr.length();
    }
    return answer;
}
int main(){
    cout<<solution("aabbaccc");
}