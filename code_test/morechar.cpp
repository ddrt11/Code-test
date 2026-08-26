#include <iostream>
int main()
{
    using namespace std;
    char ch = 'M';        //将字符M的ASCII码赋值给ch
    int i = ch;            //将相同的ASCII码存储到int类型变量中
    cout << "The ASCII code for " << ch << " is " << i << endl;

    cout << "Add ont to the character code:" << endl;
    ch = ch + 1;               //修改字符码
    i = ch;                     //将新字符码保存到i
    cout << "The ASCII code for " << ch << " is " << i << endl;   //使用cout.put()成员函数显示字符

    cout << "Displaying char ch using cout.put(ch): ";
    cout.put(ch);                                            //使用cout.put()成员函数显示字符常量
    cout.put('!');
    cout << endl << "Done"<< endl;
    return 0;
}