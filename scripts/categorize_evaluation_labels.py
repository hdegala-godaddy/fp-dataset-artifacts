
import jsonlines
from collections import defaultdict

def compare_labels(jsonl_file):
    # Dictionary to store counts of differences for each class of label
    label_diff_counts = defaultdict(int)
    
    # Dictionary to store counts of differences for each label and predicted_label combination
    label_combination_diff_counts = defaultdict(int)

    with jsonlines.open(jsonl_file) as reader:
        for obj in reader:
            label = obj.get('label', '')
            predicted_label = obj.get('predicted_label', '')

            # Increment count if label and predicted_label differ
            if label != predicted_label:
                label_diff_counts[label] += 1
                
                # Increment count for each label and predicted_label combination
                label_combination_diff_counts[(label, predicted_label)] += 1

    return label_diff_counts, label_combination_diff_counts

# Example usage
jsonl_file_path = 'path/to/your/file.jsonl'
label_diffs, label_combination_diffs = compare_labels(jsonl_file_path)

# Print the overall result
for label, diff_count in label_diffs.items():
    print(f'Differences for label "{label}": {diff_count}')

# Print the result for each label and predicted_label combination
for (label, predicted_label), combination_diff_count in label_combination_diffs.items():
    print(f'Differences for label "{label}" and predicted label "{predicted_label}": {combination_diff_count}')

