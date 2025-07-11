def lr(x):
    if x<10:
        print(x)
    else:
        lr(x//10)
        print(x%10)
lr(123)

