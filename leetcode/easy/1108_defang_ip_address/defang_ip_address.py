class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join(map(lambda x: "[.]" if x == "." else x, address))
