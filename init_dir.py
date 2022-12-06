import sys
import os

init_pyscript = """import sys
import os

def solution_1(input: str):
    return 1

def solution_2(input: str):
    return 2


if __name__ == "__main__":
    is_test = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))
    file = "test.txt" if eval(is_test.split("=")[1]) else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input))
    print("Solution 2:", solution_2(input))

"""

directory_name = sys.argv[1]

if os.path.exists(directory_name):
    print(f"{directory_name} directory already exists.")
else:
    os.makedirs(directory_name)
    with open(f"{directory_name}/{directory_name}.py", "w") as pyfile:
        pyfile.write(init_pyscript)
    open(f"{directory_name}/input.txt", "w").close()
    open(f"{directory_name}/test.txt", "w").close()

