import tensorflow as tf
from tensorflow.keras import layers

texts = [
    "Python programming tutorial",
    "Learn machine learning",
    "Football match tonight",
    "The team won the game",
    "Python code and algorithms",
    "The player scored a goal"
]

labels = [0, 0, 1, 1, 0, 1]

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

test_texts = [
    "machine learning with Python",
    "football player scored"
]

predictions = model.predict(test_texts, verbose=0)

for text, prediction in zip(test_texts, predictions):
    category = "Sports" if prediction[0] >= 0.5 else "Technology"
    print(f"{text} -> {category}")