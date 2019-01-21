
'''
832. Flipping an Image
题目描述：
对于给定的二维数组:
[[1,1,0],
 [1,0,1],
 [0,0,0]],
对立面的数字进行0-1翻转，顺序按照从左到右翻转。然后输出
然后输出
[[1,0,0],
 [0,1,0],
 [1,1,1]]
 '''
 
 C++:
 
	 class Solution {
		public:
			vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
				#声明新的vector
				vector<vector<int>> B(A.size());
				for (int i = 0; i < B.size(); i++)
					B[i].resize(A[0].size());
				
				#遍历,从右往左对值进行调整。
				for ( int ix = 0; ix < A.size(); ++ix ) 
				{
					for ( int iy = 0; iy < A[ix].size(); ++iy )
						if (A[ix][iy] == 0)
							B[ix][A[ix].size() - 1 - iy] = 1;
				}
			return B;
			}
		};
		
	Runtime: 12 ms, faster than 98.32% of C++ online submissions for Flipping an Image.

Python3：

	class Solution:
		def flipAndInvertImage(self, A):
			"""
			:type A: List[List[int]]
			:rtype: List[List[int]]
			"""
			#声明新的List
			B = [[0 for i in A[0]] for j in A]
			
			#遍历,从右往左对值进行调整。
			for i in range(len(A)):
				for j in range(len(A[0])):
					if A[i][j] == 0:
						B[i][len(A[i]) - 1 - j] = 1
			return B

	Runtime: 72 ms, faster than 81.20% of Python3 online submissions for Flipping an Image.