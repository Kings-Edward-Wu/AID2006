# 1.给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。（至少使用两种方法求解）
# 示例：给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


# 方法1
# nums = [2, 7, 11, 15]
# target = 18
# result = []
# for i in range(len(nums)-1):
#     for r in range(i,len(nums)):
#         if nums[i] + nums[r] == target:
#             result.append(i)
#             result.append(r)
# print(result)

nums = [2, 7, 11, 15]

def get_number():
    target = 5
    left = 0
    right = len(nums) - 1
    while left < right:
        if target == nums[left] + nums[right]:
            return left,right
        if target > nums[left] + nums[right]:
            left += 1
        if target < nums[left] + nums[right]:
            right -= 1
    return left,right


print(get_number())


