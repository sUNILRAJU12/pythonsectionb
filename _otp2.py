import random
out = []
while len(out)<6:
    out+=[random.choice(['@','#','$','&','!','?'])]
    out+=[chr(random.randint(65,91))]
    out+=[str(random.randint(0,9))]
    