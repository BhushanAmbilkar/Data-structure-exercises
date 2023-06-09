# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

# Given:

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]

# Show Hint
# Use list slicing

# Show Solution
# To access a range of items in a list, use the slicing operator :. With this operator, you can specify where to start the slicing, end, and specify the step.

# For example, the expression list1[ start : stop : step] returns the portion of the list from index start to index stop, at a step size step.

# for 1st list: Start from the 1st index with step value 2 so it will pick elements present at index 1, 3, 5, and so on
# for 2nd list: Start from the 0th index with step value 2 so it will pick elements present at index 0, 2, 4, and so on

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)
