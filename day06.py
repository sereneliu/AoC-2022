puzzle_input = open('day06.txt', 'r').read()

def find_marker(datastream_buffer, no_chars):
    for i in range(len(datastream_buffer)):
        if len(set(datastream_buffer[i:i + no_chars])) == no_chars:
            return i + no_chars

print(find_marker(puzzle_input, 4)) # 1155
print(find_marker(puzzle_input, 14)) # 2789
