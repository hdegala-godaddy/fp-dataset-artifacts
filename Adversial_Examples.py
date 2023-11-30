import json
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from nlpaug.util import Action
import nlpaug.augmenter.word as naw
from textattack.datasets import HuggingFaceDataset

# Load the pre-trained Electra model and tokenizer
model_name = "google/electra-small-discriminator"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a dataset using SNLI data
dataset = HuggingFaceDataset("snli", None, "test")

# Create a WordNet-based augmenter
augmenter = naw.SynonymAug(aug_src='wordnet')

# Function to perform an adversarial attack
def attack_example(example):
    premise = example[0]["premise"]
    hypothesis = example[0]["hypothesis"]
    text = f"{premise} {hypothesis}"

    # Augment the text using WordNet-based synonym replacement
    augmented_text = augmenter.augment(text)

    # Tokenize the augmented text
    inputs = tokenizer(augmented_text, return_tensors="pt", truncation=True)

    # Make a prediction using the model
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=1)

    # Convert the predictions to a human-readable label
    predicted_label = predictions.item()

    return {
        "premise": premise,
        "hypothesis": hypothesis,
        "label": predicted_label
    }

# Output JSONL file
output_file_path = "adversarial_results.jsonl"
limit = 1000
count = 0

# Generate adversarial examples and save to JSONL file
with open(output_file_path, "w") as output_file:
    for example in dataset:
        result = attack_example(example)
        output_file.write(json.dumps(result) + "\n")
        
        count += 1
        if count >= limit:
            break

print(f"Adversarial results saved to: {output_file_path}")
