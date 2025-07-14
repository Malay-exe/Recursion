def subsets(lst):
    if not lst:
        return [[]]
    r = subsets(lst[1:])
    print(r)
    return r + [[lst[0]] + i for i in r]
print(subsets([1,2,3,4]))