from qtest_connector import get_test_cases
from config import PROJECT_ID

def main():

    test_cases = get_test_cases(PROJECT_ID)

    if test_cases:
        print("Fetched Test Cases:")
        for tc in test_cases:
            print(tc)

if __name__ == "__main__":
    main()