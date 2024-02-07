#!/usr/bin/python3
"""
Purpose: String Operations
    Strings can be represented using
        1) single quotes,
        2) double quotes, or
        3) triple single quotes or
        4) triple double quotes

    PEP 8 -> use triple double quotes for doc-strings

"""

# String with single quotes
language = 'Python Programming'
print(language, type(language))

# String with double quotes
language = "Python Programming"
print(language, type(language))


# String with triple single quotes
language = '''Python Programming'''
print(language, type(language))


# String with triple double quotes
language = """Python Programming"""
print(language, type(language))
#!/usr/bin/python3
"""
Purpose: Importance and usage of multiple quotes
"""
language = 'Python Programming'
print(language, type(language))

question = 'How are you?'
print(question, type(question))

# where_abouts = 'whats' up! friend!!' 
# SyntaxError: unterminated string literal (detected at line 11)

where_abouts = 'whats` up! friend!!' 
print(where_abouts, type(where_abouts))

where_abouts = 'whats\' up! friend!!' 
print(where_abouts, type(where_abouts))
# NOTE 1: Placing \ before any operator with result
# in treating operator as a ordinary character

other_string = 'What\'s going in yours\' in-laws\' house'
print(other_string, type(other_string))

other_string = "What's going in yours' in-laws' house"
print(other_string, type(other_string))

# some_other_string = "What's up in yours' daugther's "wedding""
some_other_string = '''What's up in yours' daugther's "wedding"'''
print(some_other_string, type(some_other_string))

some_other_str = """ python -c 'awdwad' asdss "sfdsdfd", '''dedfdfwef sd -m jd;jd''' """
print(some_other_str)

print("\n\n")
# '\''
# "'"
# '"'
# ''' '""' '''
# """ ''' '""' '''' """
# "  ''' "


# sql_query = "select * from users where name = "udhay""
# SyntaxError: invalid syntax


sql_query = "select * from users where name = 'udhay' "
print(sql_query)

sql_query = "select * from users where name = 'udhay'; "
print(sql_query)
print()


# Multi-line Strings
print(
    'Today is an awesome day to learn python'
)

print(
    "Today is an awesome day\
    to learn python"
)

print(
    "Today is an awesome day\
to learn python"
)

print(
    '''Today is an awesome day\
    to learn python'''
)
print(
    """Today is an awesome day\
    to learn python"""
)
print()

print(
    '''Today is an awesome day
    to learn python'''
)
print(
    """Today is an awesome day
    to learn python"""
)
"""
Purpose: String Operations
            - Indexing
"""
language = "Python Programming"
print(language, type(language))

# len() - to get no. of characters in string
print("len(language)=", len(language))


print("STRING OPERATIONS")
print("--------------------------------------")
print("string Indexing")

# P   y  t  h  o n   P r  o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8  9 10 11 12 13 14 15 16 17    - forward indexing
# -18                    -9 -8 -7 -6 -5 -4 -3 -2 -1    - reverse indexing


# NOTE: indexing starts with 0

print("language    :", language)
print("language[14]:", language[14])
print("language[6] :", language[6])
print("language[17]:", language[17])

# print('language[18]:', language[18])
# IndexError: string index out of range

print()
print("language[0]   :", language[0])
print("language[-0]  :", language[-0])

print()
print("language[-3]  :", language[-3])
print("len(language) :", len(language))
print("language[len(language)-3]  :", language[len(language) - 3])


print()
print("language[-18] :", language[-18])
print("language[0]   :", language[0])

# print('language[-19] :', language[-19])
# IndexError: string index out of range

# NOTE 1: For a string of length N,
# we can indexing from -N to (N -1)


# print('language[0.0]   :', language[0.0])
Done