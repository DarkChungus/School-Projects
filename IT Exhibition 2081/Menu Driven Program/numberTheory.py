import math
import time
import sys

def nt_problems():
    """
    Some functions on number theory. For more help with the actual functions, please do call the respective
    functions themselves. The two problems we have here are:
    --------------------------
    1. Perfect Number Searcher
    2. Mersenne Prime Searcher
    --------------------------
    :return:
    """
    def is_prime(num):
        """
        This is a very fast way to check if a number is prime, rather than just checking using the Sieve of
        Eratosthenes. You can just set the upper range to be the square root of the number, since there will
        be no factors greater than the square root of the number if the number does happen to be a prime.
        :param num:
        :return:
        """
        x = 0
        for i in range(1, int(math.sqrt(num)) + 1): # Fast method to check if a number is prime
            if num % i == 0:
                x += 1

        if x == 2:
            return True
        else:
            return False

    def search_pn(n):
        """
        A perfect number is that number that is equal to the sum of it's divisors. An example of a perfect
        number is:

        =====================
        6 = 3 + 2 + 1
        =====================

        The first few perfect numbers are 6, 28, 496, 8128, ...
        For this, I just implemented a quick way to get all the sums of the factors, by only iterating through
        the first n/2 terms, because there are no proper factors of a number that is greater than the number
        divided by 2.

        :param n: The limit for the search of the perfect number.
        :return:
        """
        for k in range(2, n):
            x = 0 # Sum of the factors
            for i in range(1, int(k / 2) + 1): # Go through the factors of k
                if k % i == 0: # Is i a factor of k?
                    x += i # Get the sum of the factor

            if x == k: # If the sum of the divisors is equal to the actual number.
                print(f'YES! {k} is a perfect number!')

    def search_mersenne(n):
        """
        A Mersenne Prime is any prime number that can be represented in the way: 2^p-1, where p is also
        another prime number. Here I just did a typical brute force method to find the Mersenne Primes,
        although a way faster method would be to implement the Sieve of Eratosthenes.

        :param n: The limit for the search of the Mersenne Prime.

        :return:
        """
        for i in range(1, n):
            if is_prime(i): # Is the number prime?
                possible = (2 ** i - 1) # The form of a Mersenne Prime
                if is_prime(possible): # Is the number we formed a Mersenne Prime?
                    print(f'{i} is a Mersenne prime!')

    # Printing the options

    print("1. Perfect Number Searcher")
    time.sleep(.5)
    print("2. Mersenne Prime Searcher")
    time.sleep(.5)
    print()
    print()
    time.sleep(.5)
    choose = input("Type out which one you would like to use: ").lower()

    # Conditions

    if choose[0] == 'p':
        # Taking the required input
        n = int(input("Enter maximum limit for the Perfect Number Search: "))
        search_pn(n)
        done = True
    elif choose[0] == 'm':
        # Taking the required input
        n = int(input("Enter maximum limit for the Mersenne Prime Search: "))
        search_mersenne(n)
        done = True
    else:
        # Invalid input case(reloads the program)
        print("Sorry! You have an invalid input.")
        time.sleep(1)
        print("Program reloading...")
        time.sleep(.5)
        nt_problems()
        done = False

    if done:
        sys.exit() # Closes the program
    else:
        nt_problems() # Recall the program if the user input an invalid option.
