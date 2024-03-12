def solution(A):
    max_sum = -1
    digit_sum_dict = {}

    for num in A:
        sum_digits = digit_sum(num)
        if sum_digits in digit_sum_dict:
            max_sum = max(max_sum, digit_sum_dict[sum_digits] + num)
            digit_sum_dict[sum_digits] = max(digit_sum_dict[sum_digits], num)
        else:
            digit_sum_dict[sum_digits] = num

    return max_sum if max_sum != -1 else -1
