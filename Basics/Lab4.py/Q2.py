# Input from the keyboard
input_list = input("Enter multiple integers separated by spaces: ")

# Create the list of integers using list comprehension
nums = [int(x) for x in input_list.split()]

# Mean
mean = sum(nums) / len(nums)

# Median
nums.sort()
n = len(nums)
if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]

# Mode
frequency = {}
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_freq = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_freq]
if len(modes) == 1:
    mode = modes[0]
else:
    mode = modes

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
