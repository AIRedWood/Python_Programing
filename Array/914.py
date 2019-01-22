914. X of a Kind in a Deck of Cards

对于给定的牌组，请问是否能够分为N组，每组的牌一样。其中每组牌数X大于等于2。

解题思路1：
1，首先对频率进行统计。
2，对于所有的频率，如果所有的数都是最小数X的倍数，且X>=2，则每组个数为X个。

C++:
	class Solution {
	public:
		bool hasGroupsSizeX(vector<int>& deck) {
			
			// 记录频次以及最大值
			vector<int> count(1000,0);
			int max = 0;
			for(int i = 0; i < deck.size() ; i ++)
			{
				count[deck[i]] +=1;
				if(max < deck[i])
					max = deck[i];
			}
			
			int min = 1000;
			vector<int> frequency;  
			for(int i = 0; i <= max ; i ++){
				if (count[i] != 0)
				{
					frequency.push_back(count[i]);
					if (min > count[i])
						min = count[i];
				}
			}
			
			// 若所有频次都能被2到min之间的某个值整除，则可以划分反之则不能。
			for(int x = 2; x <= min; x++)
			{
				bool isok = true;
				for(int i = 0; i < frequency.size(); i++)
				{
					if (frequency[i] % x != 0)
					{
						isok = false;
						break;
					}
				}
				if(isok)
					return true;
			}
			return false;
		}
	};
	Runtime: 8 ms, faster than 98.71% of C++ online submissions for X of a Kind in a Deck of Cards.

Python3:
	class Solution:
		def hasGroupsSizeX(self, deck):
			"""
			:type deck: List[int]
			:rtype: bool
			"""
			count = collections.Counter(deck)
			N = min(count.values())
			for x in range(2,N+1):
				if N % x == 0:
					if all(v % x == 0 for v in count.values()):
						return True
			return False
	Runtime: 68 ms, faster than 95.31% of Python3 online submissions for X of a Kind in a Deck of Cards.
	
	