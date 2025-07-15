def natural(x):
    if x==0:
        return x
    natural(x-1)
    print(x)
(natural(0))