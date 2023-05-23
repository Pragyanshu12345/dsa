def rev(st, idx):
    if (idx == len(st)-1):
        return st[idx]
    else:
        return rev(st, idx+1)+st[idx]

s = "Pragyanshu"
idx = 0
print(rev(s, idx))
