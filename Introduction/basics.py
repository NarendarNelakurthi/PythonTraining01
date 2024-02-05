print("Hello world")

  
try:
  print(1/ 0)
except Exception as ex:
  print("Got Exception in the Program", ex)

"""Purpose: Python is a dynamic Typed Language.
    Progamming Languages
        - Classficiation
            1. Static-Typed Languages (c, c++, java)
                - first declare the variables, &
                - then use them
                    int a, float b  # Declaration
                    a = 10          # initialization

            2. Dynamic Typed Languages (python, perl, ruby)
                 - create when you need. No declaration needed
                    num1 = 123
                    num2 = 123.4
                    num2 = None
                    
                """
number = 20 #   In another Programming languages we have to declare what type of variables and then assign values
"""Purpose: learning importance of comment operator

ctrl + /  for commenting/uncomment

NOTE: python has only line comment operator; not multiple line comment operator"""

#Only one line comments
#You can check types using type(variable)
var1=(300,)
var2=[200,300,]
var3=300j
var4=200.0
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))