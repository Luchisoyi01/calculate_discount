def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
      # Calculate the discount amount
      discount_amount = (discount_percent / 100) * price
      # Calculate the final price after applying the discount
      final_price = price - discount_amount
      return final_price
    else:
      # If the discount is less than 20%, return the original price
      return price

# Prompt the user to enter the original price and the discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the calculate_discount function and print the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after applying the discount is: {final_price}" if discount_percentage >= 20 else f"No discount was applied. The original price is: {original_price}")
