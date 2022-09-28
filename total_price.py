# Code modified from https://medium.com/@darth_waiter/python-challenge-can-you-figure-out-whats-wrong-in-5-minutes-16e2f78a1613

# Task: find and fix the bugs that are causing the output total prices to be incorrect.
# If successful, submit a pull request containing your fixed code to my repository.

# Note: you can't change the initial data structures for this activity 
# (sizes, prices, & quantities)


sizes = [
    {
        "name": "item_1",
        "size_in_mL": "100mL",
        "alternate_identifier": "axc45"
    },
    {
        "name": "item_2",
        "size_in_mL": "100mL",
        "alternate_identifier": "axc675"
    },
    {
        "name": "item_2",
        "size_in_mL": "400mL",
        "alternate_identifier": "axc66725"
    },
    {
        "name": "item_3",
        "size_in_mL": "50mL",
        "alternate_identifier": "axd10025"
    }
]

prices = [
    {
        "price": 10.67,
        "alternate_identifier": "axc45"
    },
    {
        "price": 15.50,
        "alternate_identifier": "axc675"
    },
    {
        "price": 20.99,
        "alternate_identifier": "axc66725"
    },
    {
        "price": 7.99,
        "alternate_identifier": "axd10025"
    }
]

quantities = [
    {
        "name": "item_1",
        "quantity": 10
    },
    {
        "name": "item_2",
        "quantity": 20
    },
    {
        "name": "item_2",
        "quantity": 40
    },
    {
        "name": "item_3",
        "quantity": 15
    }
]

#
# ====== You can change anything after this line ======
#

# YOUR CODE PRINTS THE TOTAL PRICE TO BUY ALL ITEMS OF A SPECIFIC SIZE 
# (Example -  10 item_1 OF SIZE 100mL cost $106.7)

identifier_info = {item['name']: item['alternate_identifier'] for item in sizes}

price_info = {item['alternate_identifier']: item['price'] for item in prices}


# LOOP WHICH CALCULATES TOTAL PRICE

for item in quantities:
    name, quantity = item['name'], item['quantity']

    # fetch alternate_identifier to get the price
    identifier = identifier_info[name]

    # get price of the item
    price = price_info[identifier]

    # calculate the total price to buy the entire stock of a specific size of an item
    total_price = quantity * price

    print(f'The total price of {name} is {total_price}.')
