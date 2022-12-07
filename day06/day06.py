import sys
import os

def solution_1(input: str, is_test: bool = True):
    window = 4
    for datastream in input.split("\n"):
        for i in range(len(datastream) - window + 1):
            if len(set(datastream[i:i+window])) == window:
                return i + window

def solution_2(input: str, is_test: bool = True):
    window = 14
    for datastream in input.split("\n"):
        for i in range(len(datastream) - window + 1):
            if len(set(datastream[i:i+window])) == window:
                return i + window


if __name__ == "__main__":
    is_test_arg = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))
    
    is_test = eval(is_test_arg.split("=")[1])
    file = "test.txt" if is_test else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input, is_test))
    print("Solution 2:", solution_2(input, is_test))

