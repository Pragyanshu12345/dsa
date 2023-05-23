def subsets(b,a, s, i):
    t = 0
    if (i >= len(s)):
        t = t+1
        b.append(a)
        return t
    else:
        a1 = subsets(b,a.copy(), s, i+1)
        a.append(s[i])
        b1 = subsets(b,a.copy(), s, i+1)
        return a1+b1


b, a, i = [], [], 0
s = [1,2,2]
print(subsets(b,a, s, i))
print(b)
