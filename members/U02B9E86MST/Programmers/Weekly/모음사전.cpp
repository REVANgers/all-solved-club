#include <string>
#include <vector>
#include <set>

using namespace std;
set<string> words;
char order[5] = {'A','E','I','O','U'};
void recursion(string word) {
    if(word.length()==5) {
        words.insert(word);
        return;
    }
    
    for(int i=-1; i<5; i++){
        if(i==-1) {
            words.insert(word);
            continue;
        }
        recursion(word+order[i]);
    }
}

int getIndex(string word) {
    int index = 0;
    for(auto x : words) {
        if(x.compare(word) == 0) return index;
        ++index;
    }
}

int solution(string word) {
    recursion("");
    return getIndex(word);
}
