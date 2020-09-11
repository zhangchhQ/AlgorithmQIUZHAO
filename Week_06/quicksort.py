def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, end, nums)


def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark

quick_sort(0, 10, [4, 55, 3, 2, 1, 8, 9, 12, 6, 15])
