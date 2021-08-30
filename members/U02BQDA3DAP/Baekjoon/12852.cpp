#include <iostream>
#include <algorithm>
using namespace std;

int before[1000001];
int dp[1000001];

int solve(int n)
{
	dp[1] = 0;
	for (int i = 2; i <= n; i++)
	{
		// -1
		dp[i] = dp[i - 1] + 1;
		before[i] = i - 1;

		// 3으로 나누기
		if (i % 3 == 0)
		{
			if (dp[i] > dp[i / 3] + 1)
			{
				dp[i] = dp[i / 3] + 1;
				before[i] = i / 3;
			}

		}

		// 2로 나누기
		if (i % 2 == 0)
		{
			if (dp[i] > dp[i / 2] + 1)
			{
				dp[i] = dp[i / 2] + 1;
				before[i] = i / 2;
			}

		}
	}

	return dp[n];
}

int main(void)
{
	int  n;
	cin >> n;

	cout << solve(n) << '\n';

	while (n!=0)
	{
		cout << n << " ";
		n = before[n];
	}

	return 0;
}