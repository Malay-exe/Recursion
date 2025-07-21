def sd(x):
    if x<10:
        return x
    return x%10+sd(x//10)
print(sd(1234))
