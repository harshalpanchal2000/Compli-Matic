import streamlit as st
import random

# List of compliments
compliments = [
    "You're a ray of sunshine on a cloudy day!",
    "You have the best laugh!",
    "Your positivity is infectious!",
    "You're as cool as a cucumber!",
    "You're one in a million!",
    "You're a superhero in disguise!",
    "You're doing great!",
    "You're simply amazing!",
    "You're a work of art!",
    "You're the bee's knees!",
    "You light up the room!",
    "You're a total rockstar!",
    "You're a wizard at being awesome!",
    "You're a shining star!",
    "You're the cat's pajamas!",
    "You're a legend!",
    "You're a true gem!",
    "You're a champion!",
    "You're a breath of fresh air!",
    "You're fantastic!"
]

# Function to generate a random compliment
def generate_compliment():
    compliment = random.choice(compliments)
    return compliment

# Main Streamlit app
def main():
    st.title("Compli-Matic")

    st.write("Click the button below to receive a compliment!")

    if st.button("Generate Compliment"):
        compliment = generate_compliment()
        st.write(f"🌟 {compliment}")

if __name__ == "__main__":
    main()
