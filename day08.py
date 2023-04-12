from aocd import get_data
puzzle_input = get_data(day=8, year=2022).split('\n')

def down(x, y):
     return x, y + 1

def up(x, y):
     return x, y - 1
     
def right(x, y):
     return x + 1, y

def left(x, y):
     return x - 1, y

trees = {}

def store_tree_coords(tree_heights):
    x = 0
    y = 0

    for row in tree_heights:
        for tree_height in row:
            trees[(x, y)] = int(tree_height)
            x += 1
        x = 0
        y += 1

def find_tree_visibility(tree_coords, height, max_coord):
    x, y = tree_coords
    side_visible = True
    scenic_score = 0
    scenic_scores = []
    multiplied_score = 1
    if y == max_coord:
        scenic_score = 1
    while y != max_coord:
       x, y = down(x, y)
       scenic_score += 1
       if trees[(x, y)] >= height:
           side_visible = False
           break
    scenic_scores.append(scenic_score)
    x, y = tree_coords
    side_visible = True
    scenic_score = 0
    if y == 0:
        scenic_score = 1
    while y != 0:
        x, y = up(x, y)
        scenic_score += 1
        if trees[(x, y)] >= height:
           side_visible = False
           break
    scenic_scores.append(scenic_score)
    x, y = tree_coords
    side_visible = True
    scenic_score = 0
    if x == max_coord:
        scenic_score = 1
    while x != max_coord:
        x, y = right(x, y)
        scenic_score += 1
        if trees[(x, y)] >= height:
           side_visible = False
           break
    scenic_scores.append(scenic_score)
    x, y = tree_coords
    side_visible = True
    scenic_score = 0
    if x == 0:
        scenic_score = 1
    while x != 0:
        x, y = left(x, y)
        scenic_score += 1
        if trees[(x, y)] >= height:
            break
    scenic_scores.append(scenic_score)
    for score in scenic_scores:
        multiplied_score = multiplied_score * score
    return multiplied_score

def find_visible_trees(tree_heights):
    store_tree_coords(tree_heights)
    visible = 0
    scenic_score = 0
    max_scenic_score = 0
    for tree, height in trees.items():
        scenic_score = find_tree_visibility(tree, height, len(tree_heights[0]) - 1)
        if scenic_score > 0:
            visible += 1
        max_scenic_score = max(scenic_score, max_scenic_score)
    return visible, max_scenic_score

print(find_visible_trees(puzzle_input)) # Part 1: 1672, Part 2: 327180
