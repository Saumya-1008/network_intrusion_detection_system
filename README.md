# 🚨 Network Intrusion Detection System (NIDS)

A machine-learning based Network Intrusion Detection System that classifies network traffic as **Normal**, **DoS Attack**, or **Port Scan**. It uses a Random Forest classifier, a Streamlit web interface for interactive detection, and Scapy for live packet capture.

## Features

- Classifies traffic into 3 classes: Normal, DoS, Port Scan
- Random Forest model with saved/loaded weights (`model.pkl`)
- Interactive Streamlit dashboard with prediction and confidence scores
- Live packet sniffing using Scapy (foundation for real-time detection)
- Experiments on the NSL-KDD benchmark dataset

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3 |
| ML | scikit-learn (RandomForestClassifier), pandas, numpy |
| UI | Streamlit, matplotlib |
| Packet capture | Scapy |

## Project Structure

```
.
├── app.py              # Streamlit web app (UI + prediction)
├── train_model.py      # Trains the Random Forest and saves model.pkl
├── realtime.py         # Live packet capture with Scapy
├── utils.py            # Helper: loads model.pkl and exposes predict_attack()
├── data/
│   └── intrusion.csv   # Small sample dataset
├── KDDTrain+.txt       # NSL-KDD dataset (used for experiments in app.py)
└── model.pkl           # Generated after running train_model.py
```

## How It Works

```
Dataset → Preprocessing → RandomForest training → model.pkl → Streamlit UI
                                                      ↑
                                         Scapy packet capture (realtime.py)
```

1. **Data**: each record has `duration`, `protocol`, `src_bytes`, `dst_bytes` and a `label`.
2. **Preprocessing**: categorical values are encoded to numbers
   - protocol: `tcp=0, udp=1, icmp=2`
   - label: `normal=0, dos=1, scan=2`
3. **Training**: a Random Forest (an ensemble of decision trees that vote on the class) is fit on the features and saved with `pickle`.
4. **Prediction**: the app takes user input, builds a feature vector and shows the predicted class along with class probabilities (confidence).
5. **Real-time**: `realtime.py` captures packets using Scapy's `sniff()`.

## Dataset

- `data/intrusion.csv`: a tiny sample (columns: `duration, protocol, src_bytes, dst_bytes, label`) used for the demo model.
- **NSL-KDD**: standard IDS benchmark with 41 features per connection plus a label and a difficulty score. Attacks fall into four families: DoS, Probe, R2L, U2R.

## Installation

```bash
git clone <your-repo-url>
cd <project-folder>
pip install pandas numpy scikit-learn streamlit matplotlib scapy
```

> Packet capture with Scapy usually needs administrator/root privileges (and Npcap on Windows).

## Usage

**1. Train the model**
```bash
python train_model.py
```
This creates `model.pkl`.

**2. Run the web app**
```bash
streamlit run app.py
```
Enter duration, protocol, source bytes and destination bytes, then click **Detect**.

**3. Capture live packets**
```python
from realtime import start_sniffing
start_sniffing()   # captures 10 packets and prints a summary of each
```

## Known Limitations

- The sample `intrusion.csv` has only a handful of rows, so its accuracy is not meaningful.
- The UI uses only 4 features, while NSL-KDD provides 41.
- `app.py` currently trains a model on NSL-KDD and then retrains on a small hardcoded array, so the UI predicts with the small model.
- `train_test_split` has no fixed `random_state`, so results vary between runs.
- Encoders/scaler are not saved, so preprocessing at prediction time is not guaranteed to match training.
- `realtime.py` only prints packets; it does not yet feed them to the model.
- Only accuracy is reported; no precision/recall/F1 or confusion matrix yet.

## Future Improvements

- Train on all 41 NSL-KDD features and save a full `sklearn` Pipeline (encoders + scaler + model) with `joblib`
- Evaluate with precision, recall, F1-score and a confusion matrix; handle class imbalance
- Extract features from live packets and classify them in real time
- Multi-class detection of specific attack families (DoS, Probe, R2L, U2R)
- Alerting and logging of detected intrusions
- Compare against other models (XGBoost, SVM, neural networks)

## Author

**Saumya**: B.Tech CSE, UIT RGPV Bhopal. Technical lead on this project.
