#include <iostream>
#include <locale>
int main() {
float a , b ;
std::cout << "Enter number:: "; //ведення 1 числа
std::cin >> a ;
std::cout << "Enter number:: "; // ведення 2 числа
std::cin >> b ;

char c;
std::cout << "Enter operator:: "; // математична дія 
std::cin >> c;

if (c == '+') {
    std::cout << "Result: " << a + b << std::endl;
} else if (c == '-') {
    std::cout << "Result: " << a - b << std::endl;
} else if (c == '*') {
    std::cout << "Result: " << a * b << std::endl;
} else if (c == '/') {
    if (b != 0) {
        std::cout << "Result: " << a / b << std::endl;
    } else {
        std::cout << "Error: Division by zero!" << std::endl;
    }
} else {
    std::cout << "Invalid operator!" << std::endl;
}
}
