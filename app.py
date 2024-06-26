import streamlit as st

def main():
    # Set Page Configuration
    st.set_page_config(
        page_title="Compli-Matic: Because You Deserve a Daily Dose of Encouragement!",
        page_icon="🌟",
        layout="wide"
    )

    # Title and description for generating compliments
    st.markdown("<h1 style='text-align: center;'>Compli-Matic 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Because You Deserve a Daily Dose of Encouragement!</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Click the button below to receive a compliment!</p>", unsafe_allow_html=True)

    # Layout with 5 columns
    col1, col2, col3, col4, col5 = st.beta_columns(5)

    # Place empty columns in col1, col2, col4, col5
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass

    # Place button in col3
    with col3:
        center_button = st.button('Generate Compliment', key="generate_button", help="Click to generate compliment")

        if center_button:
            compliment = generate_compliment()
            st.write(f"🌟 {compliment}")

    # Separator
    st.markdown("---")

    # Title and description for sign-up
    st.title("Sign up for Daily Compliments")
    st.write("Enter your name and email address to receive daily compliments!")

    # User input fields for sign-up
    name = st.text_input("Name")
    email = st.text_input("Email")

    # Sign-up button
    if st.button("Sign Up"):
        # Save user sign-up data to database (placeholder)
        save_to_database(name, email)
        st.success("You've successfully signed up for daily compliments!")

    # Built by information
    st.markdown("<h4 style='text-align: center; font-size: small;'>Built by <a href='https://www.linkedin.com/in/harshal-panchal/' target='_blank'>Harshal Panchal</a></h4>", unsafe_allow_html=True)

# Function to save user sign-up data to database (placeholder)
def save_to_database(name, email):
    # Implement database connection and data storage here
    pass

# Function to generate a random compliment
def generate_compliment():
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
    compliment = random.choice(compliments)
    return compliment

if __name__ == "__main__":
    main()
