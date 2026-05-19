product_prices = {'apple': 30, 'banana': 20, 'orange': 40}

item = input("Select product: ").lower()

if item in product_prices:

    if item == "apple":
        print("Apple selected")
        print("Price:", product_prices[item])

    elif item == "banana":
        print("Banana selected")
        print("Price:", product_prices[item])

    elif item == "orange":
        print("Orange selected")
        print("Price:", product_prices[item])

else:
    print("Product not found")