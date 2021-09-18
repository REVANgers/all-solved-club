#include <string>
#include <vector>
#include <map>

using namespace std;
map <string, int> dictionary;
 vector<int> answer;

string zip(string str){
    string w = str;
    int c = str.length()-1;
    
    for(int i=str.length()-1; i>=0; i--){
        // 가장 긴 w 찾기
        if(dictionary.find(w)!=dictionary.end()){
            c = i;
            break;
        }
        else{
            w = w.substr(0, i);
        }
    }
    
    if(c<str.length()-1){
        string wc = w + str[c+1];
        dictionary.insert({wc, dictionary.size()+1});
    }
    answer.push_back(dictionary.find(w)->second);
    return str.substr(c+1); 
}

vector<int> solution(string msg) {
    
    for(int i=0; i<26; i++){
        string str = "";
        str+=(char)('A'+i);
        dictionary.insert({str, i+1});
    }
    
    string s = zip(msg);
    while(s.length()>0){
        s = zip(s);
    }
    
    return answer;
}