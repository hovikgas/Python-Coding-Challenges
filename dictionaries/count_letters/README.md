## Counting character frequencies in a string

### Explanation of Solution 1: `count_letters_solution.py`

> Remember: If you run the solution file in your Terminal, the embedded doctests will "succeed silently" and there will be no output to the Terminal. You can add print statements throughout the code to better understand what is happening. But, if you add print statements, the doctests will fail and you'll see a failure report print to the Terminal.

**Line 15:** Define a function called `my_chars()` that takes in a parameter called `my_string`.

**Line 17:** Initialize a variable called `char_count`, which is bound to an empty dictionary. We'll use this dictionary later to store the characters in `my_string` as keys, and the number of times each character appears in `my_string` will be each key's associated value.

**Line 19:** Create a for-loop whose iterator is the variable `i`. The `len()` method returns the length of the object passed to it as an argument. In this case, the argument is `my_string`. So, it'll return a number that describes how many characters are in the string. This returned number then becomes the argument that is passed into the `range()` function. The `range()` function [returns a list of integers](http://pythoncentral.io/pythons-range-function-explained/), starting at zero by default. The list contains as many integers as are passed in as the argument. For example, `range(3)` would return this list: `[0, 1, 2]` which has 3 items within it. The iterator `i` will begin in the for-loop as the value at the 0th element of the list which was returned by the range function, and its index number will increment by 1 each time through the loop. Because we passed in the length of `my_string` as the argument to the `range()` function, the `range()` function will only create as many indexes as there are characters in `my_string`. This ensures that we'll access every character in `my_string`, and it also ensures that we won't try to access anything beyond the length of the string. (If we tried to do that, we'd get an IndexError.)

**Line 21-22:** If the character currently at the index `my_string[i]` is already a key in the `char_count` dictionary, increment its associated value by 1.

**Lines 24-25:** If the character currently at the index `my_string[i]` is **not** already a key in the `char_count` dictionary, create a new key-value pair with `my_string[i]` as the key and give it a value of 1. We start the value at 1, not zero, since the program is seeing this character for the first time and it counts as 1 appearance. Because this is the last line of executable code within the for-loop, Python will automatically increment the index of `my_string` by 1, and the if/else comparison will be run on the next character. 

**Line 29:** Return the final version of the `char_count` dictionary, which contains the frequency that each character appears in `my_string`.

**Line 31:** Remember to call your function!

> Just for fun, try changing the argument that gets passed in when the function is run on line 31. Can you find an input that causes an error? If so, try to write some code into the function to "catch" those situations.

### Submitting Alternative Solutions
If you've created a solution to this coding challenge that is materially different than the one(s) already here, please submit a pull request for your new Python file, which should be named `count_letters_solution<#>.py`. Replace <#> with the number that is one greater than the current number of solution files. Please also edit this README to include a new header and a line-by-line walkthrough of your solution as shown above. View the raw code of the README to duplicate the markdown styling.

### Reporting Errors
Please submit a new issue if you encounter any errors in the solution(s).
