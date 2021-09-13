#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
vector<vector<char>> board;
int n, m;
int ans = 11;

//상,좌,우 이동
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,1,-1 };

void move(int rx, int ry, int bx, int by, int cnt) {
	if (cnt >= ans) { return; }

	for (int i = 0; i < 4; i++) {
		int rnx = rx + dx[i];
		int rny = ry + dy[i];
		int bnx = bx + dx[i];
		int bny = by + dy[i];

		bool redHole = false;
		bool blueHole = false;
		bool BR = false;

		vector<vector<char>> save;
		save = board;

		//빨간 구슬 이동
		while (board[rnx][rny] == '.') {
			rnx += dx[i];
			rny += dy[i];
		}
		if (board[rnx][rny] == '#') {
			// 이동할 수 있을만큼 이동 -> 실제로 이동시킴
			swap(board[rnx - dx[i]][rny - dy[i]], board[rx][ry]);
		}
		else if (board[rnx][rny] == 'B') {
			BR = true;
		}
		else {
			// hole
			redHole = true;
			board[rx][ry] = '.';
		}

		//파란 구슬 이동
		while (board[bnx][bny] == '.') {
			bnx += dx[i];
			bny += dy[i];
		}
		if (board[bnx][bny] == '#'|| board[bnx][bny] == 'R') {
			// 이동할 수 있을만큼 이동 -> 실제로 이동시킴
			swap(board[bnx - dx[i]][bny - dy[i]], board[bx][by]);
		}
		else {
			// hole
			blueHole = true;
			board[bx][by] = '.';
		}

		//움직이는 방향에 파란 구슬이 빨간 구슬보다 앞에 있다면
		//파란 구슬을 움직이고 빨간 구슬을 다시 움직여야
		if (BR) {
			while (board[rnx][rny] == '.') {
				rnx += dx[i];
				rny += dy[i];
			}
			if (board[rnx][rny] == '#'|| board[rnx][rny] == 'B') {
				// 이동할 수 있을만큼 이동 -> 실제로 이동시킴
				swap(board[rnx - dx[i]][rny - dy[i]], board[rx][ry]);
			}
			else {
				// hole
				redHole = true;
				board[rx][ry] = '.';
			}
			BR = false;
		}

		if (redHole && blueHole) {
			// 빨간색과 파란색이 모두 구멍에 들어감 -> X
			board = save;
		}
		else if (redHole) {
			board = save;
			ans = min(cnt, ans);
			return;
		}
		else if (blueHole) {
			board = save;
			continue;
		}

		else if (rnx - dx[i] == rx && rny - dy[i] == ry && bnx - dx[i] == bx && bny - dy[i] == by) {
			//이동이 없음
			continue;
		}
		else {
			move(rnx - dx[i], rny - dy[i], bnx - dx[i], bny - dy[i], cnt+1);
			board = save;
		}
	}
}

int main() {
	cin >> n >> m;
	int rx, ry, bx, by;
	//board 입력
	for (int i = 0; i < n; i++) {
		vector <char> v;
		board.push_back(v);
		for (int j = 0; j < m; j++) {
			char c;
			cin >> c;
			if (c == 'R') { rx = i; ry = j; }
			else if (c == 'B') { bx = i; by = j; }
			board[i].push_back(c);
		}
	}

	move(rx, ry, bx, by, 1);

	if (ans == 11) cout<< -1;
	else cout<<ans;
}
