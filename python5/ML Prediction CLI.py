import joblib

model = joblib.load(
    "model.pkl"
)

values = input(
    "Features separated by space: "
)

features = [
    float(x)
    for x in values.split()
]

prediction = model.predict(
    [features]
)

print(
    "Prediction:",
    prediction[0]
)