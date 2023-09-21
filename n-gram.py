import nltk
from sklearn.model_selection import train_test_split
import os
import pickle
from collections import Counter, defaultdict

# Define the preprocessing function
def basic_preprocess_pipeline(data):
    sentences = data.split('\n')
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if len(s) > 0]
    tokenized = [sentence.lower().split() for sentence in sentences]
    return tokenized

def count_n_grams(data, n, start_token='<s>', end_token='<e>'):
    """
    Count all n-grams in the data
    """
    n_grams = defaultdict(Counter)
    for sentence in data:
        sentence = [start_token] * (n-1) + sentence + [end_token]
        for i in range(len(sentence) - n + 1):
            n_gram = tuple(sentence[i:i+n])
            prefix, word = n_gram[:-1], n_gram[-1]
            n_grams[prefix][word] += 1
    return n_grams

# Load and preprocess the data
with open('/Users/bram/Downloads/en_US.twitter.txt', 'r', encoding='utf-8') as file:
    data = file.read()

tokenized_sentences = basic_preprocess_pipeline(data)
train, test = train_test_split(tokenized_sentences, test_size=0.2, random_state=42)
train, val = train_test_split(train, test_size=0.25, random_state=42)

# Build the N-Gram models
n_gram_counts_list = []
for n in range(1, 6):  # Building models from unigram to 5-gram
    n_gram_counts_list.append(count_n_grams(train, n))

# Save the models and data
output_dir = '/Users/bram/Downloads/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the tokenized training data
with open(os.path.join(output_dir, 'tokenized_train.pkl'), 'wb') as file:
    pickle.dump(train, file)

# Save the N-Gram models
for n, n_gram_counts in enumerate(n_gram_counts_list, 1):
    with open(os.path.join(output_dir, f'n_gram_counts_{n}.pkl'), 'wb') as file:
        pickle.dump(n_gram_counts, file)

print("Processing and model building complete. Models and data saved to:", output_dir)

