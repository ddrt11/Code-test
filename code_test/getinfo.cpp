#include <iostream>

int main()
{
    using namespace std;

    int carrots;

    cout << "How many carrots do you have?" << endl;
    cin >> carrots;                                     //C++ input
    cout <<"Here are two more. ";
    carrots = carrots + 2;                 
// 下一行将输出连接起来
    cout << "Now you have " << carrots << "carrots." << endl;
    return 0l;
}