import streamlit as st
import pandas as pd

def generate_meal_plan(calories, diet_type):
    # Load dataset
    df = pd.read_csv("data/sample_meal.csv")

    # Filter by diet
    filtered = df[df["diet_type"] == diet_type]

    # Just pick 3 random meals (stub logic)
    plan = filtered.sample(3)

    return plan

# Streamlit UI
st.title("🍴 AI Calorie Copilot: Nutrition Assistant")

calories = st.number_input("Daily Calorie Requirement", min_value=1200, max_value=4000, step=100, value=2000)
diet_type = st.selectbox("Diet Preference", ["vegetarian", "vegan", "non-vegetarian", "pescatarian"])

if st.button("Generate Meal Plan"):
    plan = generate_meal_plan(calories, diet_type)

    st.success("Here's your personalized meal plan:")
    st.write(plan[["meal_name", "calories", "protein(g)", "carbs(g)", "fat(g)"]])

    # ✅ Download button
    csv = plan.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Meal Plan as CSV",
        data=csv,
        file_name="meal_plan.csv",
        mime="text/csv",
    )
