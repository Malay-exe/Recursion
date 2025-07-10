def result(n, w, wt, vl):
    if n == 0 or w == 0:
        return 0
    else:
        cvl = vl[n-1]
        cwt = wt[n-1]
        if cwt <= w:
            c1 = cvl + result(n-1, w-cwt, wt, vl)
            c2 = result(n-1, w, wt, vl)
            return max(c1, c2)
        else:
            return result(n-1, w, wt, vl)


n = 3
w = 4
wt = [1,2,3]
vl = [4,5,1]
print(result(n, w, wt, vl))