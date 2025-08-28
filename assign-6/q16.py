
A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

common_elements = A.intersection(B, C)
print("Elements common to all three sets:", common_elements)

all_elements = A.union(B, C)
print("Elements present in at least one set:", all_elements)


print("\nAdditional set operations:")

only_A = A - B - C
only_B = B - A - C
only_C = C - A - B
exactly_one = only_A.union(only_B, only_C)
print("Elements in exactly one set:", exactly_one)

in_A_B = A.intersection(B) - C
in_A_C = A.intersection(C) - B
in_B_C = B.intersection(C) - A
exactly_two = in_A_B.union(in_A_C, in_B_C)
print("Elements in exactly two sets:", exactly_two)
