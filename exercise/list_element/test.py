from exercise import exe
import time
import json
import timeout_decorator
import os
import sys

red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

class Tests:

    test_file = 'test_cases.json'

    def __init__(self):
        with open(current_dir + '/' + self.test_file) as f:
            self.test_cases = json.load(f)
    
    def run_tests(self):
        for test_case in self.test_cases:
            print(test_case, ": ", end="")
            try:
                exe_out = self.run_test(self.test_cases[test_case]['input'], self.test_cases[test_case]['element'])
                if exe_out == self.test_cases[test_case]['expected_output']:
                    print(f"{green}[OK]{reset}")
                else:
                    print(f"{red}[FAIL]{reset}")
                    print("Expected output: ", self.test_cases[test_case]['expected_output'])
                    print("Your output: ", exe_out)
            except timeout_decorator.timeout_decorator.TimeoutError:
                print(f"{red}[FAIL] Timeout{reset}")

    @timeout_decorator.timeout(0.002)  # Imposta il timeout a 2 secondi per questa funzione
    def run_test(self, input, element):
        start_time = time.time()
        exe_out = exe(input, element)
        end_time = time.time()
        print("Elapsed time:", (end_time - start_time) * 1000, "milliseconds")
        return exe_out

if __name__ == '__main__':
    sorting_test = Tests()
    sorting_test.run_tests()


