#include "gcd.h"

int euclideanAlgorithm(unsigned int firstNumber,
                       unsigned int secondNumber)
{
    // Implementing the Euclidean Algorithm
    // https://sites.math.rutgers.edu/~greenfie/gs2004/euclid.html
    int remainder;
    while ((firstNumber % secondNumber) > 0)
    {
        remainder = firstNumber % secondNumber;
        firstNumber = secondNumber;
        secondNumber = remainder;
    }
    return secondNumber;
}

void printAreCoprime(unsigned int firstNumber,
                     unsigned int secondNumber)
{
    // Check if the number is prime and print the result
    if(euclideanAlgorithm(firstNumber, secondNumber) == 1)
    {
        printf("The numbers %u and %u are coprime!\n", firstNumber, secondNumber);
    }
    else
    {
        printf("The numbers %u and %u are not coprime!\n", firstNumber, secondNumber);
    }
}
