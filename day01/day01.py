import sys
import os

def solution_1(input: str):
    elves_calorie_stash = []
    current_elf = []

    for i in input.split("\n"):
        if i != "":
            current_elf.append(int(i))
        else:
            elves_calorie_stash.append(current_elf)
            current_elf = []

    elves_calorie_stash.append(current_elf)
    calorie_stash_sums = [sum(i) for i in elves_calorie_stash]
    sorted_stash_sums = sorted(calorie_stash_sums, reverse=True)
    
    max_calorie_stash = sorted_stash_sums[0]
    
    return max_calorie_stash

def solution_2(input: str):
    elves_calorie_stash = []
    current_elf = []

    for i in input.split("\n"):
        if i != "":
            current_elf.append(int(i))
        else:
            elves_calorie_stash.append(current_elf)
            current_elf = []

    elves_calorie_stash.append(current_elf)
    calorie_stash_sums = [sum(i) for i in elves_calorie_stash]
    
    sorted_stash_sums = sorted(calorie_stash_sums, reverse=True)
    top3_calorie_stash = sum(sorted_stash_sums[:3])
    print(sorted_stash_sums[:3])
    
    return top3_calorie_stash


if __name__ == "__main__":
    is_test = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))
    file = "test.txt" if eval(is_test.split("=")[1]) else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input))
    print("Solution 2:", solution_2(input))
