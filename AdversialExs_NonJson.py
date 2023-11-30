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
    premise = example["premise"]
    hypothesis = example["hypothesis"]
    text = f"{premise} {hypothesis}"

    # Augment the text using WordNet-based synonym replacement
    augmented_text = augmenter.augment(text)

    # Tokenize the augmented text
    inputs = tokenizer(augmented_text, return_tensors="pt", truncation=True)

    # Make a prediction using the model
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=1)

    # Convert the predictions to a human-readable label
    predicted_label = tokenizer.convert_ids_to_tokens(predictions.item())

    return text, augmented_text, predicted_label

# Generate adversarial examples
for example in dataset:
    original_text, adversarial_text, predicted_label = attack_example(example)

    # Print the original and adversarial examples
    print(f"Original: {original_text}")
    print(f"Adversarial: {adversarial_text}")
    print(f"Predicted Label: {predicted_label}\n")
