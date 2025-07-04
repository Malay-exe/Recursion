def count(x):
    if x==0:
        return x
    return 1+count(x//10)
print(count(12345))