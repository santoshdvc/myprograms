sum=int(0)
list1=[]
sum1=int(0)
done=False
while not done:
    list1.append(tuple(input('enter the value as d,amount or c,amount else will be not consider as transaction').split(',')))
    choice=eval(input('Enter your choice to add more Transaction 1/0: '))
    if choice==1:
        done=False
    else:
        done=True
tup=tuple(list1)
for e in tup:
    if e[0]=='d':
        sum=sum+int(e[1])
    elif e[0]=='c':
        sum1=sum1+int(e[1])
d1={'d':sum,'c':sum1}
if d1['d']>d1['c']:
    print('Debited Amount Is Greater Than Your Credited Amount...')
    print('Your Balance is: ')
    print(d1['c']-d1['d'])
elif d1['d']<d1['c']:
    print('Debited Amount Is Less Than Your Credited Amount...')
    print('Your Balance is: ')
    print(d1['c']-d1['d'])
elif d1['d']==d1['c']:
    print("Debited === Credited")
    print('Current Balance is: ')
    print(d1['c']-d1['d'])
else:
    pass
