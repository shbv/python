""" 
Generators: (called a coroutine in other languages)
- Temporarily returns execution to the caller (yields a value) & saves where it last left off. 
- Type of iterator
- Use for memory efficient data processing (large datasets that dont fit in memory)

How to call:  generator_method_instance = generator_method()
    - for loop on generator_method_instance
    - next(generator_method_instance)
"""

def temp_generator():
    yield "first"
    yield "second"
    ix = 0
    l = [1, 2, 3, 4]
    while ix < len(l):        
        yield l[ix]
        ix += 1

"""Using next"""
gen_obj = temp_generator()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
#print(next(gen_obj)) # Raises StopIteration

"""No StopIteration using for loop"""
gen_obj = temp_generator()
for element in gen_obj:
    print(element)

"""
# Used under the hood when we open file:
with open(<file>) as file_obj: 
    for line in file_obj: 
        ...
"""
