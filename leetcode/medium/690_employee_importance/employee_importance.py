
# Definition for Employee.
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        self.employees = {}
        for employee in employees:
            self.employees[employee.id] = (
                employee.importance, employee.subordinates)
        return self.recurse(id)

    def recurse(self, id):
        importance = self.employees[id][0]
        for subordinate in self.employees[id][1]:
            importance += self.recurse(subordinate)
        return importance
