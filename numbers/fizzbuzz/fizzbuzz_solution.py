'''
Solution by GitHub user @allardbrain in July 2017.

Write a funciton called fizzbuzz() which takes a number (n) as an argument and returns a list. 
For each integer between 1 and n, if the integer is divisible by 3, append "Fizz" 
to the result list. If the integer is divisible by 5, append "Buzz" to the result list. 
If the integer is divisible by both 3 and 5, append "FizzBuzz" to the result list. If the integer
is not evenly divisible by 3 or 5, append the integer itself to the result list.

>>> fizzbuzz(15)
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

'''

def fizzbuzz(n):

    result = []

    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')

        elif i % 3 == 0:
            result.append('Fizz')

        elif i % 5 == 0:
            result.append('Buzz')

        else:
            result.append(i)

    return result


fizzbuzz(100)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


    