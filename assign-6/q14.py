# Given lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2)

result = list(common_elements)

print("Common elements:", result)
