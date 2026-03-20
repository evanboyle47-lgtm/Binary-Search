import streamlit as st
import random

# --- CONFIG & STYLING ---
st.set_page_config(page_title="Stetson CS - Binary Battle", page_icon="🎓")

# Custom CSS to match your Stetson Green & Gold theme
st.markdown("""
    <style>
    .main { background-color: #121212; color: white; }
    .stButton>button { background-color: #CFB53B; color: black; font-weight: bold; width: 100%; border-radius: 5px; }
    .stHeader { color: #006747; }
    h1, h2, h3 { color: #CFB53B !important; }
    div[data-testid="stMetricValue"] { color: #3498db !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (Keeps data across clicks) ---
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses = []
    st.session_state.game_over = False

# --- HEADER ---
st.image("https://www.stetson.edu/main/media/images/logos/stetson-u-logo.png", width=200) # Optional: uses Stetson logo if URL is valid
st.title("Binary Battle: You vs. Math")
st.subheader("Department of Computer Science")

# --- SIDEBAR (History) ---
st.sidebar.header("📜 Guess History")
for i, g in enumerate(st.session_state.guesses):
    st.sidebar.write(f"Attempt {i+1}: **{g}**")

# --- GAME LOGIC ---
if not st.session_state.game_over:
    st.write("I'm thinking of a number between **1 and 100**.")
    st.write("Can you beat the algorithm's **7-step** limit?")

    # Input area
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="current_guess")
    
    if st.button("SUBMIT GUESS"):
        st.session_state.guesses.append(guess)
        
        if guess < st.session_state.secret_number:
            st.error(f"{guess} is TOO LOW! ⬆️")
        elif guess > st.session_state.secret_number:
            st.warning(f"{guess} is TOO HIGH! ⬇️")
        else:
            st.session_state.game_over = True
            st.balloons()
            st.rerun()

# --- WIN SCREEN ---
else:
    st.success(f"🎊 SUCCESS! The number was {st.session_state.secret_number}")
    st.write(f"You found it in **{len(st.session_state.guesses)}** guesses.")
    
    # The "Science" explanation
    st.info(f"""
    **Algorithm Discovery:**
    A Binary Search algorithm would have found this in **7 steps or fewer**.
    By splitting the 100 numbers in half every time, it uses **O(log n)** efficiency!
    """)
    
    if st.button("PLAY AGAIN"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.guesses = []
        st.session_state.game_over = False
        st.rerun()