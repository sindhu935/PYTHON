
import random

# Define Prosthetic class
class Prosthetic:
    def __init__(self, model_name, material, weight, cost, durability_score):
        self.model_name = model_name
        self.material = material
        self.weight = weight          # in kg
        self.cost = cost              # in USD
        self.durability_score = durability_score  # scale 1-10
    
    def display_info(self):
        print(f"--- {self.model_name} ---")
        print(f"Material: {self.material}")
        print(f"Weight: {self.weight} kg")
        print(f"Cost: ${self.cost}")
        print(f"Durability: {self.durability_score}/10\n")
    
    def simulate_use(self, hours):
        """Simulate prosthetic usage and reduce durability"""
        wear = hours * random.uniform(0.03, 0.07)
        self.durability_score = max(0, self.durability_score - wear)
        print(f"After {hours} hours of use, durability is {self.durability_score:.2f}/10\n")
    
    def is_usable(self):
        return self.durability_score > 2

# Define function to optimize cost vs durability
def optimize_prosthetic(material_options, budget):
    best_option = None
    for material in material_options:
        weight = round(random.uniform(0.8, 1.5), 2)  # kg
        durability = round(random.uniform(6, 10), 1)
        cost = round(weight * material_options[material]["cost_factor"], 2)
        if cost <= budget:
            prosthetic = Prosthetic(f"LifeStep-{material}", material, weight, cost, durability)
            if not best_option or prosthetic.durability_score > best_option.durability_score:
                best_option = prosthetic
    return best_option

# Material options with cost factor (USD/kg)
materials = {
    "PLA Plastic": {"cost_factor": 40},
    "ABS Plastic": {"cost_factor": 45},
    "Carbon Fiber": {"cost_factor": 70},
    "Aluminum Alloy": {"cost_factor": 60}
}

# Budget for low-cost prosthetic
budget = 80  # USD

# Optimize prosthetic selection
selected_prosthetic = optimize_prosthetic(materials, budget)

# Display prosthetic details
if selected_prosthetic:
    selected_prosthetic.display_info()

    # Simulate usage
    selected_prosthetic.simulate_use(15)  # 15 hours simulated use
    print(f"Is prosthetic usable? {'Yes' if selected_prosthetic.is_usable() else 'No'}")
else:
    print("No suitable prosthetic could be designed within the budget.")
