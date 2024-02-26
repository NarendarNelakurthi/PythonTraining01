# def prime_number(num):
#     if num%2==0 or num%3==0:
#         pass
#     else:
#         return num
# x=list(map(prime_number,range(1208,4893)))
# print(x)
# odd_nums3 = list(map(lambda x: x *2, range(9)))
# print(odd_nums3)

# odd_nums3 = list(filter(lambda x: x *2, range(9)))
# print(odd_nums3)

# def prime_number(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     else:
#         return True
# x=list(filter(prime_number,range(1208,4893)))
# print(x)
from functools import reduce
import itertools
print(list(map(lambda x, y: x + y, [1, 2, 3, 4], (11, 22, 33))))
print(list(map(lambda x, y, z: x + y, "abcd", "zyx", [1, 2, 3])))
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
