#include <stdio.h>

#include "prime.h"
#include "gcd.h"

int main() {
    // Initializing the variables of type int
    unsigned int firstNumber; // They are unsigned ints since the problem states
    unsigned int secondNumber; // that the numbers will always be positive

    // Reading the user's input
    printf("Please, indicate the 2 integer numbers with a single space in between: ");
    scanf("%u%u", &firstNumber, &secondNumber);

    // Part 1: Calculating the numbers' average
    double averageNumber = (firstNumber + secondNumber) / 2.0;
    printf("Average Number: %f\n", averageNumber);

    // Part 2
    // Calling a function in order to skip code repetition
    printIsPrime(firstNumber);
    printIsPrime(secondNumber);

    // Part 3
    printAreCoprime(firstNumber, secondNumber);

    return 0;
}