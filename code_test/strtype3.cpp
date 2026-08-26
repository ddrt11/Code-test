#include <iostream>
#include <string>                   //引入字符串类
#include <cstring>                   
int main()
{
    using namespace std;
    char charr1[20];
    char charr2[20] = "jaguar";
    string str1;
    string str2 = "panther";

    str1 = str2;                 //将str2复制到str1
    strcpy(charr1, charr2);

    str1 += " paste";     //将paste添加到str1末尾
    strcat(charr1, " juice");

    int len1 = str1.size();          //获取str1的长度
    int len2 = strlen(charr1);

    cout << "The string " << str1 << " contains "
         << len1 << " characters.\n";
    cout << "The string " << charr1 << " contains "
         << len2 << " characters.\n";
    return 0; 

}