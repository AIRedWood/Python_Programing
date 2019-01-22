665. Non-decreasing Array
对于一个数组，是否可以只调整最多一个数字，将其变成递增序列(nums[i-1]<=nums[i]<=nums[i+1)


解题思路1：暴力求解
对于任意一个数字，如果它的后面数字存在比它小，则其需要调整 back_sum+=1
如果它前面存在数字比它大，则其需要调整，front_sum+=1
遍历，如果back_sum和front_sum有数字<=1，则可以调整，反之则不能。
C++:
	class Solution {
	public:
		bool checkPossibility(vector<int>& nums) {
			if (nums.size()<2)
				return true;
			int back_sum = 0;
			int front_sum = 0;
			for(int i = 0; i <nums.size(); i++){
				for(int j = i+1; j < nums.size(); j++)
					if (nums[i] > nums[j]){
						back_sum += 1;
						break;
					}   
				for(int j = 0; j < i; j++)
					if (nums[i] < nums[j]){
						front_sum += 1;
						break;
					}          
			}
			cout<<back_sum<<"    "<<front_sum<<endl;
			if(back_sum <= 1 or front_sum <= 1)
				return true;
			else
				return false;
		}
	};
	Runtime: 200 ms, faster than 1.80% of C++ online submissions for Non-decreasing Array.
	接近于Time Limit Exceeded。
Python3：
	class Solution:
		def checkPossibility(self, nums):
			"""
			:type nums: List[int]
			:rtype: bool
			"""
			# method1 
			if len(nums) <2:
				return True
			back_sum = 0
			front_sum = 0
			for i in range(len(nums)):
				for j in range(i+1, len(nums)):
					if nums[i] > nums[j]:
						back_sum += 1
						break
				for j in range(i):
					if nums[i] < nums[j]:
						front_sum += 1
						break
			return back_sum <= 1 or front_sum <= 1
	Runtime: 14500 ms, faster than 0.96% of Python3 online submissions for Non-decreasing Array.
	接近于Time Limit Exceeded。

解题思路2：
强行调整，循环，对于任意值 nums[i] = nums[i-1],查看是否是递增序列，如果不是则i+1,进行测试，反之返回true
C++:
	class Solution {
	public:
		bool monotone_increasing(vector<int>& arr){
			for(int i = 0; i <arr.size()-1; i++)
				if (arr[i] > arr[i+1])
					return false;
			return true;
		}
		bool checkPossibility(vector<int>& nums) {
			vector<int>& new_(nums);
			for(int i = 0; i <nums.size(); i++){
				int old_ai = nums[i];
				if (i > 0)
					new_[i] = new_[i-1];
				else
					new_[i] = -10000;
				if(monotone_increasing(new_))
					return true;
				new_[i] = old_ai;
			}
			return false;
		}
	};
	Runtime: 44 ms, faster than 19.50% of C++ online submissions for Non-decreasing Array.
Python3:
	class Solution:
		def checkPossibility(self, nums):
			"""
			:type nums: List[int]
			:rtype: bool
			"""
			def monotone_increasing(arr):
				for i in range(len(arr) - 1):
					if arr[i] > arr[i+1]:
						return False
				return True
			new = nums[:]
			for i in range(len(nums)):
				old_ai = nums[i]
				new[i] = new[i-1] if i > 0 else float('-inf')
				if monotone_increasing(new):
					return True
				new[i] = old_ai

			return False
	Runtime: 1636 ms, faster than 0.96% of Python3 online submissions for Non-decreasing Array.
	
解题思路3：
在解题思路2的基础上，提前对数组进行"瘦身":
从左往右，若nums[i] <= nums[i+1] <= nums[i+2],则nums[i]不需要调整,i = i+1,当条件不满足时，停止。
从右往左，nums[j-2] <=nums[j-1] <= nums[j],则nums[j]不需要调整,j = j-1,当条件不满足时，停止。
然后再使用解题思路2对中间这段数组进行求解。
by the way，对于一般可以调整的数组分为以下两种情况：
A:[:,1 2] 4 [3,:] 左边两个，中间为待调整值，右边一个
B [:,1] 4 [2 3,:] 左边一个，中间为待调整值，右边两个
所以如果中间数组长度大于5的话，则说明至少包含两个待调整值，则直接return False

C++:
	class Solution {
	public:
		bool monotone_increasing(vector<int>& arr){
			for(int i = 0; i <arr.size()-1; i++)
				if (arr[i] > arr[i+1])
					return false;
			return true;
		}
		bool checkPossibility(vector<int>& nums) {
			
			int i = 0,j = nums.size() - 1;
			while (i+2 < nums.size() and nums[i] <= nums[i+1] and nums[i+1] <= nums[i+2])
				i += 1;
			while (j-2 >= 0 and nums[j-2] <=nums[j-1] and nums[j-1] <= nums[j])
				j -= 1;
			if (j - i + 1 <= 2)
				return true;
			if (j - i + 1 >= 5)
				return false;
			vector<int> new_nums;
			for(int x = i; x <=j; x++)
				new_nums.push_back(nums[x]);
			vector<int> new_(new_nums);
			for(int i = 0; i <new_nums.size(); i++){
				int old_ai = new_nums[i];
				if (i > 0)
					new_[i] = new_[i-1];
				else
					new_[i] = -10000;
				if(monotone_increasing(new_))
					return true;
				new_[i] = old_ai;
			}
			return false;
		}
	};
	Runtime: 24 ms, faster than 94.70% of C++ online submissions for Non-decreasing Array.

Python3:
	class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i,j = 0,len(nums) - 1
        while i+2 < len(nums) and nums[i] <= nums[i+1] <= nums[i+2]:
            i += 1
        while j-2 >= 0 and nums[j-2] <=nums[j-1] <= nums[j]:
            j -= 1
        
        if j - i + 1 <= 2:
            return True
        if j - i + 1 >= 5:
            return False
        
        nums = nums[i:j+1]
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        new = nums[:]
        for i in range(len(nums)):
            old_ai = nums[i]
            new[i] = new[i-1] if i > 0 else float('-inf')
            if monotone_increasing(new):
                return True
            new[i] = old_ai

        return False
	Runtime: 60 ms, faster than 74.25% of Python3 online submissions for Non-decreasing Array.
	
解题思路4：
若出现超过两次nums[i] < nums[i - 1]，则return False。

C++:
	class Solution {
	public:
		bool checkPossibility(vector<int>& nums) {
			bool modified = false;
			for(int i = 1; i < nums.size(); i++){
				if(nums[i] < nums[i-1]){
					if(modified)
						return false;
					if(i >= 2 and nums[i] < nums[i - 2])
						nums[i] = nums[i - 1];
					modified = true; 
				}
			}
			return true;
		}
	};
	Runtime: 24 ms, faster than 94.70% of C++ online submissions for Non-decreasing Array.

Python3:
	class Solution:
		def checkPossibility(self, nums):
			"""
			:type nums: List[int]
			:rtype: bool
			"""
			modified = False
			for i in range(1, len(nums)):
				if nums[i] < nums[i - 1]:
					if modified:
						return False
					if i >= 2 and nums[i] < nums[i - 2]:
						nums[i] = nums[i - 1]
					modified = True
			return True
	Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Non-decreasing Array.

解题思路5：
类似于解题思路4，若出现超过两次nums[i] < nums[i - 1]，则return False。
若只出现一次，则对于出错的地方进行判定

C++:
	class Solution {
	public:
		bool checkPossibility(vector<int>& nums) {
			int p = -1;
			for(int i = 0; i < nums.size() - 1; i ++)
				if (nums[i] > nums[i+1]){
					if (p != -1)
						return false;
					p = i;
				}
			return p ==-1 or p == 0 or p == nums.size()-2 or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2];
		}
	};
	Runtime: 24 ms, faster than 94.70% of C++ online submissions for Non-decreasing Array.
	
Python3：
	class Solution(object):
		def checkPossibility(self, A):
			p = None
			for i in range(len(A) - 1):
				if A[i] > A[i+1]:
					if p is not None:
						return False
					p = i
			return (p is None or p == 0 or p == len(A)-2 or
					A[p-1] <= A[p+1] or A[p] <= A[p+2])
		Runtime: 60 ms, faster than 74.25% of Python3 online submissions for Non-decreasing Array.