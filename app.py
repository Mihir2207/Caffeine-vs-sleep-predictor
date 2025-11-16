# app.py
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(
    page_title="Caffeine → Sleep Quality ",
    layout="centered",
)

# --- Color Palette ---
PRIMARY = "#e23636"    # Red accent
BG_DARK = "#000000"    # Background
TEXT_LIGHT = "#f1f1f1"
GRAY = "#504a4a"
BLUE = "#518cca"
ORANGE = "#f78f3f"

# --- Custom CSS ---
st.markdown(f"""
<style>
body {{
    background-color: {BG_DARK};
    color: {TEXT_LIGHT};
    font-family: 'Segoe UI', sans-serif;
}}
h1, h2, h3, h4 {{
    color: {PRIMARY};
    text-align: center;
}}
p, label {{
    color: {TEXT_LIGHT};
}}
hr {{
    border: 1px solid {GRAY};
    margin: 1rem 0;
}}
.stButton>button {{
    background: linear-gradient(90deg, {PRIMARY}, {ORANGE});
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.3rem;
    font-weight: 600;
    font-size: 1rem;
    transition: 0.3s;
}}
.stButton>button:hover {{
    background: linear-gradient(90deg, {BLUE}, {ORANGE});
    transform: scale(1.05);
}}
div[data-testid="stNumberInput"] label {{
    color: {BLUE} !important;
    font-weight: 600;
}}
.codeblock {{
    background: {GRAY};
    color: {ORANGE};
    padding: 0.6rem;
    border-radius: 6px;
    font-family: monospace;
    font-size: 0.9rem;
}}
.block-container {{
    padding-top: 2rem;
}}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown(f"<h1>Predict Sleep Quality on Caffeine intake</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:{BLUE};'>Predict your sleep quality score (0–10) based on caffeine intake per day.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Load Model ---
with open("sleep_model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Input ---
caffeine = st.number_input(
    "Enter caffeine intake (mg):",
    min_value=0.0,
    max_value=1000.0,
    value=150.0,
    step=10.0,
    help="Includes coffee, tea, soft drinks, and energy drinks.",
)

# --- Prediction ---
if st.button("🔍 Predict Sleep Quality"):
    pred = model.predict(np.array([[caffeine]]))[0]
    pred = max(0, min(10, pred))
    
    st.markdown(f"<h3 style='color:{ORANGE};text-align:center;'>Predicted Sleep Quality: {pred:.2f} / 10</h3>", unsafe_allow_html=True)

    # Model Equation
    m = model.coef_[0]
    b = model.intercept_
    st.markdown(f"<h4 style='color:{BLUE};'>Model Equation:</h4>", unsafe_allow_html=True)
    st.markdown(f"<div class='codeblock'>Sleep_Quality = {m:.4f} × Caffeine_mg + {b:.4f}</div>", unsafe_allow_html=True)
    
    # Chart
    df = pd.read_csv("caffeine_sleep.csv")
    df = df.rename(columns={"Caffeine_mg": "x", "Sleep_Quality": "y"}).set_index("x")
    st.line_chart(df["y"])

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:{GRAY};font-size:13px;'>Built with ❤️ by Mihir</p>", unsafe_allow_html=True)
