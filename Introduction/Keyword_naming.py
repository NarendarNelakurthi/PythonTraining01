# Identifiers - User-defined variables
#   - Naming Convention
#      1. keywords should not be used as identifiers
#      2. first character: a-z, A-Z, _
#      3. remaining chars: a-z, A-Z, _, 0-9
"""variable
    keyword  -- variables defined by the language
    identifier  --- variables defined by user
                    or, user-defined variables
# Loading a module
import keyword

print(keyword)
print(dir(keyword))  # uses
print()

print(keyword.kwlist)

# variable casing(Use this for Variables)
# 1.snake casing or underscore casing
student = "shiva"
employee_salary = 2343223432.23
cost_of_mango = 12
selling_price_of_apples = 34

output_of_thermal_sensor = 32
no_of_current_processes = 5


# 2. Camel casing(Use this for Class)
Student = "Shiva"
EmployeeSalary = 2343223432.23
CostOfMango = 12
SellingPriceOfApples = 34
Brace
    ()  paranthesis

    []  square braces
    {}  flower braces
                    
                    """
sum_of_values = (123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12 \
    - 123 + 23 - 123 * 2 / 12 \
    - 123 + 23 - 123 * 2 / 12 \
    - 123 + 23 - 123 * 2 / 12 \
    - 123 + 23 - 123 * 2 / 12)
print(sum_of_values)

sum_of_values = (123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12
    - 123 + 23 - 123 * 2 / 12
    - 123 + 23 - 123 * 2 / 12
    - 123 + 23 - 123 * 2 / 12
    - 123 + 23 - 123 * 2 / 12)
print(sum_of_values)



sum_of_values = [123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12
    -123 + 23 - 123 * 2 / 12
    - 123 + 23 - 123 * 2 / 12
    - 123 + 23 - 123 * 2 / 12
    - 123 + 23 - 123 * 2 / 12]
print(sum_of_values)
# \ line continuation operator
# Python is interpreter based lanugage - means line by line execution
# Python -> c lanagueg - > aseembly - machine lnag -> machine
