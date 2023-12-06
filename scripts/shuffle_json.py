import json
import random

def shuffle_jsonl(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()
        random.shuffle(lines)

    with open(output_file, 'w') as f_out:
        f_out.writelines(lines)

# Replace 'input.jsonl' and 'shuffled_output.jsonl' with your file names
#input_file = 'train_hard_to_learn.jsonl'
#output_file = 'train_hard_to_learn_shuffled.jsonl'
input_file = 'train_variability_to_learn.jsonl'
output_file = 'train_variability_to_learn_shuffled.jsonl'

shuffle_jsonl(input_file, output_file)

