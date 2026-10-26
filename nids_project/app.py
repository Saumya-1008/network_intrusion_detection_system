import pandas as pd
data = pd.read_csv("KDDTrain+.txt", header=None)

import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import random
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
from sklearn.preprocessing import LabelEncoder

for col in X.columns:
    if X[col].dtype == 'object':
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])


 # protocol column
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2
)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Train model
X = np.array([
    [10,0,100,200],
    [5,1,300,100],
    [2,2,400,10],
    [20,0,500,300],
    [3,1,70,20]
])

y = np.array([0,1,2,1,0])

model = RandomForestClassifier()
model.fit(X,y)

st.title("🚨 Network Intrusion Detection System")

duration = st.number_input("Duration", min_value=0.0)
protocol = st.selectbox("Protocol", ["tcp","udp","icmp"])
src = st.number_input("Source Bytes", min_value=0.0)
dst = st.number_input("Destination Bytes", min_value=0.0)

protocol_map = {"tcp":0,"udp":1,"icmp":2}

if st.button("Detect"):
    data = np.array([duration, protocol_map[protocol], src, dst]).reshape(1,-1)
    result = model.predict(data)[0]

    if result == 0:
        st.success("✅ Normal Traffic")
    elif result == 1:
        st.error("🚨 DoS Attack")
    else:
        st.warning("⚠️ Port Scan")

# Graph
st.subheader("📊 Network Traffic")

traffic = [random.randint(10,100) for _ in range(10)]

plt.plot(traffic)
plt.title("Traffic Trend")
st.pyplot(plt)

st.write("Input Data:", data)

prob = model.predict_proba(data)
st.write("Prediction Confidence:", prob)