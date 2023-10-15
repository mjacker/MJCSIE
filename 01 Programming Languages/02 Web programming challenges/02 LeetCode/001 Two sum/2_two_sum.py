def twoSum(self, nums: List[int], target: int) -> List[int]:
    pos_num = [x for x in enumerate(nums)]
    pos_num.sort(key=lambda x:x[1])
    for x in pos_num:
        for y in pos_num:
            if x != y:
                if (x[1] + y[1] == target):
                    return(list([x[0], y[0]]))
