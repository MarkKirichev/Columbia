#include "prime.h"

int isPrime(unsigned int number)
{
    if(number == 1) // For this case, even though mathematically incorrect we'll assume that
    {               // 1 is not a prime number for the function to have a return value
        return 0;
    }
    if(number == 2) // Checking 2 since it's an edge case
    {
        return 1;
    }
    if(!(number & 1) && (number & 2))
    {
        return 0;
    }

    // if the number is not 1 and 2 & not divisible by 2,
    // we'll need to implement a for-loop to identify if a number is prime

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

void printIsPrime(unsigned int number)
{
    // Check if the number is prime and print the result
    if(isPrime(number))
    {
        printf("The number %u is a prime number!\n", number);
    }
    else
    {
        printf("The number %u is not a prime number!\n", number);
    }
}