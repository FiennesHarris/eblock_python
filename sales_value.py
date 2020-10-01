product_price = float(input("how much does the item cost?: "))


if product_price >= 200:
    print(f"the item costs: £{product_price} but there is a 10% discount so the final price is: £{product_price * 0.90}")
    
elif 100 <= product_price <= 199.99 :
    print(f"the item costs: £{product_price} but there is a 5% discount so the final price is: £{product_price * 0.95}")
    
elif product_price <100:
    print(f"there is no discount so the final price is: £{product_price}")