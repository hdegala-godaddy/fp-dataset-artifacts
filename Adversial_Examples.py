from transformers import AutoModelForSequenceClassification, AutoTokenizer
from textattack.augmentation import WordNetAugmenter
from textattack.attack_recipes import TextFoolerJin2019
from textattack.datasets import HuggingFaceDataset
from textattack import Attack

# Load the pre-trained Electra model and tokenizer
model_name = "google/electra-small-discriminator"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a dataset using SNLI data
dataset = HuggingFaceDataset("snli", None, "test")

# Specify the attack recipe (TextFoolerJin2019 is used here as an example)
attack_recipe = TextFoolerJin2019.build(model, tokenizer)

# Augment the dataset using WordNet augmentation
augmenter = WordNetAugmenter()

# Custom goal function for untargeted classification
def custom_goal_function(inputs):
    return model(inputs)

# Instantiate the attack method
attack = Attack(goal_function=custom_goal_function, constraints=attack_recipe.constraints(), transformation=attack_recipe.transformation())

# Generate adversarial examples
for example in dataset:
    text = example["premise"] + " " + example["hypothesis"]
    augmented_text = augmenter.augment(text)
    
    # Run the attack
    attack_result = attack.attack(augmented_text)

    # Print the original and adversarial examples
    print(f"Original: {text}")
    print(f"Adversarial: {attack_result.perturbed_text}\n")
