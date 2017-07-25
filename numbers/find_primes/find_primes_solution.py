'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called find_primes() that takes an integer argument, n,
and returns a list of all the prime numbers between 2 and n, inclusive.

>>> find_primes(25)
[2, 3, 5, 7, 11, 13, 17, 19, 23]

'''

def find_primes(n):

    primes = []

    for i in range(2, n + 1):

        prime = True 

        for j in range(2, i - 1):  

            if (i % j == 0):
                prime = False

        if prime:
            primes.append(i)

    return primes


find_primes(1000)


if __name__ == '__main__':
    import doctest
    doctest.testmod()