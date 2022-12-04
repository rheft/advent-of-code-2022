
import sys
import os

def solution_1(input: str):
    pairs = input.split("\n")
    count_fully_duplicated = 0
    for pair in pairs:
        # print(pair)
        elf1, elf2 = pair.split(",")[0], pair.split(",")[1]
        elf1_set = set(list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)))
        elf2_set = set(list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)))
        if elf1_set.issubset(elf2_set) or elf2_set.issubset(elf1_set):
            count_fully_duplicated += 1

    # print(count_fully_duplicated)
    return count_fully_duplicated

def solution_2(input: str):
    pairs = input.split("\n")
    count_semi_duplicated = 0
    for pair in pairs:
        # print(pair)
        elf1, elf2 = pair.split(",")[0], pair.split(",")[1]
        elf1_set = set(list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)))
        elf2_set = set(list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)))
        if len(elf1_set.intersection(elf2_set)) > 0:
            count_semi_duplicated += 1

    # print(count_fully_duplicated)
    return count_semi_duplicated


if __name__ == "__main__":
    is_test = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))
    file = "test.txt" if eval(is_test.split("=")[1]) else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input))
    print("Solution 2:", solution_2(input))

