rows = int(input('enter number of rows :-'))
out =''
for i in range(rows):
    for j in range(rows):
        if i in                                                                 
            out+='    '
        else:
            out+='* '
    out+='\n'
name = input('enter file name:-')
with open(f'{name}.txt','w') as file:
    file.write(out)
    