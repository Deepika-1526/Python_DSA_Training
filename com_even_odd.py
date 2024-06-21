'''list1 = [6, 3, 2, 9, 4, 7]
list2 = [8, 7, 5, 3, 6, 9]

even = [num for num in list1 if num % 2 == 0]
odd = [num for num in list2 if num % 2 != 0]

result = [even + odd for even in even for odd in odd]
print(result)'''
def even(nums, index=0, evens=[]):
    if index == len(nums):
        return evens
    if nums[index] % 2 == 0:
        return even(nums, index + 1, evens + [nums[index]])
    return even(nums, index + 1, evens)

def odd(nums, index=0, odds=[]):
    if index == len(nums):
        return odds
    if nums[index] % 2 != 0:
        return odd(nums, index + 1, odds + [nums[index]])
    return odd(nums, index + 1, odds)

def sums(evens, odds, ev_index=0, od_index=0,group_sum=0, result=[]):
    if ev_index == len(evens):
        return result
    if od_index == len(odds):
        result.append(group_sum)
        return sums(evens, odds, ev_index + 1,0,0,result)
    group_sum += evens[ev_index] + odds[od_index]
    return sums(evens, odds, ev_index, od_index + 1,group_sum, result)

list1 = [6, 3, 2, 9, 4, 7]
list2 = [8, 7, 5, 3, 6, 9]

evens = even(list1)
odds = odd(list2)

result = sums(evens, odds)

print(result)

