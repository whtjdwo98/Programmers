def solution(nums):
    pocket_kind = len(set(nums))
    answer = len(nums) / 2
    if answer > pocket_kind:
        answer = pocket_kind
    return answer