import json

def validate_and_write_valid_lines(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line_num, line in enumerate(f_in, start=1):
            try:
                json_object = json.loads(line)

                # Check if "label" is present and is of type number
                if 'label' in json_object and isinstance(json_object['label'], (int, float)):
                    # If the line is a valid JSON object with a numeric "label," write it to the output file
                    f_out.write(line)
                else:
                    print(f"Error in line {line_num}: 'label' field is not a number.")

            except json.JSONDecodeError as e:
                print(f"Error in line {line_num}: {e}")

# Replace 'input.jsonl' and 'output_valid.jsonl' with your file names
validate_and_write_valid_lines('train.jsonl', 'train_2.jsonl')