#include <iostream>
#include <vector>

using namespace std;

int inorder[100001];
int postorder[100001];
int idx[100001];

void preOrder(int inStart, int inEnd, int postStart, int postEnd)
{
    // 더 이상 분할 할 수 없는 경우 return
    if (inStart > inEnd || postStart > postEnd)
        return;

    // postorder의 끝 값이 root값
    int rootIndex = idx[postorder[postEnd]];
    int leftSize = rootIndex - inStart;
    int rightSize = inEnd - rootIndex;

    // root 출력
    cout << inorder[rootIndex] << ' ';

    //왼쪽
    preOrder(inStart, rootIndex - 1, postStart, postStart + leftSize - 1);
    
    //오른쪽
    preOrder(rootIndex + 1, inEnd, postStart + leftSize, postEnd - 1);
}


int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> inorder[i];
	}

	for (int i = 0; i < n; i++) {
		cin >> postorder[i];
	}

	for (int i = 0; i < n; i++) {
		idx[inorder[i]] = i;
	}

    preOrder(0, n-1, 0, n-1);
}