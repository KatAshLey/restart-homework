from pydantic import BaseModel
import re
from typing import Dict

input_output_dict: Dict[str, bool] = {
    "FAKF-6421": True,
    "JGDE-646": False,
    "65847665": False,
    "6sdfjkn5":False
}
def match_regex(input_str) -> bool:
    test_results = re.search(r"[A-Z]{4}-[0-9]{4}", input_str)
    print(test_results)
    return test_results != None

def main():
    count = 1
    for k, v in input_output_dict.items():
        assert match_regex(input_str=k) == v, f"{count}. Test case failed with expect input {k} to produce {v}"
        count += 1
if __name__ == "__main__":
    main()   
