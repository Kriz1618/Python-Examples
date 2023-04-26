def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

arr = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x+y, arr))