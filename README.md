# ⚔️ GhostMesh: AI vs AI Cybersecurity Simulator

## 🚀 Overview
GhostMesh is a real-time AI vs AI cybersecurity simulation platform where an autonomous attacker continuously generates cyber threats, and a defender AI detects and responds using machine learning.

The system demonstrates how modern security systems can adapt to evolving attack patterns in a controlled environment.

---

## 🎯 Problem Statement
Simulate a dynamic cybersecurity environment where:
- Attacks are generated automatically
- A defense system detects anomalies
- Both attacker and defender evolve over time

---

## 🧠 Key Features

- 🤖 **AI vs AI Simulation**
  - Attacker AI generates threats
  - Defender AI detects anomalies

- ⚔️ **Attack Types**
  - Port Scan  
  - Login Flood  
  - Data Exfiltration  
  - DDoS  

- 📊 **Live Dashboard**
  - Real-time attack logs
  - Confidence scores
  - Status (Blocked / Breached)

- 📈 **Trend Graph**
  - Attacker vs Defender performance over time

- 
- 🔁 **Auto Simulation**
  - Runs continuously without manual input

---

## 🏗️ System Architecture
Attacker AI (generator.py)
↓
Feature Data (simulated network activity)
↓
Defender AI (model.py - Isolation Forest)
↓
Decision (Anomaly / Normal)
↓
Flask Backend (app.py)
↓
Frontend Dashboard (HTML + JS)
---

## 🧰 Tech Stack

- **Backend:** Python, Flask  
- **Machine Learning:** Scikit-learn (Isolation Forest)  
- **Frontend:** HTML, JavaScript  
- **Visualization:** Chart.js  

---

## 📂 Project Structure
GhostMesh/
│
├── app.py # Main Flask server
├── generator.py # Attacker AI logic
├── model.py # Defender AI (ML model)
├── requirements.txt # Dependencies
│
├── templates/
│ └── index.html # Frontend UI
│
└── static/
└── script.js # Frontend logic
