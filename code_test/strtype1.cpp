#include <iostream>
#include <string>          //使字符串类可用
int main()
{
    using namespace std;
    char charr1[20];                  //创建一个空数组
    char charr2[20] = "jaguar";           //创建一个已初始化的数组
    string str1;                       //创建一个空字符串对象
    string str2 = "panther";            //创建一个已初始化的字符串

    cout << "Enter a kind of feline: ";
    cin >> charr1;
    cout << "Enter another kind of feline: ";
    cin >> str1;
    cout << "Here are some felines:\n";
    cout << charr1 << " " << charr2 << " "
         << str1 << " " << str2 
         << endl;
    cout << "The third letter in " << charr2 << " is "
         << charr2[2] << endl;
    cout << "The third letter in " << str2 << " is "
         << str2[2] << endl;
    return 0;

}