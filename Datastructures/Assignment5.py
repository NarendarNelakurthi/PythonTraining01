def print_function(*args):
    for each_arg in args:
        print(each_arg, sep=" ", end=" ")
    print()

print_function(12, "34", "three", "India", 75, 34, "sdas", 342432, 212.34)
print_function()
def myfunc(**kwargs):
    print(type(kwargs), kwargs)


myfunc()
myfunc(name="Udhay")
myfunc(name="udhay", age=55)

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    sum=pos1+pos2+pos_or_kwd+kwd1+kwd2
    return print(sum)
f(2,3,4,kwd1=5,kwd2=6)

def sum_func(*nums):
    sum=0
    for num in nums:
        sum=sum+num
    return print(sum)
sum_func(10,20,30)

output=[]
def conv_tup(input):
    for item in input:
        if isinstance(item,(list,tuple)):
            output.extend(item)
        else:
            output.append(item)
    return tuple(output)
a=conv_tup(((1,2), 3,4, [5, 6]))
print(a)