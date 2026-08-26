#include <iostream>
int main()
{
    using namespace std;
    int updates = 6;                //声明一个变量
    int * p_updates;                //声明指向整数的指针
    p_updates = &updates;          //将整数的地址赋给指针

    cout << "Values: updates = " << updates;
    cout << ", *p_updates = " << *p_updates << endl;

    cout << "Addresses: &updates = " << &updates;
    cout << ", p_updates = " << p_updates << endl;

    *p_updates = *p_updates + 1;
    cout << "Now updates = " << updates << endl;
    return 0;
}