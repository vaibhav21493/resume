import streamlit as st
from datetime import datetime
from Mainportfolio import main_portfolio

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Vaibhav Murotiya - Portfolio",
    page_icon="✨",
    layout="wide"
)

# --- Check if portfolio page should be shown ---
if "show_portfolio" not in st.session_state:
    st.session_state.show_portfolio = False

if st.session_state.show_portfolio:
    main_portfolio()
    st.stop()

# --- IMAGES ---
scenery_images = [
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=1600",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1600",
    "https://images.unsplash.com/photo-1501973801540-537f08ccae7b?w=1600",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600"
]
n = len(scenery_images)

qp = st.query_params
if "img" in qp:
    try:
        idx = int(qp["img"]) % n
    except Exception:
        idx = 0
    st.session_state.count = idx
else:
    if "count" not in st.session_state:
        st.session_state.count = 0
    idx = st.session_state.count % n

prev_idx = (idx - 1) % n
next_idx = (idx + 1) % n
scenery_url = scenery_images[idx]

# --- CSS ---
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #2c3e50, #1a252f, #0a0e12
