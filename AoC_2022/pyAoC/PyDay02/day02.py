# ADVENT OF CODE 2022 DAY 02

# --PART 1--

# Extract data from file
with open('day02.txt', 'r') as file:
    data = file.read().strip()

# Turn data into a list
plays = data.split('\n')

# Puzzle rules
my_play_points = {
"Y": 2,
"X": 1,
"Z": 3,
}

play_points = {
"Y": {"A": 6, "B": 3, "C": 0},
"X": {"A": 3, "B": 0, "C": 6},
"Z": {"A": 0, "B": 6, "C": 3},
}

# Calculating points
# my_play_points + play_points
total_score = 0

for play in range(len(plays)):

    opponents_play = plays[play][0]
    my_play = plays[play][2]

    total_score += my_play_points[my_play] + play_points[my_play][opponents_play]

# Print the total score
print(total_score)

# --PART 2--

# New rules
game_points = {
"X": 0,
"Y": 3,
"Z": 6,
}

should_play = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1},
}

total_score = 0

for play in range(len(plays)):

    opponents_play = plays[play][0]
    play_status = plays[play][2]

    total_score += game_points[play_status] + should_play[opponents_play][play_status]

print(total_score)





