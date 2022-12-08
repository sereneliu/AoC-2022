puzzle_input = open('day08.txt', 'r').read().split('\n')
sample_input = open('day08_sample.txt', 'r').read().split('\n')

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
    if x == 0 or x == max_coord or y == 0 or y == max_coord:
        return True
    while y != max_coord:
       x, y = down(x, y)
       # print((x, y), trees[(x, y)])
       scenic_score += 1
       if trees[(x, y)] >= height:
           side_visible = False
           break
    if side_visible == True:
        return True
    x, y = tree_coords
    side_visible = True
    while y != 0:
        x, y = up(x, y)
        # print((x, y), trees[(x, y)])
        scenic_score += 1
        if trees[(x, y)] >= height:
           side_visible = False
           break
    if side_visible == True:
        return True
    x, y = tree_coords
    side_visible = True
    while x != max_coord:
        x, y = right(x, y)
        # print((x, y), trees[(x, y)])
        scenic_score += 1
        if trees[(x, y)] >= height:
           side_visible = False
           break
    if side_visible == True:
        return True
    x, y = tree_coords
    side_visible = True
    while x != 0:
        x, y = left(x, y)
        # print((x, y), trees[(x, y)])
        scenic_score += 1
        if trees[(x, y)] >= height:
           return False
    return True, scenic_score

def find_visible_trees(tree_heights):
    store_tree_coords(tree_heights)
    # print(trees)
    visible = 0
    scenic_score = 0
    max_scenic_score = 0
    max_scenic_score = max(scenic_score, max_scenic_score)
    for tree, height in trees.items():
        # print("start", tree, height, len(tree_heights[0]))
        tree_visible, scenic_score = is_tree_visible(tree, height, len(tree_heights[0]) - 1)
        if tree_visible:
            visible += 1
        # print("end", is_tree_visible(tree, height, len(tree_heights[0]) - 1))
    return visible, max_scenic_score

print(find_visible_trees(puzzle_input)) # 1672
# print(find_visible_trees(sample_input))
