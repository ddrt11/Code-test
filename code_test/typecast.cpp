#include <iostream>
int main()
{
    using namespace std;
    int auks, bats,coots;

    //下面这些语句将值作为双精度数相加
    //然后将结果转换为整数相加
    auks = 19.99 + 11.99;

    //这些语句将值作为整数相加
    bats = (int) 19.99 + (int) 11.99;     //旧C语法
    coots = int (19.99) + int (11.99);    //新C++语法
    cout << "auks = " << auks << ", bats = " << bats;
    cout << ", coots = " << coots << endl;

    char ch = 'Z';
    cout << "The code for " << ch << " is ";    //以字符形式输出
    cout << int(ch) << endl;                   //以整数形式输出
    cout << "Yes, the code is ";
    cout << static_cast<int>(ch) << endl;
    return 0;
}