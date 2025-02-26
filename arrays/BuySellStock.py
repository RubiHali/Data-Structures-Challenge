class BuySellStock:
    """ Time Complexity : O(N)
    Space Complexity : O(1)
    Using constant memory / variable to record max profit
    """

    def find_max_profit(self, prices: list):
        max_profit = 0
        buy_price = float('inf')
        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                profit = price - buy_price
                max_profit = max(profit, max_profit)
        return max_profit


if __name__ == "__main__":
    buy_sell_stock = BuySellStock()
    profit = buy_sell_stock.find_max_profit([10, 1, 5, 6, 7, 1])
    print(profit)
