# 给你一个长度为n的数组，
# 其中只有一个数字出现了1次，其他均出现2次，问如何快速的找到这个数字。
from typing import List


def get_number(number: List):
    result = []
    for item in number:
        if item not in result:
            result.append(item)
        elif item in result:
            result.remove(item)
    return result


print(get_number([1, 1, 2, 3, 3, 4, 4]))
