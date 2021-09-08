#include <string>
#include <vector>
#include <iostream>

using namespace std;
int mm, nn;
vector<string> b;
bool check[31][31];
int ANS = 0;

void move(int x, int y){
   
    if (b[x][y] == 'X') { // 내가 빈 공간이라면
        for (int k = x; k > 0; k--) {
            if (b[k - 1][y] == 'X') break;
            b[k][y] = b[k - 1][y]; // 위에 있는 것을 땡겨옴
            b[k - 1][y] = 'X'; // 땡겨진 것들의 원래 자리를 빈공간으로
        }
    }
}

bool eraseBoard(){
    bool c = false;
    for(int i=0; i<mm; i++){
        for(int j=0; j<nn; j++){
            if(check[i][j]){
                ANS++;
                b[i][j] = 'X';
                c = true;
            }
        }
    }
    
    return c;
}

void find(int x, int y){
    int dx[3] = {1, 0, 1};
    int dy[3] = {0, 1, 1};
    
    int p = b[x][y];
    int cnt = 1;
    if(p!='X'){
        for(int i=0; i<3; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx>=0&&nx<mm&&ny>=0&&ny<nn&&b[nx][ny]!='X'){
                if(b[nx][ny]==p) cnt++;
            }
        }
    }
    
    
    //지워질 조건 만족 -> 지우기로 check
    if(cnt==4){
        check[x][y] = true;
        for(int i=0; i<3; i++){
            check[x + dx[i]][y + dy[i]] = true;
        }
    }
}

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    mm = m;
    nn = n;
    b = board;

    while(1){
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                find(i, j);
            }
        }
        
    
        if(eraseBoard()){          
            for(int i=0; i<m; i++){
                for(int j=0; j<n; j++){
                    move(i, j);
                }
            }  
        }
        
    
        else break;
        
        // 초기화
        for(int i=0; i<m; i++){
                for(int j=0; j<n; j++){
                    check[i][j]=false;
                }
        }   
          
    }
    
    return ANS;
}