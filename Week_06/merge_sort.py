def merge_sort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)
    merge(nums, left, right, mid)

def merge(nums, left, right, mid):
    i = left
    j = mid+1
    temp = []
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            temp.append(i)
            i += 1
        else:
            temp.append(j)
            j += 1
    while i <= mid:
        temp.append(i)
        i+=1
    while j <= right:
        temp.append(j)
        j+=1
    nums[left:right+1] = temp

nums = [4, 55, 3, 2, 1, 8, 9, 12, 6, 15]
merge_sort(nums, 0, 9)
print(nums)

