a=' '
out=' '
for i in range(len(a)):
    if a[i] in a[i+1:]:
        if a[i] not in out:
            out+=a[i]
            print(out)