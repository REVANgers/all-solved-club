#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

struct Node {
	int x;
	int y;
	int index;
	Node* leftNode;
	Node* rightNode;
};

void insert(Node* parent, Node* child) {
	if (parent->x < child->x) {
		if (parent->rightNode == NULL) parent->rightNode = child;
		else insert(parent->rightNode, child);
	}
	else {
		if (parent->leftNode == NULL) parent->leftNode = child;
		else insert(parent->leftNode, child);
	}
}

vector<Node> Tree;
vector<int> pre;
vector<int> post;

void preorder(Node* cur) {
	if (cur == NULL) return;
	pre.push_back(cur->index);
	preorder(cur->leftNode);
	preorder(cur->rightNode);
}

void postorder(Node* cur) {
	if (cur == NULL) return;
	postorder(cur->leftNode);
	postorder(cur->rightNode);
	post.push_back(cur->index);
}

bool cmp(Node& a, Node& b) {
	if (a.y == b.y)
		return a.x < b.x;
	return a.y > b.y;
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
	vector<vector<int>> answer;
	
	for (int i = 0; i < nodeinfo.size(); i++) 
		Tree.push_back({nodeinfo[i][0],nodeinfo[i][1], i + 1 });

	sort(Tree.begin(), Tree.end(), cmp);
	Node* root = &Tree[0];
	
	for (int i = 1; i < Tree.size(); i++) 
		insert(root, &Tree[i]);

	preorder(root);
	postorder(root);

	answer.push_back(pre);
	answer.push_back(post);
	return answer;
}