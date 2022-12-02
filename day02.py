puzzle_input = open('day02.txt', 'r').read().split('\n')

# Part 1

my_shape = ("X", "Y", "Z")

win = ("A Y", "B Z", "C X")
draw = ("A X", "B Y", "C Z")
lose = ("A Z", "B X", "C Y")

def assign_score(rounds):
    score = 0
    for round in rounds:
        score += (my_shape.index(round[-1]) + 1)
        if round in win:
            score += 6
        elif round in draw:
            score += 3
        else:
            score += 0
    return score

print(assign_score(puzzle_input)) # 11386

# Part 2

rock = ("A Y", "B X", "C Z")
paper = ("B Y", "C X", "A Z")
scissors = ("C Y", "A X", "B Z")

def assign_new_score(rounds):
    score = 0
    for round in rounds:
        if round in rock:
            score += 1
        elif round in paper:
            score += 2
        elif round in scissors:
            score += 3
            
        if round[-1] == "Z":
            score += 6
        elif round[-1] == "Y":
            score += 3
        elif round[-1] == "X":
            score += 0
    return score

print(assign_new_score(puzzle_input)) # 13600
