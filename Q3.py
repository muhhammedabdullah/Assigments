from __future__ import print_function
import shop
def shopSmart(orderList, fruitShops):
    lowest_cost=fruitShops[0]
    for item in range(0,len(fruitShops)-1) :
        if (fruitShops[item].getPriceOfOrder(orderList)>fruitShops[item+1].getPriceOfOrder(orderList)) :
            lowest_cost=fruitShops[item+1]
    return lowest_cost
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    dir3 ={'apples':1.5,'oranges':2.0}
    shop3=shop.FruitShop('shop3',dir3)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())