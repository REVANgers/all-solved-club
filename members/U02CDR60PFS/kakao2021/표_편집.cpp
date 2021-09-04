#include <string>
#include <vector>
#include <iostream>
#include <stack>
using namespace std;

struct Node
{
    bool removed;
    Node *prev;
    Node *next;
};

Node nodeArr[1000000];

string solution(int n, int k, vector<string> cmd)
{
    string answer = "";

    for (int i = 1; i < n; i++)
    {
        nodeArr[i - 1].next = &nodeArr[i];
        nodeArr[i].prev = &nodeArr[i - 1];
    }

    Node *cur = &nodeArr[k];
    stack<Node *> stack;

    for (string str : cmd)
    {
        if (str[0] == 'U')
        {
            int x = atoi(str.c_str() + 2);
            for (int i = 0; i < x; i++)
            {
                cur = cur->prev;
            }
        }
        else if (str[0] == 'D')
        {
            int x = atoi(str.c_str() + 2);
            for (int i = 0; i < x; i++)
            {
                cur = cur->next;
            }
        }
        else if (str[0] == 'C')
        {
            stack.push(cur);
            cur->removed = true;
            Node *up = cur->prev;
            Node *down = cur->next;
            if (up)
            {
                up->next = cur->next;
            }
            if (down)
            {
                down->prev = cur->prev;
                cur = down;
            }
            else
            {
                cur = up;
            }
        }
        else
        {
            Node *node = stack.top();
            stack.pop();
            node->removed = false;
            Node *up = node->prev;
            Node *down = node->next;
            if (up)
            {
                up->next = node;
            }
            if (down)
            {
                down->prev = node;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (nodeArr[i].removed == true)
            answer += 'X';
        else
            answer += 'O';
    }
    return answer;
}