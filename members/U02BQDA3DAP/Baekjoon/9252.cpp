#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int dp[1001][1001];

int main() {
	string a, b; 
	cin >> a >> b;

	for (int i = 1; i <= b.length(); i++) {
		for (int j = 1; j <= a.length(); j++) {
			if (a[j - 1] == b[i - 1])
				dp[i][j] = dp[i - 1][j - 1] + 1;
			else
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
		}
	}

	string lcs = "";
	int col = a.length();
	int row = b.length();

	while (dp[row][col]) {

		if (dp[row][col] == dp[row - 1][col]) {
			row--;
		}
		else if (dp[row][col] == dp[row][col - 1]) {
			col--;
		}
		else {
			lcs += a[col-1];
			row--, col--;
		}

	}

	cout << lcs.length() << "\n";
	if (lcs.length() == 0) return 0;
	else {
		for (int i = lcs.length() - 1; i >= 0; i--)cout << lcs[i];
	}
}