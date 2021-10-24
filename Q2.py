fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}
def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    multi=0.0
    fruit=0.0
    for order in orderList:
        fruit=order[0]
        multi=fruitPrices[fruit]
        totalCost+=order[1]*multi
    return totalCost
orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
orderList = [('oranges', 4.0), ('strawberries', 3.0), ('limes', 4.0)]
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))