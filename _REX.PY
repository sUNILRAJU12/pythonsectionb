import re
pattern='[Tt][Nn][ ]?[0-3][1-9][ ]?[a-zA-Z][ ]?[0-9]{4}'
data = 'TN 03 z 1055'
data=re.findall(pattern,data)
print(data)
