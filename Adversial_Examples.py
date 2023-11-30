from transformers import AutoModelForSequenceClassification, AutoTokenizer
from textattack.augmentation import WordNetAugmenter
from textattack.attack_recipes import TextFoolerJin2019
from textattack.datasets import HuggingFaceDataset
from textattack.goal_functions import UntargetedClassification

# Load the pre-trained Electra model and tokenizer
model_name = "google/electra-small-discriminator"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a dataset using SNLI data
dataset = HuggingFaceDataset("snli", None, "test")

# Specify the model's goal (in this case, untargeted classification)
goal_function = UntargetedClassification(model)

# Specify the attack recipe (TextFoolerJin2019 is used here as an example)
attack_recipe = TextFoolerJin2019.build(model, tokenizer)

# Augment the dataset using WordNet augmentation
augmenter = WordNetAugmenter()

# Generate adversarial examples
for example in dataset:
    text = example["premise"] + " " + example["hypothesis"]
    augmented_text = augmenter.augment(text)
    
    # Run the attack
    attack_result = attack_recipe.attack(augmented_text, goal_function)

    # Print the original and adversarial examples
    print(f"Original: {text}")
    print(f"Adversarial: {attack_result.perturbed_text}\n")
