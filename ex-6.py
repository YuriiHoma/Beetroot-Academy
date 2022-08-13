price = int(input("laptop price "))
tax = int(input("tax "))
# print(price, tax )
tax_amount = price/100*tax
# print(tax_amount)
total_price = price+tax_amount
print("The total price of the laptop is", total_price)