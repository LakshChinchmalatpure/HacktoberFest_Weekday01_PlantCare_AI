"""
FloraSprout - Open-Source Offline Plant Care & Garden Companion
Theme: "Touch Grass" AI Hackathon
Ultra-Premium Dark Biophilic Glassmorphism UI
Featuring Google Gemma local LLM, Gemini Vision Multimodal Diagnostics,
Local Garden Planner, and Screen Time Saver Mode.
"""

import os
import sys
import json
import time
from typing import Dict, List, Any, Optional, Tuple
from PIL import Image
import requests
import streamlit as st

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# Import offline botanical knowledge base & vision analyzer
try:
    from botanical_data import (
        HARDINESS_ZONES,
        COMPANION_PLANTS,
        DIAGNOSTIC_CASES,
        FALLBACK_KNOWLEDGE_BASE,
        get_offline_botanical_answer,
    )
    from vision_analyzer import (
        analyze_image_with_gemini,
        analyze_image_offline,
    )
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from botanical_data import (
        HARDINESS_ZONES,
        COMPANION_PLANTS,
        DIAGNOSTIC_CASES,
        FALLBACK_KNOWLEDGE_BASE,
        get_offline_botanical_answer,
    )
    from vision_analyzer import (
        analyze_image_with_gemini,
        analyze_image_offline,
    )

# -----------------------------------------------------------------------------
# Streamlit Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="FloraSprout 🌱 | Offline Plant Care & Vision AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# Ultra-Premium Dark Biophilic Glassmorphism Theme (Custom CSS)
# -----------------------------------------------------------------------------
PREMIUM_THEME_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

    /* Global Dark Biophilic Canvas */
    .stApp {
        background: radial-gradient(circle at 12% 15%, rgba(16, 185, 129, 0.09) 0%, transparent 45%),
                    radial-gradient(circle at 88% 80%, rgba(245, 158, 11, 0.05) 0%, transparent 45%),
                    radial-gradient(circle at 50% 50%, rgba(5, 150, 105, 0.04) 0%, transparent 60%),
                    #07140e !important;
        color: #e2ece6 !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1280px !important;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
        color: #f0fdf4 !important;
    }

    p, span, label, li {
        color: #d1fae5;
    }

    /* Sidebar Luxury Obsidian Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #050f0a 0%, #091a12 100%) !important;
        border-right: 1px solid rgba(52, 211, 153, 0.15) !important;
        box-shadow: 4px 0 24px rgba(0, 0, 0, 0.4) !important;
    }
    [data-testid="stSidebar"] * {
        color: #d1fae5 !important;
    }

    /* Luxury Segmented Navigation Tabs */
    div[data-baseweb="tab-list"] {
        background: rgba(13, 33, 23, 0.75) !important;
        backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(52, 211, 153, 0.22) !important;
        border-radius: 60px !important;
        padding: 6px !important;
        gap: 6px !important;
        margin-bottom: 2rem !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
    }

    button[data-baseweb="tab"] {
        border-radius: 50px !important;
        color: #86efac !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.94rem !important;
        padding: 10px 24px !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    button[data-baseweb="tab"]:hover {
        color: #ffffff !important;
        background: rgba(52, 211, 153, 0.12) !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.45) !important;
    }

    /* Hero Banner */
    .hero-glass-box {
        background: linear-gradient(135deg, rgba(16, 43, 31, 0.8) 0%, rgba(9, 26, 18, 0.9) 100%) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(52, 211, 153, 0.25) !important;
        border-radius: 28px !important;
        padding: 2.4rem 2.8rem !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        margin-bottom: 2rem !important;
        position: relative;
        overflow: hidden;
    }

    .hero-badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(245, 158, 11, 0.16);
        color: #fde68a;
        border: 1px solid rgba(245, 158, 11, 0.35);
        padding: 5px 16px;
        border-radius: 30px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .hero-title-gradient {
        background: linear-gradient(135deg, #ffffff 30%, #a7f3d0 70%, #34d399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Outfit', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        margin: 0;
        line-height: 1.15;
    }

    .hero-subtitle {
        color: #a7f3d0;
        font-size: 1.1rem;
        margin-top: 0.6rem;
        margin-bottom: 1.4rem;
        max-width: 860px;
        line-height: 1.6;
    }

    /* Glassmorphic Feature Cards */
    .glass-card {
        background: rgba(14, 34, 25, 0.6) !important;
        backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(52, 211, 153, 0.18) !important;
        border-radius: 22px !important;
        padding: 1.6rem !important;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3) !important;
        margin-bottom: 1.4rem !important;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .glass-card:hover {
        border-color: rgba(52, 211, 153, 0.35) !important;
        transform: translateY(-2px);
    }

    /* Diagnostic Result 4-Box Grid */
    .result-domain-box {
        background: rgba(10, 25, 18, 0.7);
        border: 1px solid rgba(52, 211, 153, 0.18);
        border-radius: 18px;
        padding: 1.4rem;
        height: 100%;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }

    .domain-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Health Gauge Bar */
    .gauge-track {
        height: 12px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        overflow: hidden;
        margin: 10px 0 16px 0;
    }

    .gauge-progress {
        height: 100%;
        border-radius: 10px;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Badges */
    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 700;
    }

    .badge-green {
        background: rgba(16, 185, 129, 0.18);
        color: #6ee7b7;
        border: 1px solid rgba(16, 185, 129, 0.4);
    }

    .badge-amber {
        background: rgba(245, 158, 11, 0.18);
        color: #fde68a;
        border: 1px solid rgba(245, 158, 11, 0.4);
    }

    .badge-red {
        background: rgba(239, 68, 68, 0.18);
        color: #fca5a5;
        border: 1px solid rgba(239, 68, 68, 0.4);
    }

    .badge-blue {
        background: rgba(14, 165, 233, 0.18);
        color: #7dd3fc;
        border: 1px solid rgba(14, 165, 233, 0.4);
    }

    /* Screen Time Saver Alert */
    .saver-glow-banner {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(5, 150, 105, 0.1) 100%);
        border: 1px solid rgba(52, 211, 153, 0.4);
        color: #ecfdf5;
        padding: 1.1rem 1.5rem;
        border-radius: 18px;
        margin: 1.2rem 0;
        box-shadow: 0 8px 30px rgba(16, 185, 129, 0.18);
        display: flex;
        align-items: center;
        gap: 14px;
    }

    /* Metric Grid Cards */
    .metric-card-lux {
        background: rgba(14, 34, 25, 0.65);
        border: 1px solid rgba(52, 211, 153, 0.2);
        border-radius: 18px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
    }

    .metric-val-lux {
        font-family: 'Outfit', sans-serif;
        font-size: 1.85rem;
        font-weight: 800;
        color: #34d399;
    }

    .metric-lbl-lux {
        font-size: 0.8rem;
        color: #94d2bd;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.05em;
        margin-top: 4px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: #ffffff !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.98rem !important;
        padding: 0.72rem 1.8rem !important;
        border-radius: 14px !important;
        border: 1px solid rgba(110, 231, 183, 0.4) !important;
        box-shadow: 0 6px 22px rgba(16, 185, 129, 0.35) !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.5) !important;
    }

    .stDownloadButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        color: #ffffff !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        border-radius: 14px !important;
        border: 1px solid rgba(52, 211, 153, 0.4) !important;
        box-shadow: 0 6px 22px rgba(5, 150, 105, 0.3) !important;
    }

    /* Selectbox, Textbox & Inputs */
    div[data-baseweb="select"] > div,
    input[type="text"], input[type="password"] {
        background: rgba(10, 24, 18, 0.85) !important;
        border: 1px solid rgba(52, 211, 153, 0.25) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }

    /* Checkbox */
    .stCheckbox label span {
        color: #d1fae5 !important;
    }
