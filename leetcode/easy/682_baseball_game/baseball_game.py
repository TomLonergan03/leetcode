from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            match operation:
                case '+':
                    record.append(record[-2] + record[-1])
                case 'D':
                    record.append(2*record[-1])
                case 'C':
                    record.pop()
                case _:
                    record.append(int(operation))
        return sum(record)
