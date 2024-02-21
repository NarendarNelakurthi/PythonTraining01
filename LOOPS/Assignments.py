for each_ele,each_e in enumerate([11, 22, 33, 44, 55]):
    print(f"{each_ele} ===> {each_e}") # indexing
print()
for loop_index, each_chr in enumerate("Python", -3):
    print(f"At position {loop_index:2}, character is {each_chr}")
print()
for loop_index,range_num in enumerate(range(10),-10):
    print(f'The index number {loop_index} and range number {range_num}')
for progress in [3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    bar_length=10
    fil_length=int(round((progress*bar_length/100)))
    bar='*'*fil_length+' '*(bar_length-fil_length)
    print(f'[{bar}] {progress}')
i=10
while i:
    j=10
    while j:
        print(f'{i} * {j} = {i*j}')
        j=j-1
    i=i-1
j=1
while j<=10:
    i=1
    row=''
    while i<=10:
        row +=f'{str(i).zfill(2)} * {str(j).zfill(2)} = {str(int(i*j)).zfill(3)} | '
        i=i+1
    print(row)
    j=j+1



