#Luhn Formula
def validate(num_card):
    nums = []
    checker_num = int(num_card[len(num_card) - 1])

    for i in range(len(num_card)-1):
        nums.append(int(num_card[i]))

    nums.reverse()

    for i in range(0, len(nums), 2):
        nums[i] *= 2

    for i in range(len(nums)):
        if nums[i] > 9:
            nums[i] -= 9

    check_sum = 0
    for i in range(len(nums)):
        check_sum += nums[i]
    return (check_sum + checker_num) % 10 == 0
if validate(input()):
    print('It is valid')
else:
    print('It is invalid')
