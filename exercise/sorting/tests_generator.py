import json
import random
import sys
import os

from solution import sol

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

def generate_testcase(num_elements):
    input_list = [random.randint(-1000, 1000) for _ in range(num_elements)]
    expected_output = sol(input_list)
    return {"input": input_list, "expected_output": expected_output}

def generate_testcases(num_testcases, num_elements):
    testcases = {"test_1": {"input": [], "expected_output": []}}
    for i in range(num_testcases):
        test_name = f"test_{i + 2}"
        testcases[test_name] = generate_testcase(num_elements)
    return testcases

if __name__ == '__main__':
    num_testcases = 15
    num_elements = 10000
    testcases = generate_testcases(num_testcases, num_elements)

    with open(current_dir + '/' +'test_cases.json', 'w') as f:
        json.dump(testcases, f)

    print(f"Generated {num_testcases} test cases with {num_elements} elements each.")
