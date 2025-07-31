import streamlit as st
import random

# Word categories
easy_words = ["apple", "banana", "mango", "orange"]
medium_words = ["python", "java", "monkey", "rust"]
hard_words = ["elephant", "umbrella", "diamond", "computer"]

# Set up session state
if 'secret' not in st.session_state:
    st.session_state.secret = ""
    st.session_state.hint = ""
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.level = "easy"

# Reset the game
def reset_game(level):
    word_list = {
        "easy": easy_words,
        "medium": medium_words,
        "hard": hard_words
    }
    secret = random.choice(word_list.get(level, easy_words))
    st.session_state.secret = secret
    st.session_state.hint = "_" * len(secret)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.level = level

# UI
st.title("🎮 Word Guessing Game")

# Level selection
level = st.selectbox("Choose difficulty level", ["easy", "medium", "hard"])
if st.button("Start New Game"):
    reset_game(level)

# Input guess
if not st.session_state.game_over:
    st.subheader(f"Guess the word ({len(st.session_state.secret)} letters)")
    st.write(f"Hint: **{st.session_state.hint}**")
    guess = st.text_input("Enter your guess: ").lower()

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.secret:
            st.success(f"🎉 Correct! The word was **{st.session_state.secret}**")
            st.info(f"Attempts taken: {st.session_state.attempts}")
            st.session_state.game_over = True
        else:
            # Update hint
            new_hint = ""
            for i in range(len(st.session_state.secret)):
                if i < len(guess) and guess[i] == st.session_state.secret[i]:
                    new_hint += guess[i]
                else:
                    new_hint += "_"
            st.session_state.hint = new_hint
            st.warning("❌ Incorrect! Try again.")
            st.write(f"New Hint: **{st.session_state.hint}**")

else:
    st.balloons()
    if st.button("Play Again"):
        reset_game(st.session_state.level)
