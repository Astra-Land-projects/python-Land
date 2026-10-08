import string
from collections import Counter
import math
import random

# 1. Data Collection (Example - Replace with your own dataset)
def load_data(filepath):
    """Loads text data from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = [line.strip() for line in f]
    return data

# 2. Preprocessing
def preprocess_text(text):
    """Removes punctuation and converts to lowercase."""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# 3. Vocabulary Creation
def create_vocabulary(data):
    """Creates a vocabulary from the given data."""
    all_words = []
    for text in data:
        words = preprocess_text(text).split()
        all_words.extend(words)
    return set(all_words)

# 4. Vectorization (Bag-of-Words)
def vectorize_text(text, vocabulary):
    """Converts text to a vector based on word counts."""
    words = preprocess_text(text).split()
    vector = [words.count(word) for word in vocabulary]
    return vector

# 5. Training (Simple Naive Bayes)
def train_model(training_data, labels, vocabulary):
    """Trains a Naive Bayes classifier."""
    positive_counts = Counter()
    negative_counts = Counter()
    positive_total = 0
    negative_total = 0

    for i, text in enumerate(training_data):
        vector = vectorize_text(text, vocabulary)
        if labels[i] == 'positive':
            positive_counts.update(vector)
            positive_total += 1
        elif labels[i] == 'negative':
            negative_counts.update(vector)
            negative_total += 1

    # Laplace Smoothing
    positive_counts = {word: count + 1 for word, count in positive_counts.items()}
    negative_counts = {word: count + 1 for word, count in negative_counts.items()}
    vocabulary_size = len(vocabulary)
    positive_total = positive_total + vocabulary_size
    negative_total = negative_total + vocabulary_size

    return positive_counts, negative_counts, positive_total, negative_total

# 6. Prediction
def predict_sentiment(text, vocabulary, positive_counts, negative_counts, positive_total, negative_total):
    """Predicts the sentiment of a given text."""
    vector = vectorize_text(text, vocabulary)

    positive_prob = 1.0
    negative_prob = 1.0

    for i, count in enumerate(vector):
        positive_prob *= (positive_counts[list(vocabulary)[i]] / positive_total) if count > 0 else 1.0
        negative_prob *= (negative_counts[list(vocabulary)[i]] / negative_total) if count > 0 else 1.0

    if positive_prob > negative_prob:
        return 'positive'
    else:
        return 'negative'

# Main Execution
if __name__ == "__main__":
    # Load data
    data = load_data('sentiment_data.txt')  # Replace with your file

    # Split data into training and testing sets
    random.shuffle(data)
    split_index = int(0.8 * len(data))
    training_data = data[:split_index]
    testing_data = data[split_index:]

    # Create labels (assuming your data has labels like 'positive' or 'negative')
    labels = ['positive'] * (split_index // 2) + ['negative'] * (split_index - split_index // 2) #Example
    # Create vocabulary
    vocabulary = create_vocabulary(training_data)

    # Train the model
    positive_counts, negative_counts, positive_total, negative_total = train_model(training_data, labels, vocabulary)

    # Test the model
    correct_predictions = 0
    for i, text in enumerate(testing_data):
        predicted_sentiment = predict_sentiment(text, vocabulary, positive_counts, negative_counts, positive_total, negative_total)
        actual_sentiment = labels[i + split_index] #Corrected index
        if predicted_sentiment == actual_sentiment:
            correct_predictions += 1

    accuracy = correct_predictions / len(testing_data)
    print(f"Accuracy: {accuracy}")

    # Example Prediction
    new_text = "This is a great movie!"
    predicted_sentiment = predict_sentiment(new_text, vocabulary, positive_counts, negative_counts, positive_total, negative_total)
    print(f"Sentiment of '{new_text}': {predicted_sentiment}")