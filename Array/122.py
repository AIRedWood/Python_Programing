122. Best Time to Buy and Sell Stock II
对于股票的走势：[7,1,5,3,6,4]，求解最大回报。

结题思路1：
遍历数组，如果当前天的价格高于前一天的话，则认为存在利润，若是低的话，则利润为0
(不计算亏损)。

C++：
	class Solution {
	public:
    int maxProfit(vector<int>& prices) {
        int sum = 0;
        for(int i = 1; i < prices.size(); i++)
            if (prices[i] > prices[i-1])
                sum += prices[i] - prices[i-1];
        return sum ;
		}
	};
	Runtime: 4 ms, faster than 100.00% of C++ online submissions for Best Time to Buy and Sell Stock II.
	
Python3：
	class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0;
        for i in range(1,len(prices)):
            sum += prices[i] - prices[i-1] if (prices[i] > prices[i-1]) else 0
        return sum 
	Runtime: 52 ms, faster than 98.92% of Python3 online submissions for Best Time to Buy and Sell Stock II.
	 