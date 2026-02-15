# Predictive Maintenance ML 🛠️

A machine learning pipeline that analyzes historical industrial log files to predict equipment failure before it occurs using anomaly detection.

## Description
A machine learning pipeline that analyzes historical industrial log files to predict equipment failure before it occurs using anomaly detection and time-series forecasting.

## Key Features
- **Failure Forecasting:** Predicts Remaining Useful Life (RUL) of industrial assets.
- **Anomaly Detection:** Identifies "out-of-spec" vibrations or temperatures in machine logs.
- **Maintenance Scheduler:** Automatically generates service tickets based on ML risk scores.

## Tech Stack
- **Language:** Python
- **Libraries:** TensorFlow/Keras, Scikit-Learn, Pandas, Plotly
- **Model:** LSTM (Long Short-Term Memory) Neural Network for time-series data.

## Engineering Logic
- **Backend:** The engine processes multi-variate sensor logs (Pressure, Heat, Vibration) and uses an LSTM model to recognize the sequential patterns that precede a breakdown.
- **Software Engine:** A Streamlit dashboard visualizes the "Health Index" of multiple factory assets, highlighting machines that require immediate inspection.
