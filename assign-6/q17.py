set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Original set1:", set1)
print("Original set2:", set2)

set1.intersection_update(set2)

print("\nAfter removing items not common to both sets:")
print("set1:", set1)
print("set2 remains unchanged:", set2)




