#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <stdlib.h>

using namespace std;

class Move
{
public:
    int elementCount;
    int fromStack;
    int toStack;
    Move(int elementCount, int fromStack, int toStack)
    {
        this->elementCount = elementCount;
        this->fromStack = fromStack;
        this->toStack = toStack;
    }
};

int main()
{
    ifstream file("input.txt");
    string str;

    vector<string> stack_vec;
    for (int i = 0; i < 8; i++)
    {
        getline(file, str);
        replace(str.begin(), str.end(), '[', ' ');
        replace(str.begin(), str.end(), ']', ' ');
        stack_vec.push_back(str);
    }

    vector<stack<char>> stacks;
    for (int i = 0; i < stack_vec[0].size(); i++)
    {
        stack<char> s;
        for (int j = stack_vec.size() - 1; j >= 0; j--)
        {
            if (stack_vec[j][i] != ' ')
            {
                s.push(stack_vec[j][i]);
            }
        }
        if (!s.empty())
        {
            stacks.push_back(s);
        }
    }

    getline(file, str);
    getline(file, str);

    vector<Move> moves;
    while (getline(file, str))
    {
        int elementCount = 0;
        int fromStack = 0;
        int toStack = 0;

        elementCount = atoi(str.c_str() + 5);
        fromStack = atoi(str.c_str() + 12);
        toStack = atoi(str.c_str() + 17);

        moves.push_back(Move(elementCount, fromStack, toStack));
    }

    for (int i = 0; i < moves.size(); i++)
    {
        int elementCount = moves[i].elementCount;
        stack<char> fromStack = stacks[moves[i].fromStack - 1];
        stack<char> toStack = stacks[moves[i].toStack - 1];

        stack<char> tempStack;
        for (int j = 0; j < elementCount; j++)
        {
            char item = fromStack.top();
            tempStack.push(item);
            fromStack.pop();
        }

        while (!tempStack.empty())
        {
            char item = tempStack.top();
            toStack.push(item);
            tempStack.pop();
        }

        stacks[moves[i].fromStack - 1] = fromStack;
        stacks[moves[i].toStack - 1] = toStack;
    }

    for (int i = 0; i < stacks.size(); i++)
    {
        cout << stacks[i].top() << endl;
    }
}