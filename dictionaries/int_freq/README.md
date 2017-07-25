## Counting integer frequencies in a list

### Concepts covered
* Defining a function
* Adding keys to dictionaries
* Comparing an integer to dictionary keys
* Incrementing values in dictionaries
* The `.items()` dictionary method
* Indexing into tuples
* Using the `range()` function
* For-loops
* Indexing into a list
* Returning a dictionary key with the highest value
* Returning None

### Explanation of `int_freq_solution.py`

> Remember: If you run the solution file in your Terminal, the embedded doctests will "succeed silently" and there will be no output to the Terminal. You can add print statements throughout the code to better understand what is happening. But, if you add print statements, the doctests will fail and you'll see a failure report print to the Terminal.

**Line 20:** Define a function called `int_frequency()` that takes in a parameter called `intlist`.

**Line 22:** Initialize a variable called `int_freq_dict`, which is bound to an empty dictionary. We'll use this dictionary later to store the integers in `int_list` as keys, and the number of times each integer appears in `int_list` will be each key's associated value.

**Line 25:** A feature of Python is that a list with at least one item in it evaluates to True, and an empty list evaluates to False. Here, we are only running the code that follows if the list has at least one item in it. Scroll down to Line 50 for the else statement that is paired with the if statement on Line 25.

**Line 27:** Create a for-loop whose iterator is the variable `i`. The `len()` method returns the length of the object passed to it as an argument. In this case, the argument is `intlist`. So, it'll return a number that describes how many items are in the list. This returned number then becomes the argument that is passed into the `range()` function. The `range()` function [returns a list of integers](http://pythoncentral.io/pythons-range-function-explained/), starting at zero by default. The list contains as many integers as are passed in as the argument. For example, `range(3)` would return this list: `[0, 1, 2]` which has 3 items within it. The iterator `i` will begin in the for-loop as the value at the 0th element of the list which was returned by the range function (0, in our example), and its index number will increment by 1 each time through the loop. 

Because we passed in the length of `intlist` as the argument to the `range()` function, the `range()` function will only return a list that has as many items in it as there are items in `intlist`. This ensures that we'll access every item in `intlist`, and it also ensures that we won't try to access an index beyond the length of the string. (If we tried to do that, we'd get an IndexError.)

**Lines 29-30:** If the integer currently at the index `intlist[i]` is **not** already a key in the `int_freq_dict` dictionary, create a new key-value pair with `intlist[i]` as the key and give it a value of 1. We start the value at 1, not zero, since the program is seeing this integer for the first time and it counts as 1 appearance.

**Lines 32-33:** If the integer currently at the index `intlist[i]` is already a key in the `int_freq_dict` dictionary, increment its associated value by 1. Because this is the last line of executable code within the for-loop, Python will automatically increment the index of `intlist` by 1, and the if/else comparison will be run on the next integer in `intlist`.

**Lines 35-36:** Now that the for-loop has cataloged the frequency of each integer in `int_list` into the `int_freq_dict` dictionary, we need to isolate the integer that appears most frequently so we can return that integer later. We can do this by isolating the key-value pair that has the highest value. This will represent the key containing the integer that appeard most often, and the value containing the number of times the integer appears in `intlist`. 

We can do this by calling the `.items()` dictionary method on the `int_freq_dict` dictionary. The `.items()` method returns a list of tuples, and inside each tuple is a key-value pair from the dictionary. The key is stored in the 0th index of the tuple (eg: `my_tuple[0]`) and the value is stored in the 1st index of the tuple (eg: `my_tuple[1]`). We're saving this output list to a variable called `freq_data`.

**Lines 38-39:** Initialize two variables that we'll use to store values temporarily as we loop through `freq_data` in the next bit of code. Both the `temp_freq` and `temp_num` variables are initialized to zero so that when we compare the positive numbers we'll access in `freq_data`, the zero is always less than whatever number we're accessing.

**Line 41:** Define a for-loop to access every item in `freq_data`. Remember, every item in `freq_data` is a tuple.

**Line 43-45:** Recall that each tuple represents 1) A key, which is stored in the 0th index of the tuple (eg: `my_tuple[0]`), and 2) A value, which is stored in the 1st index of the tuple (eg: `my_tuple[1]`). 

For each tuple in `freq_data`, if the value it holds at pair[1] is greater than the integer `temp_freq` is bound to, we replace the integer that `temp_freq` is bound to with whatever integer is found at pair[1]. We do this because we want to return the integer that appears most frequently.

For each tuple in `freq_data`, if the key it holds at pair[0] is greater than the integer `temp_num` is bound to, we also replace the integer that `temp_num` is bound to with whatever integer is found at pair[0]. We do this because we want to return the integer that appears most frequently.

In doing this, we are ensuring that both `temp_freq` and `temp_num` always hold the key-value pair with the highest value.

**Line 47:** Return the final version of the `temp_num` variable, which contains the integer that appears most frequently in `intlist`.

**Lines 50-51:** If the list is empty, return None.

**Line 54:** Remember to call your function!

> Just for fun, try changing the argument that gets passed in when the function is run on line 31. Can you find an input that causes an error? If so, try to write some code into the function to "catch" those situations.

### Submitting Alternative Solutions
If you've created a solution to this coding challenge that is materially different than the one(s) already here, please submit a pull request for your new Python file, which should be named `count_letters_solution<#>.py`. Replace <#> with the number that is one greater than the current number of solution files. Please also edit this README to include a new header and a line-by-line walkthrough of your solution as shown above. View the raw code of the README to duplicate the markdown styling.

### Reporting Errors
Please submit a new issue if you encounter any errors in the solution(s).
