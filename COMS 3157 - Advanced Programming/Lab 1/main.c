#include <stdio.h>

int isPrime(int number);
void printIsPrime(int number);
int euclideanAlgorithm(int firstNumber, int secondNumber);
void printAreCoprime(int firstNumber, int secondNumber);

int main() {
    // Initializing the variables of type int
    unsigned int firstNumber; // They are unsigned ints since the problem states
    unsigned int secondNumber; // that the numbers will always be positive

    // Reading the user's input
    printf("Please, indicate the 2 integer numbers with a single space in between: ");
    scanf("%d%d", &firstNumber, &secondNumber);

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

int isPrime(int number)
{
    if(number == 1) // For this case, even though mathematically incorrect we'll assume that
    {               // 1 is not a prime number for the function to have a return value
        return 0;
    }
    if(number == 2) // Checking 2 since it's an edge case
    {
        return 0;
    }

    // if the number is not 1 and 2, we'll need to implement a for-loop to identify if a number is prime

    // we will initialize a long long number to iterate over
    // this is needed because if our number is not a prime number, then it must
    // have a divisor which is less than or equal to sqrt(number)
    // therefore, we will need our iterating number to be large enough
    // not to cause integer overflow and, thus, we'll need a long long number
    long long i;
    for(i = 3; i * i <= number; i += 2) // we can start with 3 and increment by 2 each time because of
    {                                   // the 2 if statements above, allowing us to reduce the overall complexity
        if(!(number % i))
        {
            return 0;
        }
    }

    // if the for-loop is complete and the function has not returned 0, then the number is prime
    return 1;
}

void printIsPrime(int number)
{
    // Check if the number is prime and print the result
    if(isPrime(number))
    {
        printf("The number %d is a prime number!\n", number);
    }
    else
    {
        printf("The number %d is not a prime number!\n", number);
    }
}

int euclideanAlgorithm(int firstNumber, int secondNumber)
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

void printAreCoprime(int firstNumber, int secondNumber)
{
    // Check if the number is prime and print the result
    if(euclideanAlgorithm(firstNumber, secondNumber) == 1)
    {
        printf("The numbers %d and %d are coprime!\n", firstNumber, secondNumber);
    }
    else
    {
        printf("The numbers %d and %d are not coprime!\n", firstNumber, secondNumber);
    }
}