#include <iostream>
using namespace std;
int main()
{
    using namespace std;
    int chest = 42;
    int waist = 42;
    int inseam = 42;

    cout << "Monsieur cuts a striking figure!" << endl;
    cout << "chest = " << chest << " (decimal for 42)" << endl;
    cout << hex;                    //用于改变数制的操作符
    cout << "waist = " << waist << " (hexadecimal for 42)" << endl;
    cout << oct;                    //用于改变数制的操作符
    cout << "inseam = " << inseam << " (octal for 42)" << endl;
    return 0;
}