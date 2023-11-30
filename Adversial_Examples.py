from transformers import AutoModelForSequenceClassification, AutoTokenizer
from textrobust import generate

# Load the pre-trained Electra model and tokenizer
model_name = "google/electra-small-discriminator"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a dataset using SNLI data
# Note: You may need to install the `nltk` library for WordNet. You can do this with `pip install nltk`.
from textattack.datasets import HuggingFaceDataset
dataset = HuggingFaceDataset("snli", None, "test")

# Augment the dataset using WordNet augmentation
from textattack.augmentation import WordNetAugmenter
augmenter = WordNetAugmenter()

# Specify the attack recipe (TextFoolerJin2019 is used here as an example)
from textattack.attack_recipes import TextFoolerJin2019
attack_recipe = TextFoolerJin2019()

# Generate adversarial examples
for example in dataset:
    premise = example["premise"]
    hypothesis = example["hypothesis"]
    
    # Combine premise and hypothesis
    text = f"{premise} {hypothesis}"

    # Augment the text using WordNet augmentation
    augmented_text = augmenter.augment(text)

    # Generate adversarial examples
    adversarial_text = generate(augmented_text, model, tokenizer)

    # Print the original and adversarial examples
    print(f"Original: {text}")
    print(f"Adversarial: {adversarial_text}\n")
