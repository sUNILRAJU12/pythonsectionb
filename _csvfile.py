import csv
with open('new.csv','w',newline='') as csvfile:
    fieldnames=['id','name','age']
    record=csv.DictWriter(csvfile,fieldnames)
    record.writeheader()
    data=[
        {'id':1,'name':'rajesh','age':18},
        {'id':2,'name':'rakul','age':12},
        {'id':3,'name':'kal','age':18},
    ]
    record.writerows(data)

with open('new.csv','r',newline='') as file:
    record=csv.DictReader(file)
    for i in record:
        print(i)