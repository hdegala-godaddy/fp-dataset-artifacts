import json

def extract_fields(input_file, output_file, fields_to_extract):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            try:
                json_object = json.loads(line)

                # Extract specified fields
                extracted_data = {field: json_object.get(field, None) for field in fields_to_extract}

                # Write the extracted data to the output file
                json.dump(extracted_data, f_out)
                f_out.write('\n')

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

# Replace 'input.jsonl', 'output_extracted.jsonl', and ['field1', 'field2'] with your file names and fields
input_file = 'scitail_1.0_dev.jsonl'
output_file = 'scitail_1.0_extracted.jsonl'
fields_to_extract = ['sentence1', 'sentence2', 'gold_label']

extract_fields(input_file, output_file, fields_to_extract)

