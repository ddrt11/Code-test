#include <iostream>
int main()
{
    using namespace std;
    cout.setf(ios_base::fixed, ios_base::floatfield);
    float tree = 3;       //整数换为浮点数
    int guess(3.9832);      //double转换为int
    int debt = 7.2E12;      //C++中未定义结果
    cout << "tree = " << tree << endl;
    cout << "guess = " << guess << endl;
    cout << "debt = " << debt << endl;
    return 0;
}