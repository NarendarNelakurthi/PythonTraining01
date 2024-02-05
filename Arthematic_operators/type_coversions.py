"""Purpose: Data Type Conversions - int, float, complex, boolean, string, None

    int - decimal       - int() -base 10  (0-9)
        - binary        - bin() -base  2  (0-1)
        - hexadecimal   - hex()
        - octal         - oct()
    floatm
        float()
    String
        str()"""
# Octal -> 0-7
# decimal -> octal
print("oct(9)  ", oct(9))  # '0o11'
print("oct(-23)", oct(-23))  # '-0o27'
# octal -> decimal
print(int(oct(9), base=8))  # 9
print(int("0o11", base=8))  # 9
print(int("11", base=8))  # 9
print(int("11"))  # 11