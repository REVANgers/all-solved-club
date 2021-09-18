#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int cacheSize, vector<string> cities) {

    vector <string> cache;
    int answer = 0;

    for(int i=0; i<cities.size(); i++){
        transform(cities[i].begin(), cities[i].end(), cities[i].begin(), ::tolower);
        if(cacheSize==0)answer+=5;
        else{
            if(find(cache.begin(), cache.end(), cities[i])==cache.end()){
                //cache miss

                //다 차있다면 삭제
                if(cache.size()==cacheSize){
                    cache.erase(cache.begin());
                }

                cache.push_back(cities[i]);

                answer+=5;
            }

            else{
                //cache hit
                cache.erase(find(cache.begin(), cache.end(), cities[i]));
                cache.push_back(cities[i]);
                answer+=1;
            }

        }
    }

    return answer;
}