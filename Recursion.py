# 函数内部自己调用自己
# 必须有出口

# 3 + 2 + 1
def sum_number(num):
    if num == 1:                              # Exit
        return 1
    return num + sum_number(num-1)            # Use itself

result = sum_number(4)
print(result)


def sum_branch(i):
    if i == 0:
        return 1
    return 2 ** i + sum_branch(i - 1)

root = [3,9,20,'null','null',15,7]
i = 0
while i < len(root):
    if sum_branch(i) == len(root):
        print(i + 1)
        break
    else:
        i += 1

nums = [2,2,1,1,4]
for i in nums:
    if nums.count(i) == 1:
        print(i)
