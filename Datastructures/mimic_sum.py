# Assignment: mimick sum() builtin function with
#  a. user-defined function
#  b. using reduce
# """
# print(sum((1, 23, 23, 2)))
# print(sum([(1, 2), (3,), (9, 1)], ()))
# print(sum([[1, 2], [3, 4]], []))
from functools import reduce

def mimic_sum(iter):
    sum=0
    for item in iter:
        if isinstance(item,(list,tuple)):
            if len(item)>0:
                for i in range(len(item)):
                    sum=sum+item[i]
            else:
                continue
        else:
            sum=sum+item
    return sum
print(mimic_sum((1, 23, 23, 2)))
print(mimic_sum([(1, 2), (3,), (9, 1), ()]))
print(mimic_sum([[1, 2], [3, 4], []]))
itera=[(1, 23, 23, 2),[(1, 2), (3,), (9, 1), ()],[[1, 2], [3, 4], []]]
result=[]
def mimic_sum(itera):
    
    for iter in itera:
      output=[]
      for item in iter:
        if isinstance(item,(list,tuple)):
                output.extend(item)
        else:
            output.append(item)
      result.append(output)
    return result
results=[]
def sum_mimic2(a):
    for i in a:
        print(i)
        results.append(reduce(lambda x,y:x+y,i))
    return results
b=sum_mimic2(mimic_sum(itera))
print(b)
        

