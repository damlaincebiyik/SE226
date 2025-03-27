#include <iostream>

double harmonicSeriesRecursive(int n) {
    if (n == 0) {
        return 0.0;
    }
    return 1.0/n + harmonicSeriesRecursive(n - 1);
}

double harmonicSeriesRecursive() {
    int n;
    std::cout << "Enter the value of n: ";
    std::cin >> n;
    return harmonicSeriesRecursive(n);
}

int main() {
    int n = 10;
    double result = harmonicSeriesRecursive(n);
    std::cout << "Harmonic series sum for n = " << n << ": " << result << std::endl;
    
    double overloadedResult = harmonicSeriesRecursive();
    std::cout << "Harmonic series sum (user input): " << overloadedResult << std::endl;

    return 0;
}