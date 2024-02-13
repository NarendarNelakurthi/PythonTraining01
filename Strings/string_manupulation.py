example="today is good day"
print(example.split())
output=[]
for i in example.split():
    output.append(i[::-1])
print(output)
example_output=' '.join(output)
print(example_output)
str1="1234½"
str2="12356"
print(str1.isdigit())
print(str2.isdigit())
print(str1.isnumeric())
print(str2.isnumeric())
x="aaaaaaaaaaa".replace('a','b',2)
print(x[::-1])
def caesar_cipher(text,shift):
    out_str=""
    for ch in text.lower():
        out_str += chr((ord(ch) + shift-97) % 26+97)
    return out_str
print(caesar_cipher("ABC",3))
int1 = 76
int2 = 42
print(f"{int1 == int2 =}")
print(f"{int1 >  int2 =}")
print(f"{int1 >= int2 =}")
print(f"{int1 <  int2 =}")
print(f"{int1 <= int2 =}")
print(f"{int1 != int2 =}")
print()
int1 = 7.7
int2 = 4.2
print(f"{int1 == int2 =}")
print(f"{int1 >  int2 =}")
print(f"{int1 >= int2 =}")
print(f"{int1 <  int2 =}")
print(f"{int1 <= int2 =}")
print(f"{int1 != int2 =}")
print()
print("bool(0.00000000)  ", bool(0.00000000))
print("bool(0.000000001) ", bool(0.000000000000000000001))
print("bool(-0.000000001)", bool(-0.00000000000000000001))
print()
for number in range(45,137):
    if number % 2 == 0:
      print(f"{number} is EVEN")
    else:
       print(f"{number} is ODD")

vowel_input=input("Enter the character ").strip()
if len(vowel_input)==1 and vowel_input.isalpha():
    if vowel_input.lower() in ('a','e','i','o','u'):
        print(f'The given character {vowel_input} is vowel')
    else:
        print(f'The given character {vowel_input} is not vowel')
else:
    print(f' It is not a alphabet')
cel_input = input("Enter temperature in Celsius ").strip()
if cel_input.replace('.','').isdigit():  
    celsius = float(cel_input)
    fahrenheit = (1.8 * celsius) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
else:
    print("Invalid input")
year=int(input("Enter the year"))
if year%2 != 0:
    print("It is a common year")
elif year%100 != 0:
    print("It is a leap year")
elif year%400 != 0:
    print("It is a common year")
else:
    print('it is a leap year')

import sys

# units_consumed = 357
units_consumed = float(input("Enter the no. of units consumed:").strip())


if units_consumed < 0:
    print("INVALID INPUT")
    sys.exit(1)

# NOTE: Prefer to use if-Guarded clause to make code syntax simple
# cylcometric complexity should be as much less as possible
    
print(f"{units_consumed =}")

amount = 0
remaining_units = units_consumed
if units_consumed > 250:
    slab_units = remaining_units - 250
    amount += slab_units * 10.0
    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
        """
    )
    remaining_units -= slab_units


if 150 < remaining_units <= 250:
    slab_units = remaining_units - 150
    amount += slab_units * 7.0
    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )
    remaining_units -= slab_units


if 100 < remaining_units <= 150:
    slab_units = remaining_units - 100
    amount += slab_units * 4.0

    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )
    remaining_units -= slab_units



if 60 < remaining_units <= 100:
    slab_units = remaining_units - 60
    amount += slab_units * 2.0

    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )
    remaining_units -= slab_units



if 0 <= remaining_units <= 60:
    slab_units = 60  # minimum charge
    amount += slab_units * 1.25

    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )


print(f"Total Billable Amount: {amount}")
electricity_cess = amount*0.02
discount= amount*0.0111
total_amount=amount+electricity_cess-discount
total_gst=total_amount*0.07
print(f"Total Billable Amount After gst: {round(total_amount+total_gst,2)}")









    