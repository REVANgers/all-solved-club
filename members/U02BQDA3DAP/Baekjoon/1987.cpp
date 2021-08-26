#include <iostream>
#include <vector>

using namespace std;
char board[21][21];
int r, c;
int mymax = 0;
bool visited[26];

void find(int x, int y, int cnt) {
	int dx[4] = { 0, 0, 1, -1 };
	int dy[4] = { 1, -1, 0, 0 };

	if (cnt > mymax)mymax = cnt;

	for (int i = 0; i < 4; i++) {
		
		int nx = x + dx[i];
		int ny = y + dy[i];

		//움직일 수 있는 위치라면 움직인다.
		if (nx >= 0 && nx < r && ny >= 0 && ny < c) {

			//이미 방문한 문자인지 확인
			if (!visited[board[nx][ny] - 'A']) { //방문하지 않음
				visited[board[nx][ny] - 'A']=true;
				find(nx, ny, cnt+1);
				visited[board[nx][ny] - 'A'] = false;
			}

		}
	}
}


int main() {
	cin >> r >> c;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> board[i][j];
		}
	}

	visited[board[0][0]-'A']=true;
	find(0, 0, 1);

	cout << mymax;
}
