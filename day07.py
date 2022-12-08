# import the os module
import os

# read the input file
puzzle_input = open('day07.txt', 'r').read().split('\n')

# create an empty dictionary to store the directories
directories = {}
# directory = key
# contains a tuple with the following elements:
# - a list of subdirectories
# - the total file size (not including subdirectories)

def parser(lines, directories):
    # initialize the current directory
    current_dir = '/'

    # iterate over the lines of the input
    for line in lines:
        # strip any leading or trailing whitespace from the line
        line = line.strip()

        # if the line is empty, skip it
        if not line:
            continue

        # split the line into words
        words = line.split()

        # if the line starts with a "$" character, it is a command
        if words[0] == '$':
            # the second word is the command
            command = words[1]

            # if the command is "cd", update the current directory
            if command == 'cd':
                # get the directory to change to
                new_dir = words[2]

                # if the directory exists, update the current directory
                if new_dir in directories:
                    current_dir = new_dir

            # if the command is "ls", list the contents of the current directory
            elif command == 'ls':
                # if the current directory is not already in the dictionary,
                # add it and initialize the subdirectories list and file size
                if current_dir not in directories:
                    directories[current_dir] = [[], 0]

        # if the line does not start with a "$" character, it is a directory or file
        else:
            # split the line on the first space character
            name, rest = line.split(' ', 1)

            # if the line is a directory, add it to the list of subdirectories
            # for the current directory
            if name == 'dir':
                subdir = rest.strip()
                directories[current_dir][0].append(subdir)

                # parse the subdirectory
                subdir_lines = puzzle_input[lines.index(line) + 1:]
                parser(subdir_lines, directories)
            # if the line is a file, add its size to the total file size
            # for the current directory
            else:
                # parse the file size as an integer
                file_size = int(name)
                directories[current_dir][1] += file_size

# print the directories to check that they are correct
parser(puzzle_input, directories)
print(directories)
