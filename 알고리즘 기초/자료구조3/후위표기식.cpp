#include <iostream>
#include <cstring>
#include <stack>

#define MAX_LINE 1000
using namespace std;
// + - / * ( )

//우선순위 확인 함수
int get_priority(char c)
{
    if (c == '+' || c == '-')
    {
        return 1;
    }
    else if (c == '*' || c == '/')
    {
        return 2;
    }
    else if (c == '(' || c == ')')
    {
        return 0;
    }
    return -1;
}

int main()
{
    char line[MAX_LINE]; //입력받을 줄
    stack<char> s;       //각 토큰 확인용
    stack<string> n;     //계산할 숫자 저장
    string temp = "";    //숫자저장할 임시 문자열

    cin.getline(line, MAX_LINE); //입력받음
    int length = strlen(line);   //길이 확인
    char c;

    for (int i = 0; i < length; i++)
    {
        c = line[i];
        //연산자일 경우
        if (c == '+' || c == '-' || c == '*' || c == '/')
        {
            while (!s.empty() && (get_priority(c) <= get_priority(s.top())))
            {
                cout << s.top();
                s.pop();
            }
            s.push(c);
        }
        //괄호 확인
        else if (c == '(')
        {
            s.push(c);
        }
        //괄호 끝남
        else if (c == ')')
        {
            while (true)
            {
                if (s.top() == '(')
                {
                    s.pop();
                    break;
                }
                cout << s.top();
                s.pop();
            }
        }
        //숫자일 경우(여러자리 확인해야하므로 반복)
        else
        {
            temp = "";
            cout << line[i];
            temp += line[i];
        }
    }

    //남아있는 잔여 연산자 출력
    while (!s.empty())
    {
        cout << s.top();
        s.pop();
    }
}