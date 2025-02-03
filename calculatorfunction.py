def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_input = input("Enter the discount percentage (e.g., 20 for 20%): ")

# Remove '%' sign if present and convert the discount to a float
discount_percent = float(discount_input.replace('%', '').strip())

# Call the function and print the result
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: ${final_price:.2f}")
