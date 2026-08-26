#include <iostream>
int main()
    {
        using namespace std;
        int yams[3];         //创建包含三个元素的数组
        yams[0] = 7;         //为第一个元素赋值
        yams[1] = 8;
        yams[2] = 6;

        int yamcosts[3] = {20, 30, 5};     //创建并初始化数组

        cout << "Total yams = ";
        cout << yams[0] + yams[1] + yams[2] << endl;
        cout << "The package with " << yams[1] << " yams costs";
        cout << yamcosts[1] << " cents per yam.\n";
        int total = yams[0] * yamcosts[0] + yams[1] * yamcosts[1];
        total = total + yams[2] * yamcosts[2];
        cout << "The total yam expense is " << total << " cents.\n";
        cout << "\nSize of yams array = " << sizeof yams;
        cout << " bytes.\n";
        cout << "Size of one element = " << sizeof yams[0];
        cout << " bytes.\n";
        return 0;
    }
