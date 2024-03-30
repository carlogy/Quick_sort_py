def quick_sort(nums, low, high):
    if low < high:
        partion_input = partition(nums, low, high)
        quick_sort(nums, low, partion_input - 1)
        quick_sort(nums, partion_input + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
