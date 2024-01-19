import random
number = random.randint(10,100)
while True:
    a=int(input('enter a number:-'))
    if a==number:
        print('congrats! you sucessesfully gused the number,a')
        break
    elif a<number:
        print('enter some greater number')
    else:
        print('enter some lesser number')
