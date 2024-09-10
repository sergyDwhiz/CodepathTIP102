from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for i in range(len(operations)):
            if operations[i] == "X++" or operations[i] == "++X" :
                count+=1
            elif operations[i] == "--X" or operations[i]  == "X--":
                count-=1
            else:
                return count
        return count
