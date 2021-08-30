#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;
// string에서 nick_name - uid 뽑아주는거
pair<string,int> refineRecord(const string s,map<string,string> &users)
{
    pair<string,int> result;
    vector<string> words;
    string temp="";
    for(int i=0; i<s.length(); ++i)
    {
        string c;
        c.push_back(s[i]);
        if(c == " ")
        {
            words.push_back(temp);
            temp="";
        }
        else
        {
            temp += c;
        }
    }
    words.push_back(temp);
    
    for(auto s: words)
    {
        cout<< s<<endl;
    }
    cout<<"TEST END"<<endl;
    
    if(words[0]=="Enter")
    {
        users[words[1]] = words[2];
        result = pair(words[1],0);
    }
    else if(words[0]=="Leave")
    {
        result = pair(words[1],1);
    }
    else
    {
        users[words[1]] = words[2];
        result = pair("",-1);
    }
    return result;
}
// map을 통해서 uid --> nick_name으로 이어줌
// users(map) --> user : name

vector<string> solution(vector<string> record) {
    map<string,string> users;
    vector<pair<string,int>> result;
    vector<string> answer;

    const string ENTER = "님이 들어왔습니다.";
    const string LEAVE = "님이 나갔습니다.";

    for(string s: record)
    {
        pair<string,int> p = refineRecord(s,users);
        if(p.second!=-1)
        {
            result.push_back(p);
        }
    }
    
    for(pair<string,int> p : result)
    {
        if(p.second == 0)
        {
            string newStr = users[p.first] + ENTER;
            answer.push_back(newStr);
        }
        else if(p.second ==1)
        {
            string newStr = users[p.first] + LEAVE;
            answer.push_back(newStr);
        }
    }
    return answer;
}