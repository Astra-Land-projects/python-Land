import tensorflow as tf
from tensorflow.keras import layers

texts = [
    "I love this product",
    "This is amazing",
    "Very good experience",
    "I hate this",
    "This is terrible",
    "Very bad experience",
]

labels = [1, 1, 1, 0, 0, 0]

vectorizer = layers.TextVectorization(
    max_tokens=1000,
    output_sequence_length=20
)

vectorizer.adapt(texts)

model = tf.keras.Sequential([
    vectorizer,
    layers.Embedding(1000, 32),
    layers.GlobalAveragePooling1D(),
    layers.Dense(16, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(texts, labels, epochs=30, verbose=0)

sentences = [
    "I really love it",
    "This is very bad"
]

predictions = model.predict(sentences, verbose=0)

for text, prediction in zip(sentences, predictions):
    sentiment = "Positive" if prediction[0] >= 0.5 else "Negative"
    print(f"{text} -> {sentiment}")