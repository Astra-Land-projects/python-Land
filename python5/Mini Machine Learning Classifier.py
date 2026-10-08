from sklearn.neighbors import KNeighborsClassifier

X = [
    [1, 1],
    [1, 2],
    [2, 1],
    [8, 8],
    [9, 8],
    [8, 9]
]

y = [
    "small",
    "small",
    "small",
    "large",
    "large",
    "large"
]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

a = float(input("Feature 1: "))
b = float(input("Feature 2: "))

prediction = model.predict([[a, b]])

print("Prediction:", prediction[0])