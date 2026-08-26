#include <iostream>
int stonetolb(int);           //函数原型
int main()
{
    using namespace std;
    int stone;                                //声明变量
    cout << "Enter the weight in stone: ";      //输出函数
    cin >>stone;                           //使用cin为stone赋值 输入函数
    int pounds = stonetolb(stone);
    cout << stone << " stone = ";
    cout << pounds << " pounds." << endl;
    return 0;
}

int stonetolb(int sts)
{
    return 20 * sts ;
}