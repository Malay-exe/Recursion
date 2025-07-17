def rev(st):
    if len(st)==0:
        return st
    return rev(st[1:])+st[0]
print(rev('malay'))