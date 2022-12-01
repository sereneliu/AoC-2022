puzzle_input = open('day01.txt', 'r').read().split('\n')

# Part 1

elves_with_food = {}

def assign_to_elves(calories):
    elf = 1
    elves_with_food[elf] = []
    for calorie in calories:
        if calorie == "":
            elf += 1
            elves_with_food[elf] = []
        else:
            elves_with_food[elf].append(int(calorie))

assign_to_elves(puzzle_input)

def sum_calories(calorie_list):
    for elf, calories in calorie_list.items():
        calories.insert(0, sum(calories))

sum_calories(elves_with_food)

def find_most_calories(calorie_list):
    elf_with_most = 0
    most_calories = 0
    for elf, calories in calorie_list.items():
        total = calories[0]
        if total == max(most_calories, total):
            elf_with_most = elf
            most_calories = total
    return elf_with_most, most_calories

print(find_most_calories(elves_with_food)) # 67658

# Part 2

def find_next_most(calorie_list, top_number):
    top_number_total = 0
    for i in range(top_number):
        most_calories = find_most_calories(calorie_list)
        top_number_total += most_calories[1]
        del calorie_list[most_calories[0]]
    return top_number_total

print(find_next_most(elves_with_food, 3)) # 200158
