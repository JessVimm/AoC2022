# ADVENT OF CODE 2022 DAY 01

# --PART 1--

# Extract data from file
with open('day01.txt','r') as file:
    data = file.read().strip()

# Turn string data into a list
elves = data.split('\n\n')

# Extract each group of calories
calories_groups = [elf.split('\n') for elf in elves]

# Compute the sum of the calories
calories_sum = [sum(map(int, group)) for group in calories_groups]

# Sort the sums
sorted_calories = sorted(calories_sum)

# Get the elf with most calories
top = sorted_calories[-1]
print(f"Sum of top Elf: {top}")

# --PART 2--

# Get the top three Elves
sum_last_three = sum(sorted_calories[-3:])

print(f"Sum of last three: {sum_last_three}")
