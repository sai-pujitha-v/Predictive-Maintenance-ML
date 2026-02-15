import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import random

st.set_page_config(page_title="FactoryBrain AI", layout="wide", page_icon="🛠️")

st.markdown("""
    <style>
    .main { background-color: #1a1c24; color: #ffffff; }
    .stMetric { background-color: #262932; border: 1px solid #4a4e5a; border-radius: 10px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

if 'machine_data' not in st.session_state:
    st.session_state.machine_data = pd.DataFrame(columns=['Time', 'Vibration', 'Temperature', 'Failure_Risk'])

st.title("🛠️ FactoryBrain AI | Predictive Maintenance Hub")
st.write("Industrial Asset Monitoring & Machine Learning Diagnostics")

col_metrics, col_chart = st.columns([1, 2])

# Sidebar machine selection
asset_id = st.sidebar.selectbox("Select Asset", ["Turbine-01", "Conveyor-A4", "CNC-Lathe-09"])

placeholder = st.empty()

for i in range(100):
    # Simulated sensor noise
    vibration = 45.0 + (np.sin(i/5) * 5) + random.uniform(-1, 1)
    temp = 75.0 + random.uniform(-2, 2)
    
    # Logic: Risk spikes if vibration crosses 52Hz
    risk = (vibration - 40) * 8 if vibration > 50 else random.randint(5, 15)
    
    new_data = {
        'Time': datetime.now().strftime("%H:%M:%S"),
        'Vibration': round(vibration, 2),
        'Temperature': round(temp, 2),
        'Failure_Risk': round(min(risk, 100), 1)
    }
    
    st.session_state.machine_data = pd.concat([pd.DataFrame([new_data]), st.session_state.machine_data]).head(30)
    
    with placeholder.container():
        m1, m2, m3 = st.columns(3)
        m1.metric("Vibration (Hz)", f"{vibration:.2f}", delta="Normal" if vibration < 50 else "High", delta_color="inverse")
        m2.metric("Temp (°C)", f"{temp:.1f}")
        m3.metric("Failure Risk", f"{new_data['Failure_Risk']}%", delta=f"{random.randint(-2, 5)}%")

        if new_data['Failure_Risk'] > 75:
            st.error(f"🚨 CRITICAL WARNING: {asset_id} shows high mechanical stress. Schedule maintenance immediately.")

        # Real-time Trend Graph
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=st.session_state.machine_data['Time'], y=st.session_state.machine_data['Vibration'], name="Vibration Trend"))
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Diagnostic Log")
        st.table(st.session_state.machine_data.head(5))

    time.sleep(2)
