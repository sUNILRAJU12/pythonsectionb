a= 'hello_my-name_is_sandhya'                                                                                                                                                                                                                                                                                                                         
i=0
out=' '
temp=True
while i<len(a):
    if  a[i]==' ':
        temp=True
    elif temp and 'a'<= a[i]<='2':
        out+=chr(ord(a[i])-32)
    else:
        out+=a[i]
        temp=False
    i+=1
print(out)