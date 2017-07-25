'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called pairs_of_ten() that takes a list of integers as an argument.
Return a list of unique integer pairs that sum to 10, represented as tuples, from the input list.
Assume that pairs following this example are unique: (7, 3) and (3, 7).

>>> pairs_of_ten([5, 6, 6, 5, 7, 4, 3, 4]) == {(6, 4), (5, 5), (7, 3)}
True

'''

def pairs_of_ten(intlist):

    foundPairs = []

    for i in range(len(intlist)):

        for j in range(i + 1, len(intlist)):

            if intlist[i] + intlist[j] == 10:
                foundPairs.append((intlist[i], intlist[j]))

    return set(foundPairs)


pairs_of_ten([10, 1, 0, 9])


if __name__ == '__main__':
    import doctest
    doctest.testmod()