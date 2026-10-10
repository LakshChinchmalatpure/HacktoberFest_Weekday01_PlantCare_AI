---
title: "FloraSprout: The Offline-First Plant Care AI Built to Help You Touch Grass 🌱"
published: true
tags: hf26challenge, devchallenge, opensource, ai
canonical_url: https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI
cover_image: https://images.unsplash.com/photo-1545239351-ef35f43d514b?w=1200&auto=format&fit=crop&q=80
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass](https://dev.to/challenges/hacktoberfest-week1-2026-10-05)*

---

## What I Built

Most modern digital products and AI apps are engineered to maximize screen time, drive dopamine loops, and keep you glued to glowing glass.

**FloraSprout** turns this paradigm on its head.

Built specifically for the **"Touch Grass"** challenge, FloraSprout is an open-source, offline-first botanical companion and plant health identifier designed with an **anti-addiction philosophy**. It helps gardeners, hikers, balcony plant parents, and homesteaders diagnose sick plants, plan local gardens, and learn safe organic remedies—while actively urging you to **close your laptop, step away from screens, and get your hands in living soil.**

### ✨ Key Features:

1. **⚡ Screen Time Saver Mode ("Touch Grass" Core Mechanism):**
   - The heart of the project: When enabled, all AI and diagnostic outputs are strictly constrained into **exactly 3 short, punchy bullet points under 50 words**.
   - You get the exact diagnosis and action plan in 5 seconds, followed by: *"Mission accomplished: Close your screen and touch grass!"*

2. **📸 Multimodal Plant Health Scanner (Upload & Diagnose):**
   - Upload any leaf/plant photo or take a snapshot with your device camera.
   - Instantly outputs:
     - **Plant Name:** Common name + Botanical Latin binomial (*e.g., Monstera Deliciosa / Monstera deliciosa*).
     - **Health Status & Vitality Score:** Visual 0–100% vigor gauge and leaf symptom summary.
     - **What It Gives:** Culinary harvest yield, NASA air purification rating (VOC filtering), and wildlife/pollinator value.
     - **Pesticides & Bio-Remedies:** Prescribed natural bio-pesticide (Neem, Castile soap, etc.) with safe DIY mixing recipes and a strict anti-synthetic chemical warning to protect bees and soil biology.
     - **Ecosystem Health:** Impact on soil mycorrhizae and best companion planting partners.
     - **3-Phase Action Plan:** Immediate triage (0-24h), 48h soil follow-up, and long-term cultural prevention.

3. **🗓️ Local Garden Planner & Frost Date Checker:**
   - 100% offline USDA Hardiness Zone calculator (Zones 3–10) detailing spring/fall frost dates, growing season duration, and outdoor sowing kickoff.

4. **🤝 Offline Companion Planting Matrix:**
   - Permaculture synergy matrix detailing beneficial pairings (e.g. Tomatoes + Basil, Carrots + Rosemary) and antagonistic combinations to avoid.

5. **📋 Downloadable Field Action Cards:**
   - Converts advice into formatted, downloadable Markdown checklists (`.md`) that you can print or take to your potting shed without carrying a laptop.

---

## Demo

- **Live GitHub Repository:** [LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI](https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI)
- **Local Application URL:** `http://localhost:8501`

### 💻 Quick Local Run:
```bash
git clone https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI.git
cd HacktoberFest_Weekday01_PlantCare_AI
pip install -r requirements.txt
streamlit run app.py
```

### 🎨 User Interface Highlights:
The app features a **Dark Biophilic Glassmorphism** interface:
- Deep obsidian canvas (`#07140e`) with bioluminescent emerald accents (`#10b981`).
- Floating segmented pill navigation tabs.
- High-contrast typography (*Outfit* & *Plus Jakarta Sans*).
- 4-Domain Diagnostic Grid with visual health gauge meters.

---

## Code

{% github LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI %}

### 📂 Repository Structure:
- `app.py`: Full Streamlit web application with custom CSS styling and segmented navigation.
- `vision_analyzer.py`: Multimodal plant diagnostic engine supporting Gemini Vision AI + 100% Offline Edge Computer Vision.
- `botanical_data.py`: Offline botanical database with hardiness zones, frost dates, and companion matrices.
- `requirements.txt`: Lightweight open-source dependencies.
- `README.md`: Architecture overview and Touch Grass Manifesto.

---

## How I Built It

FloraSprout is built on an open-source, local-first stack designed for edge devices:

1. **Local Open-Weight Model (Google Gemma):**
   - Built to run locally with **Google Gemma** (`gemma:2b` / `gemma2:2b`) via **Ollama** and **LangChain**.
   - With a compact sub-4GB RAM footprint, Gemma provides exceptional botanical reasoning and prompt adherence on consumer laptops and edge boards like the Raspberry Pi 5.

2. **Multimodal Vision & Offline Edge Fallback:**
   - Online mode connects to **Gemini Vision AI** (`gemini-3.5-flash` / `gemini-3.1-flash-lite`) using a secured, git-ignored `.env` file.
   - When completely offline in the wild, FloraSprout activates an **Offline Edge Computer Vision** pixel analyzer (powered by Pillow) that measures RGB chlorophyll tissue distribution (Green vigor %, Chlorosis yellow %, Necrotic burn %) to diagnose ailments without internet.

3. **Frontend UI:**
   - Built with **Streamlit** and heavily skinned using custom CSS tokens, frosted glass cards (`backdrop-filter: blur(20px)`), and responsive layouts.

---

## Why Does Open Innovation Matter?

This project was built from the ground up on open-source principles because **nature doesn't adhere to cloud monopolies.**

### 1. 🌲 True Field Autonomy (Zero 5G in the Wild)
Plants, allotment gardens, remote hiking trails, and rural homesteads frequently have zero cellular coverage. Proprietary cloud LLMs fail the instant you lose signal. Open-weight models running on local edge hardware ensure that intelligence is democratized everywhere, even deep in the woods.

### 2. 🔒 Sovereign Privacy for Soil & Land Data
Gardeners manage sensitive property layouts, harvest yields, precise GPS coordinates, and soil chemistry. Closed proprietary LLMs harvest this telemetry. With FloraSprout, your data never leaves your device. No telemetry, no cloud tracking, 100% local sovereignty.

### 3. 💸 Zero Marginal Costs & Ecological Sustainability
Proprietary cloud APIs charge per token and demand water-intensive hyperscale data centers. Local open weights run on consumer laptops and edge hardware for free with an exponentially lower environmental impact.

### 4. 🔓 Community Auditability & Open Collaboration
Open innovation allows agricultural extension offices, permaculture collectives, and community gardens to inspect, fine-tune, and adapt the knowledge base for hyper-local microclimates without proprietary lock-in.

---

## My Agent Session

This project was pair-programmed from scratch using **Google DeepMind Antigravity**:
- Cloned the repository and architected the full offline botanical engine.
- Implemented the multimodal vision pipeline with Gemini Vision and offline edge computer vision.
- Handled GitHub Push Protection security by abstracting API keys into `.env` and `.env.example`.
- Verified and styled the Dark Biophilic Glassmorphism interface.

---

## Prize Categories

- **Main Theme Track: "Touch Grass"** — An AI application intentionally designed to minimize screen time (Screen Time Saver Mode: 3 bullets, <50 words) and encourage direct, physical interaction with living soil and outdoor plants.
- **Open-Source AI & Local Inference Track** — Full edge execution capability leveraging Google Gemma open weights, Ollama, LangChain, and offline botanical datasets.

---

*Made with 💚 for Hacktoberfest 2026. Now close your screen, step into the garden, and touch grass! 🌱*
