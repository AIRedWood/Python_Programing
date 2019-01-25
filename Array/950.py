950. Reveal Cards In Increasing Order
对于给定的字符串，将其变成指定顺序：
抽出一张牌，将一张牌放到最底下。接替进行上述两个动作，直到所有数字按序输出。

解题思路1:
Input:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
Output:[1,15,2,11,3,19,4,12,5,16,6,13,7,18,8,14,9,17,10]

对于一个序列：
观察上述数据，我们可以得到规律。对于OutPut，抽出一张牌，将一张牌放到最底下可以得到Input。
反过来，对于Input，填上一个空，将一个空移到最后面可得到Output。

1，首先，我们对其进行排序得到sorted_list。
2，我们对sorted_list按序输出，填到指定位置，填上一个空，将下一个空移到最后面。
3，交替进行，直到最后没用空。
注释：这里我们记录所有点的下标表示空的位置，使用双端队列进行装载。

C++:
	class Solution {
	public:
		vector<int> deckRevealedIncreasing(vector<int>& deck) {
			deque<int> index;
			for(int i = 0; i <deck.size(); i++)
				index.push_back(i);
			vector<int> ans(deck.size());
			
			sort(deck.begin(), deck.end());
			for(int i = 0; i < deck.size(); i++){
				ans[index.front()] = deck[i];
				index.pop_front();
				if (index.size() > 0)
					index.push_back(index.front());
					index.pop_front();
			}
				
			return ans;
		}
	};
	Runtime: 4 ms, faster than 100.00% of C++ online submissions for Reveal Cards In Increasing Order.
	
Python3：
	class Solution(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = collections.deque(range(N))
        output = [None] * N
            
        for card in sorted(deck):
            output[index.popleft()] = card
            if index:
                index.append(index.popleft())                                
        return output
		
	Runtime: 44 ms, faster than 99.20% of Python3 online submissions for Reveal Cards In Increasing Order.
	
		
		
		