#include <string>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

void splitter(string str,vector<string> &sets, set<string> &unionSet)
{
    vector<int> s;
    int l1 = str.length();
    for(int i=0; i<l1-1; i++)
    {
        if(i<l1-1)
        {
            char a = toupper(str[i]);
            char b = toupper(str[i+1]);
            if( 'A' <= a && a <= 'Z' && 'A'<= b && b <='Z')
            {
                sets.push_back({a,b});
                unionSet.insert({a,b});
            }
        }
    }
}
int solution(string str1, string str2) {
    vector<string> set1,set2; 
    set<string> unionSet;
    splitter(str1,set1,unionSet);
    splitter(str2,set2,unionSet);  

    int intersect_num = 0;
    int union_num = 0;
    for(string s1 : unionSet)
    {
        int a=0,b=0;
        for(string s2 : set1)
        {
            a += (s1==s2);
        }
        for(string s2 : set2)
        {
            b += (s1==s2);
        }
        if(a && b)
        {
            intersect_num += a<b?a:b;
        }
        union_num += a + b - (a>b?a:b);
    }

    if(set1.size()==0 && set2.size()==0 )
    {
        return 65536;
    }
    return ((double)intersect_num / union_num) *65536;
}