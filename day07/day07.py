from curses.ascii import isdigit
import sys
import os

def solution_1(input: str, is_test: bool = True):
    instructions = input.split("\n")
    size_map = {}
    pwd = []
    files_considered = []
    for inst in instructions:
        # print(inst)
        if inst.startswith("$ cd"):
            new_cwd = inst.split(" ")[-1]
            
            # Manage pwd
            if new_cwd == "..":
                pwd.pop()
            else:
                pwd.append(new_cwd)

        if inst.split(" ")[0].isdigit() and ''.join(pwd)+"/"+inst.split(" ")[1] not in files_considered:
            files_considered.append(''.join(pwd)+"/"+inst.split(" ")[1])
            size = int(inst.split(" ")[0])
            pwd_paths = ['/'.join(pwd[:i]) for i in range(1, len(pwd)+1)]
            # print(f"Adding {size} to each of {pwd_paths}")
            for dir in pwd_paths:
                curr_size = size_map.get(dir, 0) + size
                size_map[dir] = curr_size 
            
    # print(size_map)

    max_size = 100000
        # print({k:v for k,v in size_map.items() if v <= max_size})
    return sum([size for size in size_map.values() if size <= max_size])

def solution_2(input: str, is_test: bool = True):
    instructions = input.split("\n")
    size_map = {}
    pwd = []
    files_considered = []
    for inst in instructions:
        if inst.startswith("$ cd"):
            new_cwd = inst.split(" ")[-1]
            
            # Manage pwd
            if new_cwd == "..":
                pwd.pop()
            else:
                pwd.append(new_cwd)

        if inst.split(" ")[0].isdigit() and ''.join(pwd)+"/"+inst.split(" ")[1] not in files_considered:
            files_considered.append(''.join(pwd)+"/"+inst.split(" ")[1])
            size = int(inst.split(" ")[0])
            pwd_paths = ['/'.join(pwd[:i]) for i in range(1, len(pwd)+1)]
            for dir in pwd_paths:
                curr_size = size_map.get(dir, 0) + size
                size_map[dir] = curr_size 
            
    print(size_map)

    total_disk_space = 70000000
    required_space_for_update = 30000000

    total_space_used = size_map['/']
    unused_space = total_disk_space-total_space_used

    min_deletion_size = required_space_for_update-unused_space
    
    deletion_candidates = [size for size in size_map.values() if size >= min_deletion_size]
    print(f"Total space used: {total_space_used}")
    print(f"Unused Space: {unused_space}")
    print(f"Minimum deletion required: {min_deletion_size}")
    print(f"Deletion candiate sizes: {deletion_candidates}")

    return sorted(deletion_candidates, reverse=False)[0]


if __name__ == "__main__":
    is_test_arg = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))

    is_test = eval(is_test_arg.split("=")[1])
    file = "test.txt" if is_test else "input.txt"

    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input, is_test))
    print("Solution 2:", solution_2(input, is_test))

