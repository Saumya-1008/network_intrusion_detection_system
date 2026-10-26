import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("data/intrusion.csv")

# Convert protocol to numeric
protocol_map = {'tcp':0,'udp':1,'icmp':2}
data['protocol'] = data['protocol'].map(protocol_map)

# Convert labels
label_map = {'normal':0,'dos':1,'scan':2}
data['label'] = data['label'].map(label_map)

X = data.drop("label", axis=1)
y = data["label"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved!")