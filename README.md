# 🌱 FloraSprout | Offline Plant Care & Garden Companion

> **"Touch Grass" Open-Source AI Hackathon Edition**  
> *A lightweight, offline-first botanical companion powered by local Google Gemma open-weight models, LangChain, and Streamlit.*

[![License: MIT](https://img.shields.io/badge/License-MIT-10b981.svg)](LICENSE)
[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest-2026-f97316.svg)](https://hacktoberfest.com/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3b82f6.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B.svg)](https://streamlit.io)
[![CI](https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI/actions/workflows/ci.yml/badge.svg)](https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI/actions/workflows/ci.yml)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Live_Showcase-10b981?logo=github)](https://lakshchinchmalatpure.github.io/HacktoberFest_Weekday01_PlantCare_AI/)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI&branch=main&mainModule=app.py)

---

Live/Deployed Link :  https://lakshchinchmalatpure.github.io/HacktoberFest_Weekday01_PlantCare_AI/

## 🌿 The "Touch Grass" Vision

Most modern digital products are designed to maximize user screen time, ad impressions, and endless scrolling. **FloraSprout turns that paradigm on its head.**

Built specifically for the **"Touch Grass" AI Hackathon**, FloraSprout is engineered with an anti-addiction philosophy: give gardeners, hikers, and plant enthusiasts the immediate botanical insight they need—and then prompt them to shut their laptop, step into the fresh air, and put their hands in living soil.

---

## 💡 Why Open Innovation Matters

### 1. 🌲 Offline Functionality on Trails, Allotments & Remote Greenhouses
Nature doesn't have 5G towers. Traditional proprietary AI assistants stop working the second you step into the woods, visit a rural farm, or enter an off-grid greenhouse. By leveraging open-weight models running locally on edge hardware, FloraSprout guarantees 100% functionality whether you are on a remote hiking trail or in a basement potting shed.

### 2. 🔒 Total Privacy for Soil, Location & Land Data
Gardeners and homesteaders cultivate sensitive data: backyard layouts, harvest yields, precise GPS coordinates, and soil chemistry. Proprietary cloud LLMs harvest this telemetry for corporate advertising and training. FloraSprout operates entirely on your local machine—zero telemetry, zero tracking, and absolute data sovereignty.

### 3. 💸 Zero Running Costs & Sustainable Computing
Cloud API subscriptions create financial barriers and rely on massive, water-intensive data centers. With local open-source models, there are zero per-token fees, zero recurring subscriptions, and an exponentially lower carbon footprint.

---

## 🧠 How Gemma & Open-Source Harnesses Enable Edge Execution

### Local Gemma Open Weights
Google's **Gemma** family represents state-of-the-art efficiency in open weights:
- **Compact Parameter Footprint**: `gemma:2b` and `gemma2:2b` fit comfortably inside sub-4GB VRAM/RAM budgets, enabling fluid local inference on commodity consumer laptops, MacBooks, and single-board computers like the Raspberry Pi 5.
- **Botanical Domain Mastery**: Despite their lightweight footprint, Gemma models excel at following structured system prompts, botanical taxonomy, and diagnostic protocols without hallucinating chemical solutions when organic alternatives exist.

### Dual-Engine Local Orchestration
FloraSprout implements an open-source orchestration harness:
1. **Local Neural Tier (Ollama + LangChain)**: Communicates directly over `localhost:11434` with the local Gemma model using specialized system prompts.
2. **Deterministic Offline Knowledge Base**: If Ollama is not active or during zero-battery/low-power conditions, FloraSprout seamlessly falls back to an embedded botanical expert rules engine covering hardiness zones, frost dates, companion planting matrices, and DIY organic recipes.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **📸 Plant Health Scanner (Upload & Diagnose)** | Upload plant photos or take live device snapshots to instantly diagnose plant health with **Gemini Vision AI** or **FloraSprout 100% Offline Edge Computer Vision**. |
| **🌿 Plant Care AI Assistant** | Local Gemma-powered botanical chat with custom prompt constraints, prompt chips, and visual leaf triage checklists. |
| **⚡ Screen Time Saver Mode** | The signature "Touch Grass" toggle that auto-constrains all AI outputs into **exactly 3 bullet points under 50 words** to encourage getting off the screen immediately. |
| **🗓️ Local Garden Planner & Frost Dates** | Offline USDA Hardiness Zone calculator (Zones 3–10) detailing spring/fall frost windows, growing season duration, and outdoor planting schedules. |
| **🤝 Companion Planting Matrix** | Offline guide to beneficial plant pairings (e.g., Tomatoes + Basil, Carrots + Rosemary) and antagonistic combinations to avoid. |
| **📋 Diagnosis & Action Cards** | Symptom triage converting plant problems into **downloadable Field Action Cards (`.md`)** with 3-phase recovery checklists and organic DIY recipes. |

---

## 🛠️ Technical Stack

- **Frontend UI**: [Streamlit](https://streamlit.io/) (Rich custom CSS organic theme)
- **Local AI Engine**: [Ollama](https://ollama.com/) running **Google Gemma** (`gemma:2b` / `gemma2:2b`)
- **Agent Harness**: [LangChain](https://www.langchain.com/) open-source orchestration
- **Image Processing**: [Pillow (PIL)](https://python-pillow.org/)
- **Runtime Environment**: 100% Offline / Local edge execution

---

## 🚀 Quickstart Guide

### 1. Clone & Navigate
```bash
git clone https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI.git
cd HacktoberFest_Weekday01_PlantCare_AI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Launch Local Gemma with Ollama
If you wish to use the local neural AI engine alongside the built-in botanical knowledge base:
1. Install [Ollama](https://ollama.com/).
2. Pull and run Gemma locally:
   ```bash
   ollama pull gemma:2b
   ollama run gemma:2b
   ```
*(Note: If Ollama is not running, FloraSprout will automatically run in Standalone Offline Mode with its built-in botanical database!)*

### 4. Start FloraSprout
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🌐 Deploy to the Cloud (Free 1-Click)

### Streamlit Community Cloud
You can deploy FloraSprout directly from this GitHub repository for free:
1. Click the **[Open in Streamlit](https://share.streamlit.io/deploy?repository=LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI&branch=main&mainModule=app.py)** badge.
2. Sign in with your GitHub account.
3. Set **Main file path** to `app.py`.
4. (Optional) In **Advanced settings > Secrets**, add your `GEMINI_API_KEY`:
   ```toml
   GEMINI_API_KEY = "your_key_here"
   ```
5. Click **Deploy!** Your app will be live at `https://<your-subdomain>.streamlit.app`.

---

## 📂 Project Structure

```text
├── app.py                # Main Streamlit web application & UI layout
├── botanical_data.py     # Offline botanical database (zones, companion matrix, symptom rules)
├── requirements.txt      # Open-source Python dependencies
└── README.md             # Project documentation & Touch Grass Manifesto
```

---

## 📜 License & Open Source Spirit

Developed for Hacktoberfest and the **"Touch Grass" Open Source AI Hackathon**.  
Released under the [MIT License](LICENSE).  

**Remember:** Don't spend too much time reading this code—water your plants and go touch grass! 🌱
