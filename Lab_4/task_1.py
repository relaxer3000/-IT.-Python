# TODO решите задачу
import json


FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, 'r') as f:
        data = json.load(f)
    b = [dictt["score"] * dictt['weight'] for dictt in data]
    return round(sum(b), 3)

print(task())
