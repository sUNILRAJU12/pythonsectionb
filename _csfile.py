import csv
with open('sample.csv','w')as file:
    data=[
        [1,'sandhya'],
        [2,'sandy'],
        [3,'sandhya'],
        ]
    record=csv.writer(file)
    record.writerows(data)
    
