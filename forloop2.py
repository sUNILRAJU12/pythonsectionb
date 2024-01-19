string=input('enter a string')
out=' '
for char in string:
    if char not in out:
        out+out+char
        print(out)