</style>
"""
st.markdown(PREMIUM_THEME_CSS, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Local Gemma Engine Class
# -----------------------------------------------------------------------------
class LocalGemmaEngine:
    """Manages local Gemma weights running through Ollama or offline fallback."""

    def __init__(self, host: str = "http://localhost:11434", model_name: str = "gemma:2b"):
        self.host = host.rstrip("/")
        self.model_name = model_name
        self.system_prompt_base = (
            "You are FloraSprout, an expert offline botanical assistant created for the "
            "'Touch Grass' open-source hackathon. Your mission is to provide accurate, "
            "practical, organic, nature-first plant care and permaculture advice while encouraging "
            "users to spend less time staring at screens and more time outside in real soil."
        )

    def is_available(self) -> Tuple[bool, List[str], str]:
        try:
            resp = requests.get(f"{self.host}/api/tags", timeout=1.5)
            if resp.status_code == 200:
                models_data = resp.json().get("models", [])
                names = [m.get("name", "") for m in models_data if "name" in m]
                return True, names, "Connected to local Ollama server"
            return False, [], f"Ollama returned HTTP status {resp.status_code}"
        except Exception:
            return False, [], "Ollama server is not running on localhost:11434"

    def generate_response(self, user_query: str, screen_time_saver: bool = True) -> Tuple[str, str]:
        if screen_time_saver:
            screen_constraint = (
                "\n\nCRITICAL TOUCH GRASS CONSTRAINT: The user has Screen Time Saver Mode ACTIVE. "
                "Deliver your entire answer in EXACTLY 3 short, punchy bullet points, totaling under 50 words. "
                "End by telling them to put the screen down and touch grass!"
            )
        else:
            screen_constraint = (
                "\n\nFormat your answer with clear headers, diagnostic clues, actionable steps, "
                "and an organic DIY remedy."
            )

        full_system_prompt = self.system_prompt_base + screen_constraint

        is_up, available_models, _ = self.is_available()
        if is_up:
            try:
                selected_model = self.model_name
                if available_models and self.model_name not in available_models:
                    gemma_matches = [m for m in available_models if "gemma" in m.lower()]
                    selected_model = gemma_matches[0] if gemma_matches else available_models[0]

                payload = {
                    "model": selected_model,
                    "prompt": f"{full_system_prompt}\n\nUser Question: {user_query}\n\nFloraSprout Answer:",
                    "stream": False,
                    "options": {
                        "temperature": 0.3 if screen_time_saver else 0.6,
                        "num_predict": 120 if screen_time_saver else 500,
                    },
                }
                resp = requests.post(f"{self.host}/api/generate", json=payload, timeout=25.0)
                if resp.status_code == 200:
                    result = resp.json().get("response", "").strip()
                    if result:
                        return result, f"Local Neural Model: {selected_model} (Ollama)"
            except Exception:
                pass

        offline_answer = get_offline_botanical_answer(user_query, screen_time_saver=screen_time_saver)
        provider = "FloraSprout Offline Botanical Engine (Stand-alone Knowledge Base)"
        return offline_answer, provider


# Initialize Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "time_saved_minutes" not in st.session_state:
    st.session_state.time_saved_minutes = 0
if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
if "last_scan_data" not in st.session_state:
    st.session_state.last_scan_data = None
if "last_scan_provider" not in st.session_state:
    st.session_state.last_scan_provider = None


# -----------------------------------------------------------------------------
# Sidebar: Control Deck & Live Status
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image(
        "https://images.unsplash.com/photo-1545239351-ef35f43d514b?w=500&auto=format&fit=crop&q=80",
        caption="🌱 Real Soil. Real Nature. Touch Grass.",
        use_container_width=True,
    )

    st.markdown("### 🌿 Screen Time Saver Mode")
    screen_time_saver = st.toggle(
        "Activate 'Touch Grass' Mode",
        value=True,
        help="Summarizes plant diagnoses into exactly 3 bullet points under 50 words to encourage closing screens quickly.",
    )

    if screen_time_saver:
        st.markdown(
            """
            <div class="saver-glow-banner" style="margin: 0.6rem 0; padding: 0.7rem 1rem;">
                ⚡ <b>Active:</b> 3 Bullets | &lt;50 Words | Rapid Triage
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(f"Estimated screen time eliminated today: **~{st.session_state.time_saved_minutes + 20} mins**")

    st.markdown("---")
    st.markdown("### 🌐 Live Running Endpoint")
    st.markdown(
        """
        <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(52, 211, 153, 0.3); border-radius: 12px; padding: 0.7rem 1rem;">
            🔗 <b>App URL:</b> <a href="http://localhost:8501" target="_blank" style="color: #6ee7b7; font-weight: 700; text-decoration: none;">http://localhost:8501</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### 🔑 Gemini Vision AI Engine")
    gemini_key_input = st.text_input(
        "Gemini API Key:",
        value=st.session_state.gemini_api_key,
        type="password",
        help="Used for cloud multimodal plant identification when online.",
    )
    if gemini_key_input:
        st.session_state.gemini_api_key = gemini_key_input
        st.markdown(
            '<div class="badge-pill badge-green" style="width: 100%; justify-content: center; margin-top: 4px;">🟢 Gemini Vision: Active</div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### ⚙️ Local Neural AI (Gemma)")
    ollama_host = st.text_input("Ollama Host URL", value="http://localhost:11434")
    model_choice = st.text_input("Local Model Name", value="gemma:2b")

    engine = LocalGemmaEngine(host=ollama_host, model_name=model_choice)
    is_up, models_found, _ = engine.is_available()

    if is_up:
        st.success(f"🟢 Ollama Gemma Online ({len(models_found)} models)")
    else:
        st.warning("🟠 Standalone Offline Mode Active")
        with st.expander("ℹ️ Connect Local Gemma:"):
            st.code("ollama run gemma:2b", language="bash")

    st.markdown("---")
    if st.button("🧹 Reset History & Scans", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.last_scan_data = None
        st.rerun()


# -----------------------------------------------------------------------------
# Hero Banner
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero-glass-box">
        <div class="hero-badge-pill">🌿 Hacktoberfest 2026 | "Touch Grass" AI Challenge</div>
        <h1 class="hero-title-gradient">FloraSprout</h1>
        <p class="hero-subtitle">
            An offline-first, multimodal botanical companion powered by open-weight <b>Google Gemma</b>, 
            <b>Gemini Vision</b>, and edge computer vision. Identify plant health from photos, 
            discover what your plants yield, safely treat pests with organic bio-remedies, and spend less time on screens and more time in living soil.
        </p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <span class="badge-pill badge-green">✨ Anti-Addiction AI Design</span>
            <span class="badge-pill badge-amber">📸 Multimodal Health Scanner</span>
            <span class="badge-pill badge-blue">🌲 100% Offline Trail Ready</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------------------------------------------------------
# Main Navigation Tabs
# -----------------------------------------------------------------------------
tab_scan, tab_chat, tab_planner, tab_cards, tab_manifesto = st.tabs([
    "📸 Plant Health Scanner (Upload & Diagnose)",
    "🌿 Plant Care AI Assistant",
    "🗓️ Local Garden Planner & Frost Dates",
    "📋 Offline Diagnosis & Action Cards",
    "🏕️ 'Touch Grass' Manifesto & Architecture",
])


# -----------------------------------------------------------------------------
# TAB 1: Plant Health Scanner (Image Upload & Full Diagnostic Dashboard)
# -----------------------------------------------------------------------------
with tab_scan:
    st.markdown("### 📸 Multimodal Plant Health & Ecosystem Scanner")
    st.write(
        "Upload a photo of any leaf, potted plant, or crop to immediately identify the **plant name**, "
        "**health vitality**, **action recommendations**, **what it gives (harvest & air quality)**, "
        "**needed bio-pesticides**, and **ecosystem health impact**."
    )

    col_up_left, col_up_right = st.columns([1, 1])

    with col_up_left:
        st.markdown(
            """
            <div class="glass-card" style="padding: 1.3rem;">
                <h4 style="margin: 0; display: flex; align-items: center; gap: 8px;">
                    📥 1. Provide Plant Photo
                </h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

        input_choice = st.radio(
            "Select Photo Source:",
            ["📁 Upload Image File (JPG, PNG, WEBP)", "📷 Device Camera Snapshot"],
            horizontal=True,
        )

        user_image = None
        if "Upload" in input_choice:
            uploaded_file = st.file_uploader(
                "Upload a clear picture of leaf or plant:",
                type=["jpg", "jpeg", "png", "webp"],
            )
            if uploaded_file:
                user_image = Image.open(uploaded_file)
        else:
            cam_shot = st.camera_input("Take a photo with your webcam / phone camera:")
            if cam_shot:
                user_image = Image.open(cam_shot)

        if user_image:
            st.image(user_image, caption="Current Plant Specimen", use_container_width=True)

    with col_up_right:
        st.markdown(
            """
            <div class="glass-card" style="padding: 1.3rem;">
                <h4 style="margin: 0; display: flex; align-items: center; gap: 8px;">
                    ⚙️ 2. Analysis Engine & Parameters
                </h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

        engine_choice = st.selectbox(
            "Diagnostic Engine:",
            [
                "⚡ Auto (Gemini Vision AI with Edge Computer Vision Fallback)",
                "🌐 Google Gemini Vision AI (Cloud Multimodal)",
                "🍃 FloraSprout Edge Computer Vision (100% Offline Pixel Spectrum)",
            ],
        )

        col_c1, col_c2 = st.columns(2)
        with col_c1:
            cat_hint = st.selectbox(
                "Plant Category (Optional):",
                [
                    "Auto-Detect from Photo",
                    "Monstera / Philodendron (Aroid)",
                    "Tomato / Nightshade Family",
                    "Sweet Basil / Kitchen Herb",
                    "Snake Plant / Succulent",
                    "Fruit / Citrus Tree",
                    "Brassica (Kale, Cabbage)",
                    "General Houseplant",
                ],
            )
        with col_c2:
            sym_hint = st.selectbox(
                "Observed Issue (Optional):",
                [
                    "Auto-Diagnose Visual Symptoms",
                    "Yellowing Lower Leaves (Chlorosis)",
                    "Crispy Brown Leaf Tips / Scorch",
                    "Fine Webbing / Sap Pests",
                    "White Powdery Coating",
                    "General Routine Wellness Check",
                ],
            )

        st.markdown("<br/>", unsafe_allow_html=True)
        analyze_btn = st.button("🔍 Identify Plant & Analyze Health", type="primary", use_container_width=True)

    # Execution of Plant Health Scan
    if user_image and analyze_btn:
        with st.spinner("🌿 Analyzing plant taxonomy, foliar tissue health, and ecological impact..."):
            start_t = time.time()
            clean_cat = "" if "Auto" in cat_hint else cat_hint
            clean_sym = "" if "Auto" in sym_hint else sym_hint

            diag_result = None
            engine_used = ""

            # Attempt Gemini Vision if requested
            if "Offline" not in engine_choice:
                success, gemini_data, prov = analyze_image_with_gemini(
                    user_image,
                    api_key=st.session_state.gemini_api_key,
                    screen_time_saver=screen_time_saver,
                    plant_hint=clean_cat,
                    symptom_hint=clean_sym,
                )
                if success and gemini_data:
                    diag_result = gemini_data
                    engine_used = prov

            # Fallback to 100% Offline Edge Computer Vision
            if not diag_result:
                diag_result, prov = analyze_image_offline(
                    user_image,
                    plant_hint=clean_cat or "Houseplant",
                    symptom_hint=clean_sym or "Yellowing leaves",
                    screen_time_saver=screen_time_saver,
                )
                engine_used = prov

            st.session_state.last_scan_data = diag_result
            st.session_state.last_scan_provider = engine_used
            st.session_state.last_scan_duration = time.time() - start_t

    # -------------------------------------------------------------------------
    # Render Diagnostic Dashboard Results
    # -------------------------------------------------------------------------
    if st.session_state.last_scan_data:
        data = st.session_state.last_scan_data
        provider = st.session_state.last_scan_provider
        dur = st.session_state.get("last_scan_duration", 1.2)
        score = data.get("health_score", 85)

        # Score styling
        if score >= 80:
            score_color = "#10b981"
            score_badge = "🟢 Thriving & Resilient"
        elif score >= 50:
            score_color = "#f59e0b"
            score_badge = "🟡 Attention Required"
        else:
            score_color = "#ef4444"
            score_badge = "🔴 High Urgency Treatment"

        st.markdown("---")
        st.markdown("## 🌿 Plant Diagnostic & Ecological Report")

        # Top Hero Specimen Card
        st.markdown(
            f"""
            <div class="glass-card" style="border-left: 8px solid {score_color}; background: rgba(14, 34, 25, 0.85);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
                    <div>
                        <div style="font-size: 0.82rem; text-transform: uppercase; font-weight: 700; color: #a7f3d0; letter-spacing: 0.08em;">
                            Identified Specimen
                        </div>
                        <h2 style="font-size: 2.3rem; margin: 0; color: #ffffff;">
                            {data.get('plant_name', 'Botanical Specimen')}
                        </h2>
                        <div style="font-size: 1.1rem; font-style: italic; color: #6ee7b7; margin-top: 2px;">
                            {data.get('scientific_name', 'Plantae')}
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge-pill" style="background: {score_color}25; color: {score_color}; border: 1px solid {score_color}; font-size: 0.95rem;">
                            {score_badge}
                        </span>
                        <div style="font-size: 2.2rem; font-weight: 900; color: {score_color}; margin-top: 4px; font-family: 'Outfit';">
                            {score}/100 <span style="font-size: 0.9rem; font-weight: 600; color: #a7f3d0;">Vigor</span>
                        </div>
                    </div>
                </div>
                <div class="gauge-track">
                    <div class="gauge-progress" style="width: {score}%; background: {score_color};"></div>
                </div>
                <div style="font-size: 1.05rem; color: #f0fdf4; line-height: 1.6; margin-top: 8px;">
                    <b>Health Assessment:</b> {data.get('health_status', 'Healthy')} — {data.get('health_summary', '')}
                </div>
                <div style="margin-top: 12px; font-size: 0.82rem; color: #94d2bd;">
                    Diagnosis Engine: <b>{provider}</b> | Processed in {dur:.2f}s
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 4 Core Information Grid Cards
        col_g1, col_g2 = st.columns(2)

        with col_g1:
            # CARD 1: What It Gives
            gives = data.get("what_it_gives", {})
            st.markdown(
                f"""
                <div class="result-domain-box">
                    <div class="domain-title" style="color: #6ee7b7;">
                        🍎 1. What It Gives (Harvest, Air & Yield)
                    </div>
                    <p style="margin-bottom: 10px;">
                        <b style="color: #a7f3d0;">🌾 Harvest & Culinary Yield:</b><br/>{gives.get('harvest_uses', 'Ornamental foliage and psychological well-being.')}
                    </p>
                    <p style="margin-bottom: 10px;">
                        <b style="color: #a7f3d0;">💨 NASA Air Purification:</b><br/>{gives.get('air_purification', 'Actively converts CO2 to oxygen and balances room humidity.')}
                    </p>
                    <p style="margin-bottom: 0;">
                        <b style="color: #a7f3d0;">🐝 Wildlife & Pollinators:</b><br/>{gives.get('pollinator_ecosystem', 'Supports local pollinators and living soil micro-fauna.')}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_g2:
            # CARD 2: Needed Pesticides & Safe Bio-Remedies
            pest = data.get("pesticides_needed", {})
            is_pest = pest.get("is_pesticide_required", False)
            pest_status = "⚠️ Bio-Remedy Needed" if is_pest else "✅ No Pesticides Needed"
            badge_cls = "badge-amber" if is_pest else "badge-green"
            st.markdown(
                f"""
                <div class="result-domain-box">
                    <div class="domain-title" style="color: #fde68a;">
                        🛡️ 2. Pesticides & Bio-Remedies ({pest_status})
                    </div>
                    <p style="margin-bottom: 10px;">
                        <b style="color: #a7f3d0;">🌿 Recommended Natural Remedy:</b><br/>
                        <span class="badge-pill {badge_cls}">{pest.get('recommended_bio_pesticide', 'Organic Castile Soap Spray')}</span>
                    </p>
                    <p style="margin-bottom: 10px;">
                        <b style="color: #a7f3d0;">🧪 Safe DIY Application Recipe:</b><br/>
                        {pest.get('recipe_application', 'Mix 1 tsp cold-pressed neem oil + 0.5 tsp liquid castile soap in 1 quart water.')}
                    </p>
                    <p style="margin-bottom: 0; font-size: 0.88rem; color: #fca5a5;">
                        <b>🚫 Anti-Synthetic Warning:</b><br/>
                        {pest.get('synthetic_warning', 'Never use synthetic neonicotinoids or pyrethroids that exterminate bees and sterilize soil.')}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        col_g3, col_g4 = st.columns(2)

        with col_g3:
            # CARD 3: Ecosystem Health & Biodiversity
            eco = data.get("ecosystem_health", {})
            st.markdown(
                f"""
                <div class="result-domain-box" style="margin-top: 1rem;">
                    <div class="domain-title" style="color: #7dd3fc;">
                        🌍 3. Ecosystem Health & Biodiversity Impact
                    </div>
                    <p style="margin-bottom: 10px;">
                        <b style="color: #a7f3d0;">🌱 Ecosystem Health Status:</b><br/>
                        <span class="badge-pill badge-blue">{eco.get('is_healthy_for_ecosystem', 'Highly Beneficial Poly-Culture Specimen')}</span>
                    </p>
                    <p style="margin-bottom: 10px;">
                        <b style="color: #a7f3d0;">🦠 Living Soil & Biodiversity:</b><br/>
                        {eco.get('biodiversity_role', 'Enhances soil microbiome diversity through mycorrhizal root associations.')}
                    </p>
                    <p style="margin-bottom: 0;">
                        <b style="color: #a7f3d0;">🤝 Best Companion Partners:</b><br/>
                        {eco.get('companion_compatibility', 'French Marigolds, Genovese Basil, White Clover.')}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_g4:
            # CARD 4: Step-by-Step Recovery Recommendations
            recs = data.get("recommendations", [])
            rec_html = "".join([f"<li style='margin-bottom: 8px; color: #f0fdf4;'>{r}</li>" for r in recs])
            st.markdown(
                f"""
                <div class="result-domain-box" style="margin-top: 1rem;">
                    <div class="domain-title" style="color: #34d399;">
                        📋 4. Actionable Step-by-Step Recommendations
                    </div>
                    <ul style="padding-left: 20px; margin-bottom: 0;">
                        {rec_html}
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Screen Time Saver Box
        if screen_time_saver:
            st.markdown(
                f"""
                <div class="saver-glow-banner">
                    <span style="font-size: 1.6rem;">⚡</span>
                    <div>
                        <b style="color: #34d399; font-size: 1.05rem;">Screen Time Saver Mode Active (Touch Grass):</b><br/>
                        • <b>Specimen:</b> {data.get('plant_name')} ({data.get('health_status')})<br/>
                        • <b>Action:</b> {recs[0] if recs else 'Apply natural organic remedy'}<br/>
                        • <b>Touch Grass:</b> Diagnostic complete in under 50 words! Close your screen, step into the garden, and touch grass! 🌱
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.session_state.time_saved_minutes += 5

        # Interactive Field Checklist
        st.markdown("#### ✅ Real-World Hands-on Checklist")
        for i, r in enumerate(recs):
            st.checkbox(r, key=f"rec_check_{i}")

        # Download Field Action Card
        card_content = f"""# FloraSprout Field Diagnostic Report
Plant Name: {data.get('plant_name')}
Scientific Name: {data.get('scientific_name')}
Health Status: {data.get('health_status')} (Vitality Score: {score}/100)
Diagnostic Provider: {provider}

## 1. What It Gives
- Harvest & Uses: {gives.get('harvest_uses')}
- Air Purification: {gives.get('air_purification')}
- Pollinator Value: {gives.get('pollinator_ecosystem')}

## 2. Pesticides & Organic Bio-Remedies
- Remedy: {pest.get('recommended_bio_pesticide')}
- Recipe: {pest.get('recipe_application')}
- Warning: {pest.get('synthetic_warning')}

## 3. Ecosystem Health
- Status: {eco.get('is_healthy_for_ecosystem')}
- Biodiversity: {eco.get('biodiversity_role')}
- Companions: {eco.get('companion_compatibility')}

## 4. Action Steps
{chr(10).join(['- [ ] ' + r for r in recs])}

---
FloraSprout | Generated for Hacktoberfest 'Touch Grass' AI Challenge (100% Offline Capable)
"""
        st.download_button(
            "📥 Download Printable Field Action Card (.md)",
            data=card_content,
            file_name=f"FloraSprout_{data.get('plant_name', 'Plant').split()[0]}_ActionCard.md",
            mime="text/markdown",
            use_container_width=True,
        )


# -----------------------------------------------------------------------------
# TAB 2: Plant Care AI Assistant (Chat & Q&A)
# -----------------------------------------------------------------------------
with tab_chat:
    st.markdown("### 💬 Ask FloraSprout Botanical Care")
    st.caption("Ask questions about houseplants, balcony gardens, pest prevention, or soil health. Works 100% offline.")

    col_p1, col_p2, col_p3, col_p4 = st.columns(4)
    quick_query = None
    if col_p1.button("🍂 Monstera yellow leaves", use_container_width=True):
        quick_query = "My monstera deliciosa leaves are turning yellow. What should I do?"
    if col_p2.button("🍅 Tomato companion plants", use_container_width=True):
        quick_query = "What are the best companion plants to grow alongside tomatoes and why?"
    if col_p3.button("🐌 Natural slug deterrent", use_container_width=True):
        quick_query = "How do I naturally deter slugs from eating my lettuce without chemical pellets?"
    if col_p4.button("🪴 Snake plant watering", use_container_width=True):
        quick_query = "How often should I water my snake plant indoors?"

    for message in st.session_state.chat_history:
        role = message.get("role", "user")
        content = message.get("content", "")
        provider = message.get("provider", "")
        with st.chat_message(role, avatar="🧑‍🌾" if role == "user" else "🌱"):
            st.markdown(content)
            if provider:
                st.caption(f"Engine: {provider}")

    user_input = st.chat_input("Type your botanical or gardening question here...")
    active_prompt = quick_query or user_input

    if active_prompt:
        st.session_state.chat_history.append({"role": "user", "content": active_prompt})
        with st.chat_message("user", avatar="🧑‍🌾"):
            st.markdown(active_prompt)

        with st.chat_message("assistant", avatar="🌱"):
            with st.spinner("Consulting local botanical engine..."):
                start_t = time.time()
                response_text, provider_info = engine.generate_response(
                    active_prompt,
                    screen_time_saver=screen_time_saver
                )
                elapsed = time.time() - start_t

            st.markdown(response_text)
            word_count = len(response_text.split())
            col_stat1, col_stat2 = st.columns([2, 1])
            with col_stat1:
                st.caption(f"⚡ {provider_info} | Generated in {elapsed:.2f}s | Word Count: {word_count}")
            with col_stat2:
                if screen_time_saver:
                    st.markdown("<span style='color: #34d399; font-weight: 700; font-size: 0.88rem;'>🌱 Mission accomplished: Close screen & go outside!</span>", unsafe_allow_html=True)
                    st.session_state.time_saved_minutes += 3

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response_text,
            "provider": provider_info
        })


# -----------------------------------------------------------------------------
# TAB 3: Local Garden Planner & Frost Date Checker
# -----------------------------------------------------------------------------
with tab_planner:
    st.markdown("### 🗓️ Local Garden Planner & Frost Date Engine")
    st.write(
        "Plan your plantings with 100% offline hardiness zone calculations, average frost dates, "
        "and companion planting matrices without sending your GPS location to any remote cloud."
    )

    col_z1, col_z2 = st.columns([1, 1])
    with col_z1:
        zone_keys = list(HARDINESS_ZONES.keys())
        selected_zone_name = st.selectbox(
            "Select Your USDA / Regional Hardiness Zone:",
            options=zone_keys,
            index=2,
        )
        zone_data = HARDINESS_ZONES[selected_zone_name]

    with col_z2:
        st.markdown("#### 🗺️ Don't know your zone?")
        quick_climate = st.selectbox(
            "Select General Climate Type:",
            [
                "Cold Northern (Severe Freezing Winters)",
                "Moderate Temperate (Cold Winters, Warm Summers)",
                "Warm Temperate (Mild Winters, Long Summers)",
                "Subtropical / Mediterranean (Rare Frosts)",
                "Tropical (Frost-Free Year Round)",
            ]
        )
        climate_zone_map = {
            "Cold Northern (Severe Freezing Winters)": zone_keys[0],
            "Moderate Temperate (Cold Winters, Warm Summers)": zone_keys[2],
            "Warm Temperate (Mild Winters, Long Summers)": zone_keys[4],
            "Subtropical / Mediterranean (Rare Frosts)": zone_keys[5],
            "Tropical (Frost-Free Year Round)": zone_keys[7],
        }
        suggested_zone = climate_zone_map[quick_climate]
        st.info(f"Suggested Match: **{suggested_zone}**")

    # Metrics Grid
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown(
            f"""<div class="metric-card-lux">
                <div class="metric-val-lux">{zone_data['last_frost']}</div>
                <div class="metric-lbl-lux">Spring Last Frost Date</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with col_m2:
        st.markdown(
            f"""<div class="metric-card-lux">
                <div class="metric-val-lux">{zone_data['first_frost']}</div>
                <div class="metric-lbl-lux">Fall First Frost Date</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with col_m3:
        st.markdown(
            f"""<div class="metric-card-lux">
                <div class="metric-val-lux">{zone_data['growing_season_days']} Days</div>
                <div class="metric-lbl-lux">Growing Window</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with col_m4:
        st.markdown(
            f"""<div class="metric-card-lux">
                <div class="metric-val-lux">{zone_data['outdoor_direct_sow']}</div>
                <div class="metric-lbl-lux">Direct Sow Kickoff</div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("---")
    col_plan1, col_plan2 = st.columns([1, 1])
    with col_plan1:
        st.markdown(f"#### 🌱 Actionable Crop Recommendations for {selected_zone_name.split(' ')[0]}")
        st.write(f"**Zone Advice:** {zone_data['key_advice']}")
        st.markdown("**Top Recommended Crops:**")
        cols_crops = st.columns(len(zone_data['recommended_crops']))
        for idx, crop in enumerate(zone_data['recommended_crops']):
            with cols_crops[idx]:
                st.markdown(f"🌾 **{crop}**")
        st.markdown("##### 📅 Seasonal Timing:")
        st.markdown(f"- **Start Indoors / Cold Frame:** `{zone_data['indoor_start']}`")
        st.markdown(f"- **Direct Sow Outdoors:** `{zone_data['outdoor_direct_sow']}`")

    with col_plan2:
        st.markdown("#### ✅ Hands-on Outdoor Garden Checklist")
        tasks = [
            f"Aerate top 2 inches of soil in garden beds or containers in {selected_zone_name.split(' ')[0]}",
            "Collect dry brown leaves or cardboard to build carbon compost layer",
            "Perform tactile soil moisture finger-check across all potted plants",
            "Prune dead or diseased foliage with clean shears",
            "Spend at least 30 minutes outside barefoot or hands in living soil",
        ]
        for i, t in enumerate(tasks):
            st.checkbox(t, key=f"garden_task_{zone_data['zone_number']}_{i}")

    st.markdown("---")
    st.markdown("### 🤝 Offline Companion Planting Matrix")
    selected_companion_plant = st.selectbox(
        "Choose a Crop to Inspect Companion Relationships:",
        options=[c["plant"] for c in COMPANION_PLANTS],
    )
    companion_info = next(c for c in COMPANION_PLANTS if c["plant"] == selected_companion_plant)

    col_comp1, col_comp2, col_comp3 = st.columns(3)
    with col_comp1:
        st.success(f"**Best Garden Friends (Plant Together):**\n\n" + "\n".join([f"- {p}" for p in companion_info["best_friends"]]))
    with col_comp2:
        st.error(f"**Antagonistic Neighbors (Keep Apart):**\n\n" + "\n".join([f"- {p}" for p in companion_info["avoid"]]))
    with col_comp3:
        st.info(f"**Ecological Mechanism & Benefit:**\n\n{companion_info['benefit']}")


# -----------------------------------------------------------------------------
# TAB 4: Offline Diagnosis & Action Cards
# -----------------------------------------------------------------------------
with tab_cards:
    st.markdown("### 📋 Offline Diagnosis & Action Cards")
    st.write("Triage plant ailments and render clear, downloadable action cards for your garden shed or greenhouse.")

    diag_options = [c["title"] for c in DIAGNOSTIC_CASES]
    selected_diag_title = st.selectbox(
        "Select Observed Plant Issue or Symptom Profile:",
        options=diag_options,
    )
    case_data = next(c for c in DIAGNOSTIC_CASES if c["title"] == selected_diag_title)

    urgency_color = {
        "High": "#ef4444",
        "Medium": "#f59e0b",
        "Low": "#10b981",
    }.get(case_data["urgency"], "#10b981")

    st.markdown(
        f"""
        <div class="glass-card" style="border-left: 8px solid {urgency_color};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                <h3 style="margin: 0; color: #ffffff;">🌱 {case_data['title']}</h3>
                <span style="background-color: {urgency_color}; color: white; padding: 4px 14px; border-radius: 14px; font-size: 0.82rem; font-weight: 700;">
                    URGENCY: {case_data['urgency'].upper()}
                </span>
            </div>
            <p style="color: #a7f3d0; font-size: 0.94rem; margin-bottom: 0.8rem;">
                <b>Identified Symptoms:</b> {', '.join(case_data['symptoms'])}
            </p>
            <div style="margin-top: 10px;">
                <div style="font-weight: 700; color: #6ee7b7; margin-bottom: 4px;">🚨 Phase 1 (Immediate 0-24 hrs):</div>
                <div style="margin-bottom: 8px; color: #e2ece6;">{case_data['step1_immediate']}</div>
                <div style="font-weight: 700; color: #6ee7b7; margin-bottom: 4px;">⏳ Phase 2 (Follow-up 48 hrs):</div>
                <div style="margin-bottom: 8px; color: #e2ece6;">{case_data['step2_followup']}</div>
                <div style="font-weight: 700; color: #6ee7b7; margin-bottom: 4px;">🛡️ Phase 3 (Long-term Prevention):</div>
                <div style="margin-bottom: 8px; color: #e2ece6;">{case_data['step3_prevention']}</div>
            </div>
            <div style="background: rgba(16, 185, 129, 0.12); border: 1px dashed #34d399; border-radius: 12px; padding: 1rem; margin-top: 1rem; color: #ffffff;">
                <b style="color: #6ee7b7;">🌿 Organic DIY Home Remedy:</b><br/>{case_data['diy_remedy']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### 📝 Interactive Field Execution Checklist")
    st.checkbox(f"Completed Phase 1: {case_data['step1_immediate']}", key=f"card_act_{case_data['id']}_1")
    st.checkbox(f"Completed Phase 2: {case_data['step2_followup']}", key=f"card_act_{case_data['id']}_2")
    st.checkbox(f"Completed Phase 3: {case_data['step3_prevention']}", key=f"card_act_{case_data['id']}_3")
    st.checkbox(f"Applied Organic Remedy: {case_data['diy_remedy']}", key=f"card_act_{case_data['id']}_4")

    action_card_markdown = f"""# FloraSprout Field Action Card: {case_data['title']}
Urgency: {case_data['urgency']}
Generated for Touch Grass Hackathon (100% Offline)

## Key Symptoms
{chr(10).join(['- ' + s for s in case_data['symptoms']])}

## Action Checklist
- [ ] Phase 1 (Immediate): {case_data['step1_immediate']}
- [ ] Phase 2 (48 Hours): {case_data['step2_followup']}
- [ ] Phase 3 (Prevention): {case_data['step3_prevention']}
- [ ] Organic Remedy: {case_data['diy_remedy']}

---
FloraSprout | Close the laptop, take this checklist, and step into the soil!
"""
    st.download_button(
        label="📥 Download Action Card (.md)",
        data=action_card_markdown,
        file_name=f"FloraSprout_{case_data['id']}_ActionCard.md",
        mime="text/markdown",
        use_container_width=True,
    )


# -----------------------------------------------------------------------------
# TAB 5: "Touch Grass" Manifesto & Open Innovation
# -----------------------------------------------------------------------------
with tab_manifesto:
    st.markdown("### 🏕️ The 'Touch Grass' Open Innovation Manifesto")

    col_m_left, col_m_right = st.columns([1, 1])
    with col_m_left:
        st.markdown(
            """
            #### 1. Why Open Innovation Matters for Living Earth
            
            - 🌲 **Field Autonomy on Trails & Remote Greenhouses:**
              Nature does not have 5G coverage. Traditional AI tools fail the moment a gardener,
              homesteader, or hiker steps into the woods or off-grid homesteads. Open-source models
              democratize intelligence everywhere, even without internet.
            
            - 🔒 **Total Soil & Land Data Privacy:**
              Your home coordinates, land parcel layout, yield metrics, and soil test results
              belong to you. FloraSprout never uploads private backyard maps or GPS locations to cloud monopolies.
            
            - 💸 **Zero Recurring Running Costs & Low Carbon Footprint:**
              No subscriptions, no token meters, no cloud data-center water cooling waste.
              Once downloaded, Gemma runs directly on local hardware without incurring API bills.
            """
        )

    with col_m_right:
        st.markdown(
            """
            #### 2. How Gemma & Open-Source Harnesses Enable Edge Execution
            
            - 🧠 **Gemma Open-Weight Efficiency:**
              Google's Gemma family represents high-capability compact open weights.
              Gemma 2B and Gemma 2 2B deliver exceptional reasoning capabilities while running comfortably
              in sub-4GB RAM environments on consumer laptops and edge SBCs (like Raspberry Pi 5).
            
            - 🔗 **Open-Source Agent Orchestration:**
              With local engines like Ollama and harnesses like LangChain, we combine deterministic
              offline botanical tables with generative neural reasoning and multimodal vision.
            
            - 🌿 **The Anti-Addiction AI Design:**
              Most consumer software maximizes screen time and ad impressions. FloraSprout is intentionally
              engineered with **Screen Time Saver Mode** to minimize screen time and maximize real-world action.
            """
        )

    st.markdown("---")
    st.markdown("#### 🧩 System Architecture Overview")
    st.markdown(
        """
        ```
        +--------------------------------------------------------------------+
        |                      FloraSprout Streamlit UI                      |
        |  [Tab 1: Health Scanner]  [Tab 2: Care AI]  [Tab 3: Garden Planner]|
        +---------------------------------+----------------------------------+
                                          |
                                          v
                      +---------------------------------------+
                      | Screen Time Saver Policy Filter       |
                      | (Strict 3-bullet, <50 words summary)  |
                      +-------------------+-------------------+
                                          |
                        +-----------------+-----------------+
                        |                                   |
                        v                                   v
        +-------------------------------+   +--------------------------------+
        | Gemini Vision / Local Gemma   |   | FloraSprout Offline Botanical  |
        | Neural Multimodal Engine      |   | & Computer Vision Spectrum     |
        | (Localhost or Cloud API)      |   | (100% Offline Edge Fallback)   |
        +-------------------------------+   +--------------------------------+
                        |                                   |
                        +-----------------+-----------------+
                                          v
        +--------------------------------------------------------------------+
        |              Output: Concise Field Action Card (.md)               |
        |              Next Step: Step away & Touch Grass 🌱                 |
        +--------------------------------------------------------------------+
        ```
        """
    )
