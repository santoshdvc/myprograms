num=eval(input('Enter the Number of records'))
list1=[tuple(input('Enter the Name,Age,Height in comma seprated form').split(','))for i in range(num)]
print('List of tuples Befor: ')
print(list1)
list1.sort()
print(list1)

