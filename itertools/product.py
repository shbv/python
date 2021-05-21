from itertools import product

l1 = ['a1', 'a2', 'a3']
l2 = ['b1', 'b2', 'b3']
l3 = ['c1', 'c2', 'c3']
l = [l1, l2, l3]
print(*l)

"""Available function"""
print(list(product(*l)))

"""Custom function"""
def custom_prod(*args):
    # *args allows variable number of args to function & makes it iterator
    # list of lists of elements
    l_all = [l_t for l_t in args] 
    # list of lists for products (result)
    products = [[]]  
    # go over each list
    for l_t in l_all:
        # expand products with its elements appended
        products = [p+[element] for p in products for element in l_t]  
    return products

print(custom_prod(*l))
