from transformers import AutoModelForSequenceClassification, AutoTokenizer
from textattack.augmentation import WordNetAugmenter
from textattack.attack_recipes import TextFoolerJin2019
from textattack.datasets import HuggingFaceDataset
from textattack import Attack, GoalFunction

# Load the pre-trained Electra model and tokenizer
model_name = "google/electra-small-discriminator"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a dataset using SNLI data
dataset = HuggingFaceDataset("snli", None, "test")

# Augment the dataset using WordNet augmentation
augmenter = WordNetAugmenter()

# Custom goal function for untargeted classification
class CustomGoalFunction(GoalFunction):
    def __call__(self, model_output):
        # Customize this function based on the output of your model
        return model_output

# Specify the attack recipe (TextFoolerJin2019 is used here as an example)
attack_recipe = TextFoolerJin2019()

# Instantiate the attack method with the model and tokenizer
attack = Attack(goal_function=CustomGoalFunction(), transformation=attack_recipe, model_wrapper=(model, tokenizer))

# Generate adversarial examples
for example in dataset:
    text = example["premise"] + " " + example["hypothesis"]
    augmented_text = augmenter.augment(text)
    
    # Run the attack
    attack_result = attack.attack(augmented_text)

    # Print the original and adversarial examples
    print(f"Original: {text}")
    print(f"Adversarial: {attack_result.perturbed_text}\n")
