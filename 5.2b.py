def get_recipe_price(prices, optionals=[], **quantities):
    '''
    :param prices: dictionary: key=productname, value=price/100gr
    :param optionals: what we are not using to calculate the price
    :param quantities: makes a dictionary of the keyword, with the name and the amount
    we use ** to make the keyword and the value in a dictioanry
    :return:
    '''
    total_price = 0
    for item, quantity in quantities.items():
        if item not in optionals:
            # if the item doesn't exist it will return 0
            #devide by 100 becayse the amount is per 100 grams.
            total_price += prices.get(item, 0) * (quantity/100)
    return int(total_price)

print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))

