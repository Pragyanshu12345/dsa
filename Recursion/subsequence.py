"""finding all subsets for a given list"""


def subsets(b, a, s, i, t):
    if i >= len(s):
        # print(a,t)
        if t == k:
            print(a)
            return True
    a.append(s[i])
    t += s[i]
    if subsets(b, a.copy(), s, i+1, t) is True:
        return True
    a.pop()
    t -= s[i]
    if subsets(b, a.copy(), s, i+1, t) is True:
        return True
    return False


b, a, i = [], [], 0
t = 0
f = 0
k = 2
s = [1, 2, 1]
subsets(b, a, s, i, t)
# print(b)
