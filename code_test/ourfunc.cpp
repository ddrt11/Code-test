#include <iostream>
void simon(int);               //Simon()函数的原型

int main()
{
    using namespace std;
    simon(3);                 //调用Simon（）函数
    cout << "Pick an unteger: ";
    int count;
    cin >> count;
    simon(count);              //再次调用
    cout << "Done!" << endl;
    return 0;
}

void simon(int n)             //定义Simon（）函数
{
    using namespace std;
    cout << "Simon says touch your toes " << n << " times." <<endl;
}                                               //无返回值函数无需返回语句