
import sys
import os

def solution_1(input: str):
    score = 0
    for rucksack in input.split("\n"):
        length = len(rucksack)
        break_point = int(length/2)
        comp_1 = set(rucksack[:break_point])
        comp_2 = set(rucksack[break_point:])
        
        common = comp_1.intersection(comp_2)
        for char in common:
            if char.isupper():
                score += (ord(char) % 64) + 26 # Base of upper ASCII
            else:
                score += ord(char) % 96 # Base of lower ASCII
        
    return score

def solution_2(input: str):
    rucksacks = input.split("\n")
    rucksack_count = len(rucksacks)
    
    score = 0 
    i = 0
    while i < rucksack_count:
        group = rucksacks[i:i+3]
        common_items = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))

        for char in common_items:
            if char.isupper():
                score += (ord(char) % 64) + 26 # Base of upper ASCII
            else:
                score += ord(char) % 96 # Base of lower ASCII
        i+=3
    return score


if __name__ == "__main__":
    is_test = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))
    file = "test.txt" if eval(is_test.split("=")[1]) else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input))
    print("Solution 2:", solution_2(input))

