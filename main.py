def get_tax_amount(income):
    if 10000 <= income <= 20000:
        tax = (income - 10000) * 0.10 + 10000
    elif income >= 20000:
        tax = (income - 20000) * 0.20 + 20000
    else:
        tax = 0
    return tax


result = get_tax_amount(25000)

if result == 0:
    print("It doesn't fall under taxable income range !!")
else:
    print("you tax is ", result)

