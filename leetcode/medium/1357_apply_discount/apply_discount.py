from typing import List


class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = dict(zip(products, prices))
        self.customer_no = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        self.customer_no += 1
        for i in range(len(product)):
            bill += self.products[product[i]] * amount[i]
        if self.customer_no % self.n == 0:
            bill *= ((100 - self.discount) / 100)
        return bill


obj = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [
              100, 200, 300, 400, 300, 200, 100])
print(obj.getBill([1, 2], [1, 2]))
