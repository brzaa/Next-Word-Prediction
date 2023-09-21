import streamlit as st
import pickle
from collections import defaultdict

def load_model(n):
    """Load the N-Gram model on demand."""
    with open(f'/Users/bram/Downloads/n_gram_counts_{n}.pkl', 'rb') as file:
        return pickle.load(file)

def predict_next_word(n, history, top_k=3):
    """Load the appropriate model and provide top_k word predictions based on the history."""
    model = load_model(n)
    predictions = model.get(history, {})
    return sorted(predictions, key=predictions.get, reverse=True)[:top_k]

# Streamlit app
st.title('Kelompok 4 Autocomplete App')
user_input = st.text_input('Enter up to 4 words in english:')
user_tokens = user_input.split()

# Check the number of words and use the appropriate N-Gram model
if 1 <= len(user_tokens) <= 4:
    history = tuple(user_tokens)
    n = len(user_tokens) + 1
    predictions = predict_next_word(n, history)
    st.write(f"Suggested completions for {n}-Gram: {', '.join(predictions)}")
else:
    st.write("Please enter a sequence of 1 to 4 words.")

