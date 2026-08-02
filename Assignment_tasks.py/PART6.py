print("PART 6: Lists")

print("To print the list items:")
items = ["Laiba", "banana", "Bismah", "date", "Fajar"]
for item in items:
    print(item)
print("To demostrate if a tuple is mutable:")
t = (1, 2, 3)
print("Original Tuple:", t)
try:
    t[0] = 10
except TypeError:
    print("Tuples are immutable")   
print("To demostrate union and intersection,difference of sets:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
