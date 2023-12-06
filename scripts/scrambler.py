import json
import random

def scramble_jsonl(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    random.shuffle(lines)

    with open(output_file, 'w') as f:
        f.writelines(lines)

# Replace 'input.jsonl' and 'output.jsonl' with your file names
scramble_jsonl('modified_train_sorted.jsonl', 'train.jsonl')
