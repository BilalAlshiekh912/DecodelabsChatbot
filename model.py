# Import necessary libraries and dataset and perform data preprocessing steps such as splitting the dataset into training and testing sets, and scaling the features.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

iris  = load_iris()
x  = iris.data
y  = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42,shuffle=True)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


model = KNeighborsClassifier(n_neighbors=5)

model.fit(x_train_scaled, y_train)

predictions = model.predict(x_test_scaled)

print(f'First 10 Predictions: {predictions[:10]}')
print(f'Actual Labels: {y_test[:10]}')

if predictions[:10].tolist() == y_test[:10].tolist():
    print("The model's predictions match the actual labels for the first 10 samples.")