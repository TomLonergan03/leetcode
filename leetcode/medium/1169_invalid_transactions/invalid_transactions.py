from typing import List


class Transaction:
    def __init__(self, name: str, time: int, amount: int, city: str) -> None:
        self.name = name
        self.time = time
        self.amount = amount
        self.city = city

    def __str__(self) -> str:
        return str(self.name) + "," + str(self.time) + "," + str(self.amount) + "," + str(self.city)


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_dict = {}
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            if name in transaction_dict:
                transaction_dict[name].append(
                    Transaction(name, int(time), int(amount), city))
            else:
                transaction_dict[name] = [
                    Transaction(name, int(time), int(amount), city)]
        invalid = []
        for key in transaction_dict.keys():
            same_person = transaction_dict[key]
            same_person = sorted(
                same_person, key=lambda x: x.time)
            for transaction in same_person:
                if transaction.amount > 1000:
                    invalid.append(transaction)
                for other_transaction in same_person:
                    if transaction.time >= other_transaction.time - 60 and transaction.time <= other_transaction.time + 60 and transaction.city != other_transaction.city:
                        invalid.append(transaction)
                        invalid.append(other_transaction)
        return list(map(lambda x: str(x), set(invalid)))


print(Solution().invalidTransactions(
    ["alice,20,800,mtv", "alice,50,100,beijing"]))
