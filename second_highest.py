"""
1. Integer Array Element stored in random order (unsorted)
2. 2nd highest elemnt from the array.
3. We cannot use inbuilt library or sorting package
"""

a = [20, 15, 1, 12, 4, 5, 3, 20, 20]

highest = 0

second = 0

for i in a:
    if highest < i:
        second = highest
        highest = i
    elif second < i and highest != i:
        second = i

print("highest: ", highest, "second: ",second)