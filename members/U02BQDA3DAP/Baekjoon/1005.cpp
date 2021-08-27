#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;
int time[1001];
vector <vector<int>> connect(1001);
int cache[1001];

int find(int destination) {

	//끝까지 왔다면 return
	if (connect[destination].size()==0) return time[destination];

	//memorization
	if (cache[destination] != -1) return cache[destination];

	int maxTime = 0;
	for (int i = 0; i < connect[destination].size(); i++){
		int end = connect[destination][i];
		maxTime = max(maxTime, time[destination] + find(end));
	}

	return (cache[destination] = maxTime);

}

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n, k;
		cin >> n >> k;
		for (int i = 1; i <= n; i++) {
			cin >> time[i];
		}

		memset(cache, -1, sizeof(cache));
		for (int i = 0; i < k; i++) {
			int s, e;
			cin >> s >> e;
			connect[e].push_back(s);
		}

		//승리하기 위해 지어야 하는 건물
		int w;
		cin >> w;

		cout<<find(w)<<"\n";

		//초기화
		connect = vector<vector<int>>(1001);
	}
}
