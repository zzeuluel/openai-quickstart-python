def calculate_total(price, tax_rate, discount):
    discount_amount = discount if discount > 0 else 10  # Default discount of $10 if no discount is provided
    tax = price * tax_rate
    final_price = price + tax - discount_amount

    # print the Final price
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(price=100, tax_rate=0.08, discount=10)

discount = 10