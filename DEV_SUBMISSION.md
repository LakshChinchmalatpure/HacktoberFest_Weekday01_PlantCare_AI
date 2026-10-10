---
title: "FloraSprout: An Offline-First Plant Care AI Built to Help You Touch Grass 🌱"
published: true
tags: hf26challenge, devchallenge, opensource, ai
canonical_url: https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI
---

# 🌱 FloraSprout | Offline Botanical AI & Garden Companion

> *Submitted for the Hacktoberfest 2026 Week 1 DEV Challenge: **"Touch Grass"** (#hf26challenge)*

---

## 🍃 What I Built

Most modern apps and AI assistants are intentionally engineered to maximize user engagement, lengthen screen time, and show ads. 

**FloraSprout** turns this paradigm on its head.

Built specifically for the **"Touch Grass"** challenge, FloraSprout is an open-source, offline-first botanical companion that diagnoses plant health from photos, plans local planting schedules, and provides actionable gardening wisdom—while actively urging you to **close your laptop, step outside, and put your hands in living soil.**

### ✨ Key Features at a Glance:

1. **📸 Plant Health Scanner (Upload & Diagnose):**
   - Upload leaf/plant photos or take a snapshot directly via device camera.
   - Dual-engine analysis: Multimodal cloud vision via **Gemini Vision AI** or 100% offline edge computer vision analyzing RGB chlorophyll and chlorosis tissue spectrums.
2. **🌿 Plant Care AI Assistant:**
   - Powered by local open-weight **Google Gemma** (`gemma:2b` / `gemma2:2b`) via Ollama & LangChain.
   - Grounded in regenerative, organic gardening techniques without recommending toxic synthetic chemicals.
3. **⚡ Screen Time Saver Mode ("Touch Grass" Engine):**
   - The heart of the project: When enabled, all AI and diagnostic outputs are strictly condensed into **exactly 3 punchy bullet points under 50 words**. Get the answer in 5 seconds, then go outside!
4. **🗓️ Local Garden Planner & Frost Date Checker:**
   - 100% offline USDA Hardiness Zone calculator (Zones 3–10) detailing spring/fall frost dates, growing season duration, and outdoor sowing kickoff.
5. **🤝 Offline Companion Planting Matrix:**
   - Permaculture relationships matrix (e.g. Tomatoes + Basil, Carrots + Rosemary, Cucumbers + Nasturtiums) with natural pest-repellent mechanisms.
6. **📋 Printable Field Action Cards:**
   - Converts diagnoses into downloadable Markdown checklists (`.md`) with 3-phase triage (0-24h immediate, 48h follow-up, long-term prevention) and organic DIY remedy recipes.

---

## 🏃 Why "Touch Grass"?

Technology should connect us with the physical world, not isolate us behind glowing glass.

When a plant in your garden or windowsill is sick, you don't need a 2,000-word SEO article or an AI chat that keeps you engaged for 20 minutes. You need three things:
1. *What is wrong?*
2. *What do I do right now?*
3. *How do I prevent it organically?*

FloraSprout's **Screen Time Saver Mode** enforces this constraint. It provides the exact diagnosis and then tells the gardener:  
> *"Mission accomplished: close your device, get your hands in the dirt, and touch grass!"*

---

## 💡 The "Open" Factor (Why Open Innovation Matters)

This project was built from the ground up on open-source principles because nature doesn't adhere to cloud monopolies.

### 1. 🌲 True Field Autonomy (Zero 5G in the Wild)
Plants grow in places where cellular reception fails: deep forests, community garden allotments, rural homesteads, and off-grid greenhouses. Proprietary cloud LLMs fail the instant you lose signal. FloraSprout runs 100% offline on local hardware, ensuring true autonomy on the trail or in the field.

### 2. 🔒 Sovereign Privacy for Soil & Land Data
Gardeners and farmers manage sensitive spatial and agricultural data: private property boundaries, crop yields, precise GPS coordinates, and soil chemistry. With FloraSprout, your data never leaves your device. No cloud harvesting, no telemetry, no tracking.

### 3. 💸 Zero Marginal Cost & Sustainable Computing
Proprietary LLM APIs charge per token and demand water-intensive hyperscale data centers. Local open weights run on consumer laptops and edge devices (like Raspberry Pi 5) for free with an exponentially lower environmental impact.

### 4. 🧠 Gemma & Open-Source Agent Harnesses
Google's **Gemma** open weights (`gemma:2b` / `gemma2:2b`) make edge intelligence possible. With sub-4GB RAM footprints, Gemma delivers high botanical reasoning and prompt-adherence while running locally via Ollama and LangChain. When offline, FloraSprout seamlessly activates its embedded botanical rule engine.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit with custom organic nature design tokens
- **Local AI:** Google Gemma 2B via Ollama & LangChain
- **Vision Diagnostics:** Gemini Vision AI + Offline PIL Pixel Spectrum Analyzer
- **Offline Knowledge:** Embedded USDA Frost Date & Companion Planting Database
- **Language:** Python 3.10+

---

## 🏕️ Taking It Outside (Field Experience)

During testing, I took FloraSprout out to our garden patch to triage a Monstera with yellowing lower leaves and inspect tomato companion plantings:
- The **Plant Health Scanner** identified early nitrogen chlorosis from the leaf photo.
- In **Screen Time Saver Mode**, FloraSprout delivered the 3-point action plan in under 30 words.
- In less than 2 minutes, the laptop was closed, and I was aerating the topsoil and top-dressing with organic worm castings barefoot in the grass!

---

## 🔗 Links & Code

- **GitHub Repository:** [LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI](https://github.com/LakshChinchmalatpure/HacktoberFest_Weekday01_PlantCare_AI)
- **License:** Open Source (MIT)

---

*Made with 💚 for Hacktoberfest 2026. Now go close your screen and touch grass! 🌱*
