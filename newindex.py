def even(value,number):
    flag=False
    if value==0:
        flag=True
    return flag 
def sqadd(a,b): 
    return 
def add(a,b):
    return a+b 
def indexvalue(li):
    out=[] 
    for i in range(len(li)):
        if even(i) and even(li[i]): 
            out+=[sqadd(i,li[i])]
        elif even(i) and even(li[i]):
            out+=[sqadd(i,li[i])]
        else:
            out+=[add(i,li[i])]
    return out
print[indexvalue['abcd',(1,2,3)]]

