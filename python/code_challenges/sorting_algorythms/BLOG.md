# Merge Sort Challenge #28

Merge Sorting is a useful algorithm that takes information from an array and sorts it
recursively.

If you have an array or list that needs to be sorted merge sort is handy.

For example:
- [7,1,11,0,2,40,9] will be sorted as [0,1,2,7,9,11,40]

To start, the list will need to be split in half. The function then passes the halves back and recursively sorts them.
- [7,1,11,0,2,40,9] splits to [7,1,11,0] and [2,40,9]

The mid point is found by using the length of the list divided by 2.

This process then happens again with left sort leaving [7,1] and [11,0]

Then the right is done [2,40] and [9]

After the list is split the sort function will then begin comparing the numbers and
moving them left from lowest to highest before merging the sides back together.
