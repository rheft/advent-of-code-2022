import sys
import os

init_pyscript = """import sys
import os

def solution_1(input: str, is_test: bool = True):
    return 1

def solution_2(input: str, is_test: bool = True):
    return 2


if __name__ == "__main__":
    is_test_arg = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))

    is_test = eval(is_test_arg.split("=")[1])
    file = "test.txt" if is_test else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input, is_test))
    print("Solution 2:", solution_2(input, is_test))

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

