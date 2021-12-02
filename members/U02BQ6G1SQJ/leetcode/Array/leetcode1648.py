# reference : https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927522/Python-n-log-n-690-ms

import collections;

MOD = (10 ** 9) + 7;

def getAnswer(inventoryList : List[int], orders : int, target : int) -> int:
    (value, cnt) = (0, 0);
    
    for curInventory in inventoryList:
        # print("curInventory :", curInventory);
        # print("target :", target);
        # print("orders :", orders);
        
        if (curInventory >= target):
            (value, cnt) = (int(value + (((curInventory + target) / 2) * (curInventory - target + 1))) % MOD, cnt + curInventory - target + 1);
            
            # print("value :", value);
            # print("cnt :", cnt);
            
            if (cnt > orders):
                # print("False");
                
                return -1;
    
    # print("True");
    
    return (value + ((orders - cnt) * (target - 1))) % MOD;
    
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """
        (answer, left, right) = (0, 0, max(inventory));
        
        while (left <= right):
            mid = (left + right) // 2;
            result = getAnswer(inventory, orders, mid);
            
            if (result != -1):
                (answer, right) = (result, mid - 1);
                
                print(answer);
            else:
                left = mid + 1;
                
        return answer;
        """
        
        (answer, curIdx, width, inventoryList) = (0, 0, 0, sorted(collections.Counter(inventory).items(), reverse = True) + [(0, 0)]);
        
        while (orders > 0):
            width += inventoryList[curIdx][1];
            sell = min(orders, width * (inventoryList[curIdx][0] - inventoryList[curIdx + 1][0]));
            (quotient, remainder) = divmod(sell, width);
            answer += ((width * (quotient * ((inventoryList[curIdx][0] * 2) - quotient + 1)) // 2) + (remainder * (inventoryList[curIdx][0] - quotient)));
            orders -= sell;
            curIdx += 1;
            
        return (answer % MOD); 
