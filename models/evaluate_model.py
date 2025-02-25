from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

data = pd.read_csv('data.csv')
X = data.drop(columns=['target'])
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)

joblib.dump(model, 'backend/model.pkl')

predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
