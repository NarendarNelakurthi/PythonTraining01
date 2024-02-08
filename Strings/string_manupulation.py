example="today is good day"
print(example.split())
output=[]
for i in example.split():
    output.append(i[::-1])
print(output)
example_output=' '.join(output)
print(example_output)
str1="²³½"
str2="12356"
print(str1.isdigit())
print(str2.isdigit())
print(str1.isnumeric())
print(str2.isnumeric())
x="aaaaaaaaaaa".replace('a','b',2)
print(x[::-1])

    