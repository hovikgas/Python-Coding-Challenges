'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called pairs_of_ten() that takes a list of integers as an argument.
Return a list of unique integer pairs that sum to 10, represented as tuples, from the input list.
Assume that pairs following this example are unique: (7, 3) and (3, 7).

>>> pairs_of_ten([5, 6, 6, 5, 7, 4, 3, 4])
[(5, 5), (6, 4), (7, 3)]

'''

def pairs_of_ten(int_list):

    foundPairs = []

    for i in range(len(int_list)):

        for j in range(i + 1, len(int_list)):

            if int_list[i] + int_list[j] == 10:

                if (int_list[i], int_list[j]) not in foundPairs:
                    foundPairs.append((int_list[i], int_list[j]))

    return foundPairs


pairs_of_ten([10, 1, 0, 9])


if __name__ == '__main__':
    import doctest
    doctest.testmod()