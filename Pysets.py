myset = {1,2,3,4,5}
setset = {3,4,5,6,7}
print(myset)
print(setset)
print(myset | setset)  # Union
print(myset & setset)  # Intersection
print(myset - setset)  # Difference
print(myset ^ setset)  # Symmetric Difference
print(myset <= setset) # Subset
print(myset >= setset) # Superset
print(myset.isdisjoint(setset)) # Disjoint
myset.add(6)          # Add element 
print(myset)
myset.remove(6)       # Remove element
print(myset)
print(len(myset))    # Length of set
myset.clear()         # Clear set
print(myset)