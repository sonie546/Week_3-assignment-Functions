# Question One
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Question Two 
price_input = 200
discount_input = 25

# Calculate and print result
final_price = calculate_discount(price_input, discount_input)

if discount_input >= 20:
    print(f"Discount applied. Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")

