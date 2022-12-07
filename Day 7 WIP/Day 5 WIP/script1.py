# =============================================================================
# class directory:
#     
#     def __init__(self, 
#                  directories_contained, 
#                  files_contained_directly,
#                  size):
#           self.directories_
# =============================================================================



#%%

def parse_line(line):
    """
    A line can either be a command (cd or ls), or a directory, or a file.
    Return list of format (type, name, size)
    """
    first, second, third = None, None, None
    if line[0] == "$": # If it's a command.
        if line[2:4] == "cd":
            first = "cd command"
            second = line.split(" ")[-1]
        elif line[2:4] == "ls":
            first = "ls command"
    if line[:3] == "dir":
        first = "directory"
        second = line.split(" ")[-1]
    if ord(line[0]) >= 48 and ord(line[0]) <= 57: # Starts with a number so file.
        first = "file"
        second = line.split(" ")[-1]
        third = int(line.split(" ")[-2]) # Size of file.
    return first, second, third
            
def get_directory_top_level_size(directory_name, parsed_lines):
    directory_start_index = -1
    for line_index in range(len(parsed_lines)):
        if parsed_lines[line_index][0] == "cd command":
            if parsed_lines[line_index][1] == directory_name: # Found it!
                directory_start_index = line_index
    if directory_start_index == -1:
        raise Exception("Change to directory line not found.")
        
    line_index = directory_start_index
    discovered_size = 0
    
    while True:
        line_index += 1
        if parsed_lines[line_index][0] == "file":
            discovered_size += parsed_lines[line_index][2]
        if parsed_lines[line_index][0] == "cd command":
            break
        if line_index == len(parsed_lines) - 1:
            break
        
    return discovered_size

#%%
def get_directories_contained_directly(directory_name, parsed_lines):
    directory_start_index = -1
    for line_index in range(len(parsed_lines)):
        if parsed_lines[line_index][0] == "cd command":
            if parsed_lines[line_index][1] == directory_name: # Found it!
                directory_start_index = line_index
    if directory_start_index == -1:
        raise Exception("Change to directory line not found.")
        
    line_index = directory_start_index
    discovered_directories = []
        
    while True:
        line_index += 1
        if parsed_lines[line_index][0] == "directory":
            discovered_directories.append(parsed_lines[line_index][1])
        if parsed_lines[line_index][0] == "cd command" :
            break
        if parsed_lines[line_index][0] == "ls command" :
            break
        if line_index == len(parsed_lines) - 1:
            break
    
    return discovered_directories


#%%

def get_directory_list(parsed_lines):
    directory_list = []
    for line in parsed_lines:
        if line[0] == "cd command":
            if line[1] in directory_list:
                pass
            else:
                if line[1] != "..":
                    directory_list.append(line[1])
    return directory_list

#%%

def get_directory_size(directory_name, parsed_lines):
    size = get_directory_top_level_size(directory_name, parsed_lines)
    for nested_directory in get_directories_contained_directly(directory_name, parsed_lines):
        size += get_directory_size(nested_directory, parsed_lines)
    return size

#%%
#%%

filename = "input.txt"
with open(filename) as file:
    lines = file.read().splitlines()
lines_parsed = []
for line in lines:
    lines_parsed.append(parse_line(line))

directory_sizes= []
all_directories = get_directory_list(lines_parsed)
for directory in all_directories:
    directory_sizes.append(get_directory_size(directory, lines_parsed))

sum_over_threshold = 0
for size in directory_sizes:
    if size <= 100000:
        sum_over_threshold += size
    
print(f"Sum of relevant sizes: {sum_over_threshold}")
