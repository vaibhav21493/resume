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
        background: radial-gradient(circle at top left, #2c3e50, #1a252f, #0a0e12);
        color: #F0F2F6;
        font-family: 'Segoe UI', sans-serif;
    }
    .image-container {
        position: relative;
        width: 100%;
        max-width: 1200px;
        height: 300px;
        margin: 24px auto;
        overflow: hidden;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }
    .slider-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .overlay-left, .overlay-right {
        position: absolute;
        top: 0;
        width: 50%;
        height: 100%;
        z-index: 4;
        text-decoration: none;
        background: rgba(0,0,0,0);
    }
    .overlay-left { left: 0; }
    .overlay-right { right: 0; }
    .image-container:hover .overlay-left::after,
    .image-container:hover .overlay-right::after {
        position: absolute;
        font-size: 28px;
        color: rgba(255,255,255,0.75);
        top: 50%;
        transform: translateY(-50%);
        pointer-events: none;
    }
    .image-container:hover .overlay-left::after { content: '❮'; left: 18px; }
    .image-container:hover .overlay-right::after { content: '❯'; right: 18px; }
    .header-text {
        text-align: center;
        font-size: 1.3em;
        font-weight: bold;
        margin-top: 10px;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .profile-pic {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 4px solid #90EE90;
        object-fit: cover;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    .name {
        font-size: 2.5em;
        font-weight: bold;
        color: #90EE90;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 1.2em;
        color: #B0B0B0;
        margin-bottom: 30px;
    }
    .card {
        background-color: rgba(45, 45, 45, 0.9);
        border: 2px solid #90EE90;
        border-radius: 15px;
        padding: 25px;
        max-width: 350px;
        cursor: pointer;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.5);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- IMAGE SLIDER ---
st.markdown(
    f'''
    <div class="image-container">
        <img src="{scenery_url}" class="slider-image" />
        <a class="overlay-left" href="?img={prev_idx}"></a>
        <a class="overlay-right" href="?img={next_idx}"></a>
    </div>
    ''',
    unsafe_allow_html=True,
)
st.session_state.count = idx

# --- WELCOME TEXT ---
current_time = datetime.now().strftime("%I:%M %p")
st.markdown(f"<div class='header-text'>Welcome, Vaibhav — {current_time}</div>", unsafe_allow_html=True)

# --- PROFILE + CARD ---
st.markdown('<div class="container">', unsafe_allow_html=True)

# Profile image from GitHub
profile_image_url = "https://github.com/vaibhav21493/resume/blob/main/profile.jpg?raw=true"
st.markdown(f'<img src="{profile_image_url}" class="profile-pic">', unsafe_allow_html=True)

st.markdown('<div class="name">Vaibhav Murotiya</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">B.Tech in Cyber Physical Systems | MIT Manipal</div>', unsafe_allow_html=True)

# --- Button instead of link ---
if st.button("🚀 Explore My Portfolio"):
    st.session_state.show_portfolio = True
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
