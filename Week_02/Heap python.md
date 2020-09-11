### Heap python

#### 返回最小的k个数

**求k个最小用大根堆，k个最大用小根堆，一定条件下向外pop, 留下k个数为result**

**大根堆法**

大根堆：最大的元素在0索引，pop时第一个弹出，维护时的插入删除都是 O(logk )

python 只有小根堆 ，插入的元素需要加负号来让小根堆成大根堆。

**代码**

``` 
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
		heap, res = [], []
		for x in arr:
			heapq.heappush(heap, -x)
			# 保证堆中只有k个元素
			if len(heap) > k: heapq.heappop(heap) # 弹出堆顶最小值
		while len(heap):
			res.append(-heap[0])
			heapq.heappop(heap)
		return res
		
```

#### 滑动窗口取最大值

**用堆来解决**

**思路：**

 - 滑过的每一个元素入堆

 - 当滑窗全部滑入target_nums时，开始出堆（边界条件: if i + 1 >= k）

   	- k 是物理距离，i是索引距离，i+1 统一距离

 - 出堆的元素为当前滑窗中最大元素，加入res_list

    - 注意：保证堆顶元素是滑窗内的元素

      `if heap[0][1] > i - k + 1`

      i + 1 - k 表示滑窗后面剩几个元素

``` python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, heap = [],[]
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i],i))
            if i >= k -1:
                while heap and heap[0][1] < i + 1 -k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
```

