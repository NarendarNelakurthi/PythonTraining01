name='Narendar'
numbers=[]
while True:
    number=input('Enter the number ')
    if number=='Narendar':
        break
    else:
        numbers.append(eval(number))
average=sum(numbers)/len(numbers)
print(f'The average is {average}')
