from itertools import combinations, combinations_with_replacement, permutations

l1 = ['a1', 'a2', 'a3']
l2 = ['b1', 'b2', 'b3']
l3 = ['c1', 'c2', 'c3']

print(list(combinations(l1, 2)))
print(list(combinations_with_replacement(l1, 2)))
print(list(permutations(l1, 2)))

