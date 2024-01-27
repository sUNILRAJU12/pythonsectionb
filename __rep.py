import re

with open(r"F:\suresh\suresh1.py\susi.txt",'r+',encoding='utf-8') as file:
    data = file.read()
    newdata=re.sub(' ','_',data)
    file.seek(0)
    file.write(newdata)
