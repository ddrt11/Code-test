#include <iostream>
#include <cstring>     //用于strlen（）的函数
int main()
{
    using namespace std;
    const int Size = 15;
    char name1[Size];                       //空数组
    char name2[Size] = "C++owboy";        //  已初始化的数组

    cout << "Howdy! I'm " << name2;
    cout << "! What's your name?\n";
    cin >> name1;
    cout << "Well, " << name1 << ", your name has ";
    cout << strlen(name1) << " letters and is stored\n";
    cout << "in an array of " << sizeof(name1) << " bytes.\n";
    cout << "Your initial is " << name1[0] << ".\n";
    name2[3] = '\0';                    //设置为空字符
    cout << "Here are the first 3 characters of my name: ";
    cout << name2 << endl;
    return 0;
}