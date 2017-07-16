''' Write a funciton called fizzbuzz, which takes a number (n) as an argument and returns a list. 
For each integer between 1 and n, if the integer is divisible by 3, append "buzz" 
to the result list. If the integer is divisible by 5, append "fizz" to the result list. 
If the integer is divisible by both 3 and 5, append "fizzbuzz" to the result list. 
'''

def fizzbuzz(n):

    result = []

    for i in range(1, n):

        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')

        elif i % 3 == 0:
            result.append('Fizz')

        elif i % 5 == 0:
            result.append('Buzz')

        else:
            result.append(i)

    print(result)
    return result


fizzbuzz(99)


    