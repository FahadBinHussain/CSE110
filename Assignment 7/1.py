def grocery_app(items, location = "Dhanmondi"):
    prices = {
        "Rice": 105,
        "Potato": 20,
        "Chicken": 250,
        "Beef": 510,
        "Oil": 85
        }
    
    total = 0

    for item in items:
        if item in prices:
            total += prices[item]

    if location != "Dhanmondi":
        total += 70
    else:
        total += 30

    return total

user = ["Rice", "Beef", "Rice"]
print(grocery_app(user, "Mohakhali"))