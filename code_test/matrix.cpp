#include <iostream>
using namespace std;

const int MAX = 100;

void inputMatrix(int mat[MAX][MAX], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> mat[i][j];
        }
    }
}

void printMatrix(int mat[MAX][MAX], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << mat[i][j] << "\t";
        }
        cout << endl;
    }
}

void multiplyMatrices(int A[MAX][MAX], int B[MAX][MAX], int result[MAX][MAX],
                      int r1, int c1, int r2, int c2) 
            {

    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            result[i][j] = 0;
        }
    }
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            for (int k = 0; k < c1; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int A[MAX][MAX], B[MAX][MAX], result[MAX][MAX];
    int r1, c1, r2, c2;

    cout << "===== Matrix Multiplication Program =====" << endl;

    cout << "\nEnter rows and columns for Matrix A: ";
    cin >> r1 >> c1;
    cout << "Enter elements of Matrix A:" << endl;
    inputMatrix(A, r1, c1);

    cout << "\nEnter rows and columns for Matrix B: ";
    cin >> r2 >> c2;
    cout << "Enter elements of Matrix B:" << endl;
    inputMatrix(B, r2, c2);

    if (c1 != r2) {
        cout << "\nError: Columns of A != Rows of B. Cannot multiply!" << endl;
        return 1;
    }

    multiplyMatrices(A, B, result, r1, c1, r2, c2);

    cout << "\nMatrix A:" << endl;
    printMatrix(A, r1, c1);

    cout << "\nMatrix B:" << endl;
    printMatrix(B, r2, c2);

    cout << "\nResult Matrix (A * B):" << endl;
    printMatrix(result, r1, c2);

    return 0;
}