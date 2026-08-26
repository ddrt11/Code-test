#include <iostream>
#include <cstring>
using namespace std;
char * getname(void);
int main()
{
    char * name;              //创建指针但无储存

    name = getname();              //将字符串的地址赋给name
    cout << name << " at " << (int *) name << "\n";
    delete [] name;              //释放内存

    name = getname();             //重用已释放的内存
    cout << name << " at " << (int *) name << "\n";
    delete [] name;
    return 0;
}

char * getname()
{
    char temp[80];                  //临时储存
    cout << "Enter last name: ";
    cin >> temp;
    char * pn = new char[strlen(temp) + 1];
    strcpy(pn, temp);

    return pn;
}