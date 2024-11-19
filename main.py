Name:Agustin Francicetti Caceres.      Date: november 19, 2024.    period: 1st

#(1)Define the base price of the pizza and the price for each topping.
#(2)Parse the user input to identify which toppings are included, ensuring that we only count each topping once.
#(3)Calculate the total price by adding the base price and the price of the toppings.
#(4)Check if the total price exceeds $20, and if it does, apply a 5% discount.
#(5)Format the final price to two decimal places without the dollar sign.


Here's the Python code that implements this logic:

def calculate_pizza_price(toppings_input):
    # Define the base price and topping prices
    base_price = 15.00
    topping_prices = {
        'T': 1.50,  # tomatoes
        'O': 1.25,  # onions
        'P': 3.50,  # pineapple
        'M': 3.75,  # mushrooms
        'A': 0.40   # avocado
    }
    
    # Use a set to avoid counting duplicate toppings
    unique_toppings = set(toppings_input)
    
    # Calculate the total price from unique toppings
    total_topping_price = sum(topping_prices[topping] for topping in unique_toppings if topping in topping_prices)
    
    # Calculate the final price
    total_price = base_price + total_topping_price
    
    # Apply a 5% discount if the total price is over $20
    if total_price > 20:
        total_price *= 0.95  # Apply 5% discount

    # Round to the nearest cent and format to two decimal places
    final_price = round(total_price, 2)
    
    # Return the final price formatted as a string without the dollar sign
    return f"{final_price:.2f}"

# Example usage
input1 = "TPM"
output1 = calculate_pizza_price(input1)
print(output1)  # Expected output: 22.56

input2 = "AAAAAAAMMTGTMMMXMMT"
output2 = calculate_pizza_price(input2)
print(output2)  # Expected output: 19.62



Explanation of the Code:
-We define the base price of the pizza and the prices for each topping in a dictionary.

-We convert the input string of toppings into a set to automatically filter out duplicate toppings.

-We calculate the total price of the toppings by summing their prices based on the unique toppings.

-We then check if the total price exceeds $20 to apply a 5% discount if necessary.

-Finally, we round the price to two decimal places and format it as a string for output.

                                                                            
                                                                            
*This code will correctly compute the price of a pizza based on the user's topping preferences, handling duplicates and ignoring invalid characters.
