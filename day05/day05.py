import sys
import os
import json
import copy

""" TEST
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""
TEST_INIT_STACKS = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
}

""" REAL
[J]             [F] [M]            
[Z] [F]     [G] [Q] [F]            
[G] [P]     [H] [Z] [S] [Q]        
[V] [W] [Z] [P] [D] [G] [P]        
[T] [D] [S] [Z] [N] [W] [B] [N]    
[D] [M] [R] [J] [J] [P] [V] [P] [J]
[B] [R] [C] [T] [C] [V] [C] [B] [P]
[N] [S] [V] [R] [T] [N] [G] [Z] [W]
 1   2   3   4   5   6   7   8   9 
"""
INIT_STACKS = {
    1: ["N", "B", "D", "T", "V", "G", "Z", "J"],
    2: ["S", "R", "M", "D", "W", "P", "F"],
    3: ["V", "C", "R", "S", "Z"],
    4: ["R", "T", "J", "Z", "P", "H", "G"],
    5: ["T", "C", "J", "N", "D", "Z", "Q", "F"],
    6: ["N", "V", "P", "W", "G", "S", "F", "M"],
    7: ["G", "C", "V", "B", "P", "Q"],
    8: ["Z", "B", "P", "N"],
    9: ["W", "P", "J"],
}

def solution_1(input: str, is_test):
    stack = copy.deepcopy(TEST_INIT_STACKS) if is_test else copy.deepcopy(INIT_STACKS)
    for instruction in input.split("\n"):
        instruction_values_only = [int(char) for char in instruction.split(" ") if char.isdigit()]
        move_count,from_stack, to_stack  = tuple(instruction_values_only)

        stack[to_stack] += list(reversed(stack[from_stack][-move_count:]))
        stack[from_stack] = stack[from_stack][:-move_count]
        # print(json.dumps(stack, indent=4))
    
    return ''.join(v[-1] for v in stack.values())

def solution_2(input: str, is_test):
    stack = copy.deepcopy(TEST_INIT_STACKS) if is_test else copy.deepcopy(INIT_STACKS)
    print(stack)
    for instruction in input.split("\n"):
        instruction_values_only = [int(char) for char in instruction.split(" ") if char.isdigit()]
        move_count,from_stack, to_stack  = tuple(instruction_values_only)

        stack[to_stack] += list(stack[from_stack][-move_count:])
        stack[from_stack] = stack[from_stack][:-move_count]
        # print(json.dumps(stack, indent=4))
        print(stack)
    
    
    return ''.join(v[-1] for v in stack.values())

if __name__ == "__main__":
    is_test_arg = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))

    is_test = eval(is_test_arg.split("=")[1])
    file = "test.txt" if is_test else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input, is_test))
    print("Solution 2:", solution_2(input, is_test))

