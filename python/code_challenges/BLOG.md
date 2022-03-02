
# Insertion Sort Explanation

## For Starters

Some things we practice data structures over and over.  How to manipulate them and successfully get the outcome we are desiring.  Often times, we understand how to get that outcome but fail to really understand what is happening. I will attempt to explain what is happening in insertion sort.

## Pseudocode

Take this pseudocode for example....

` InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp`

First we will set a variable for the insertion

`FOR i = 1 to arr.length`

Then set a vadriable for i -1

`int j <-- i - 1`

Lastly a temp variable for tracking the array at i

`int temp <-- arr[i]`

Now for the fun part.  The iteration:

While j is greater than or equal to zero and the tem variable is less than the array at i:

`WHILE j >= 0 AND temp < arr[j]`

Array becomes j + 1:

`arr[j + 1] <-- arr[j]`

Array is now j + 1

`arr[j + 1] <-- temp`