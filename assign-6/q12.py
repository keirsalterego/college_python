A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_AB = A.union(B) 
print("Union of A and B:", union_AB)

intersection_AB = A.intersection(B) 
print("Intersection of A and B:", intersection_AB)

difference_AB = A.difference(B)  
print("Difference A - B:", difference_AB)

symmetric_diff_AB = A.symmetric_difference(B)  
print("Symmetric difference of A and B:", symmetric_diff_AB)
