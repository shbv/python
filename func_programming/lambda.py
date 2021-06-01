"""
lambda:
- keyword used for anonymous functions
    def func(x):
        return x + 5
    func(100)

        (or)

    (lambda x: x + 5)(100)
"""
print((lambda x: x + 5)(100))

func = lambda x: x + 5
print(func(101))
