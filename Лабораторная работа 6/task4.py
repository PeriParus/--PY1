import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(INPUT_FILE,determinater=',') -> list[dict]:
    with open(INPUT_FILE,"r") as f:
        headers_list=f.readline()[:-1].split(determinater)
        lines_list=[line[:-1].split(determinater) for line in f.readlines()]
        return[dict(zip(headers_list,line)) for line in lines_list]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
