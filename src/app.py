# src/app.py
import random

# Some fake dataset of Indian meals
meals = {
    "vegetarian": [
        "Moong dal chilla + mint chutney",
        "Quinoa pulao + sprouts salad",
        "Palak paneer + multigrain roti",
        "Oats upma with vegetables",
        "Chole + brown rice"
    ],
    "non_vegetarian": [
        "Grilled chicken + quinoa salad",
        "Fish curry + brown rice",
        "Egg bhurji + multigrain roti",
        "Chicken tikka + sprouts salad",
        "Omelette + oats porridge"
    ]
}

def generate_meal_plan(preference="vegetarian", calories=2000):
    """Fake meal plan generator (placeholder for AI pipeline)."""
    chosen = random.sample(meals[preference], 3)
    return {
        "Calories": calories,
        "Preference": preference,
        "Breakfast": chosen[0],
        "Lunch": chosen[1],
        "Dinner": chosen[2]
    }

if __name__ == "__main__":
    # Example run
    plan = generate_meal_plan(preference="vegetarian", calories=1800)
    print("Generated Meal Plan:")
    for k, v in plan.items():
        print(f"{k}: {v}")
