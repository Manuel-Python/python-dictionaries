set1 = set(range(0, 100))
print("Set 1 ")
print(set1)

set2 = set()
for n in range(0,10):
    set2.add(n**2)

set2.add(2000)
print("\nSet 2 ")
print(sorted(set2))
print()

set3 = set1.union(set2)
print("\nSet 3 = 1 union 2 ")
print(sorted(set3))
print()

set4 = set1.difference(set2)
print("\nSet 3 = 1 diff 2 ")
print(sorted(set4))
print()

if set4.issubset(set3):
    print("set4 is a subset of set3")

print()
if set3.issuperset(set4):
    print("set3 is a supsetset of set4")

