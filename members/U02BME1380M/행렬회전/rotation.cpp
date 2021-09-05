#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> getArray(int rows,int columns){
    vector<vector<int>> arr;
    int n = 1;
    for(int i=0; i<rows; i++){
        vector<int> row;
        for(int j=0; j<columns; j++){
            row.push_back(n++);
        }
        arr.push_back(row);
    }
    return arr;
}



void showArray(const vector<vector<int>> &arr){
    const int rows = arr.size();
    const int cols = arr[0].size();
    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++){
            cout << arr[i][j] <<"\t";
         }
        cout<<"\n";
    }
}
int rotateArray(vector<vector<int>> &arr, const vector<int> &query){
    int s_row = query[0]-1;
    int s_col = query[1]-1;
    int e_row = query[2]-1;
    int e_col = query[3]-1;
    cout << s_row << "," << s_col <<","<<e_row<<","<<e_col<<"\n";
    int prev = arr[s_row][s_col];
    int temp;
    int min = INT32_MAX;
    for(int i=s_col; i<=e_col; i++){
        temp = arr[s_row][i];
        arr[s_row][i] = prev;
        prev = temp;
        min = min > temp ? temp : min;
    }
    for(int i=s_row+1; i<=e_row; i++){
        temp = arr[i][e_col];
        arr[i][e_col] = prev;
        prev = temp;
        min = min > temp ? temp : min;
    }
    for(int i=e_col-1; i>=s_col; i--){
        temp = arr[e_row][i];
        arr[e_row][i] = prev;
        prev = temp;
    }
    for(int i=e_row-1; i>=s_row; i--){
        temp = arr[i][s_col];
        arr[i][s_col] = prev;
        prev = temp;
        min = min > temp ? temp : min;
    }

    return min;
}


vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    vector<vector<int>> arr = getArray(rows,columns);
    for(vector<int> query : queries){
        answer.push_back(rotateArray(arr,query));
        showArray(arr);
    }
    return answer;
}