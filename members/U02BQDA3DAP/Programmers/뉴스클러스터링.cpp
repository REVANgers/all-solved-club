#include <string>
#include <vector>

using namespace std;

vector <string> oneString;
vector <string> twoString;

int DIV = 65536;

string lower(string str){
    string lowerStr = "";
     for(int i=0; i<str.length(); i++){
        char a = tolower(str[i]);
        lowerStr+=a;
    }
    return lowerStr;
}


int solution(string str1, string str2) {
    int answer = 0;
    
    string lower1 = lower(str1);
    string lower2 = lower(str2);
    
    string pair= "";
    for(int i=0; i<lower1.length()-1; i++){
        char a = lower1[i];
        char b = lower1[i+1];
        if(a>='a'&&a<='z'&&b>='a'&&b<='z'){
            pair+=a; pair+=b;
            oneString.push_back(pair);
            pair = "";
        }
    }
    
    for(int i=0; i<lower2.length()-1; i++){
        char a = lower2[i];
        char b = lower2[i+1];
        if(a>='a'&&a<='z'&&b>='a'&&b<='z'){
            pair+=a; pair+=b;
            twoString.push_back(pair);
            pair = "";
        }
    }
    
  
    if(oneString.size()==0&&twoString.size()==0) return DIV;
    int strInter = 0;

    for(int i=0; i<oneString.size(); i++){
        for(int j=0;j<twoString.size(); j++){
            if(oneString[i]==twoString[j]) {
                strInter++;
                twoString[j]='X';
                break;
            }
        }
    }
    
    int strUnion = oneString.size()+twoString.size()-strInter;
    
    if(strInter==0) return 0;
    float ans = strInter*DIV/strUnion;
    
    answer = ans;
    return answer;
}