print('Implement the stack mechanism - LIFO')
my_list=[]
list_size=int(input('Enter the list size '))
i=1
while i<=list_size:
    i +=1
    element=input('Enter the Element = ')
    my_list.append(element)
print(f'{my_list = } and the list size is = {len(my_list)}')
while len(my_list):
    print(f' The Deleted number is = {my_list.pop()}')
print(f'{my_list = } and the list size is = {len(my_list)}')

print('\n')
print('Implement the stack mechanism - FIFO')

my_list=[]
list_size=int(input('Enter the list size'))
i=1
while i<=list_size:
    i +=1
    element=input('Enter the Element = ')
    my_list.insert(0,element)
print(f'{my_list = } and the list size is = {len(my_list)}')
while len(my_list):
    print(f' The Deleted number is = {my_list.pop()}')
print(f'{my_list = } and the list size is = {len(my_list)}')
