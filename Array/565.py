565. Array Nesting
对于一个指定的数组，给出其中长度最大的环。

解题思路：
这里，通过观察可知，所有的数字都能组成环，问题在于如何找到最大的环：
如例子：[5,4,0,3,1,6,2]有三个环：
1：5→6→2→0
2：1→4
3：3→3

这里可以通过查找以数组中每一个数字为起始点的环，然后取其中最大的环。
此外，一个环上的所有数字都对应着一个环，如上述所示，该组数字中只有三个环，所以，理论上来说只需要找到三个环中的任意一个数字
查找三遍即可。

这里主要有两种思路去解决这个问题：
1：设定visited数组，将所有访问过的节点置成True,当访问到该节点时，如果visited[i] == True则表示该数字所在的环已经被访问过了，则跳过这个数字。
此外，对于一个环的终结位置也是它的后续节点的visited[i] == True,如上述第一个环，当访问到0的时候，它的后续节点5的visited == True，则表示该环
结束了。
2：类似与上面的思路，这里不需要额外的visited数组，只需要将所有访问过的节点数值设为-1即可。

解题思路1：
C++:
	class Solution {
	public:
		int dfs(vector<int>& nums) {
			int maxnum = 0;
			bool visited[nums.size()] = {0};
			for(int i = 0; i < nums.size(); i++){
				if (visited[i] == true)
					continue;
				int curr = nums[i];
				int tempnum = 0;
				while(1){
					visited[curr] = true;
					tempnum += 1;
					if (visited[nums[curr]])
						break;
					else
						curr = nums[curr];
				} 
				if (maxnum < tempnum)
					maxnum = tempnum;
			}
			return maxnum;
		}
			
		int arrayNesting(vector<int>& nums) {
			return dfs(nums);
		}
	};
	Runtime: 32 ms, faster than 69.39% of C++ online submissions for Array Nesting.
	Memory Usage: 14.6 MB, less than 100.00% of C++ online submissions for Array Nesting.

Python:
	def dfs(nums):
		maxnum = 0
		visited = [False for i in nums]
		for i in range(len(nums)):
			if visited[i] == True:
				continue
			curr,tempnum = nums[i],0
			while(1):
				visited[curr] = True
				tempnum += 1
				if visited[nums[curr]]:
					break
				else:
					curr = nums[curr]
			maxnum = maxnum if maxnum > tempnum else tempnum
		return maxnum

	class Solution:
		def arrayNesting(self, nums: 'List[int]') -> 'int':
			return dfs(nums)
	Runtime: 64 ms, faster than 99.75% of Python3 online submissions for Array Nesting.
	Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Array Nesting.
解题思路2：
C++:
	class Solution {
	public:
		int dfs(vector<int>& nums) {
			int maxnum = 0;
			for(int i = 0; i < nums.size(); i++){
				if (nums[i] == -1)
					continue;
				int curr = nums[i];
				int tempnum = 0;
				nums[i] = -1;
				while(1){
					tempnum += 1;
					if (nums[curr] == -1)
						break;
					else{
						int temp = nums[curr];
						nums[curr] = -1;
						curr = temp;
					}

				} 
				if (maxnum < tempnum)
					maxnum = tempnum;
			}
			return maxnum;
		}
			
		int arrayNesting(vector<int>& nums) {
			return dfs(nums);
		}
	};
	Runtime: 28 ms, faster than 95.92% of C++ online submissions for Array Nesting.
	Memory Usage: 14.5 MB, less than 100.00% of C++ online submissions for Array Nesting.

Python:
	def dfs(nums):
		maxnum = 0
		for i in range(len(nums)):
			if nums[i] == -1:
				continue
			curr,tempnum = nums[i],0
			nums[i] = -1
			while(1):
				tempnum += 1
				if nums[curr] == -1:
					break
				else:
					temp = nums[curr]
					nums[curr] = -1
					curr = temp
			maxnum = maxnum if maxnum > tempnum else tempnum
		return maxnum

	class Solution:
		def arrayNesting(self, nums: 'List[int]') -> 'int':
			return dfs(nums)
	Runtime: 64 ms, faster than 99.75% of Python3 online submissions for Array Nesting.
	Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Array Nesting.