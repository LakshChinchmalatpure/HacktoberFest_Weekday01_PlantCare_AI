"""
FloraSprout Vision Analyzer
Handles structured multimodal plant health diagnostics via Google Gemini Vision
and 100% Offline Edge Computer Vision.
Provides:
1. Plant Name & Botanical Taxonomy
2. Health Status & Vitality Score (0-100%)
3. Step-by-Step Action Recommendations
4. What It Gives (Harvest, Air Purification, Ecological Benefits)
5. Needed Pesticides (Organic Bio-Remedies vs Toxic Synthetics)
6. Ecosystem Health & Biodiversity Impact
"""

import base64
import io
import json
import re
from typing import Dict, Any, Tuple, Optional
from PIL import Image
import requests


def pil_to_base64(image: Image.Image, format: str = "JPEG") -> Tuple[str, str]:
    """Convert PIL Image to base64 string and mime type."""
    buffered = io.BytesIO()
    rgb_im = image.convert("RGB")
    rgb_im.save(buffered, format="JPEG", quality=85)
    img_bytes = buffered.getvalue()
    b64_str = base64.b64encode(img_bytes).decode("utf-8")
    return b64_str, "image/jpeg"


def extract_json_from_text(text: str) -> Optional[Dict[str, Any]]:
    """Extract and parse JSON object from markdown code blocks or raw text."""
    try:
        # Check for ```json ... ``` blocks
        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        # Look for bare outermost brackets
        bracket_match = re.search(r"(\{.*\})", text, re.DOTALL)
        if bracket_match:
            return json.loads(bracket_match.group(1))
    except Exception:
        pass
    return None


def analyze_image_with_gemini(
    image: Image.Image,
    api_key: str,
    screen_time_saver: bool = False,
    plant_hint: str = "",
    symptom_hint: str = "",
) -> Tuple[bool, Dict[str, Any], str]:
    """
    Analyzes plant health using Google Gemini Vision API.
    Returns (success: bool, data_dict: dict, engine_info: str)
    """
    if not api_key or not api_key.strip():
        return False, {}, "Gemini API key is not configured."

    b64_data, mime_type = pil_to_base64(image)

    prompt = f"""You are FloraSprout, an expert botanical pathologist, organic permaculturist, and agroecologist for the 'Touch Grass' Hackathon.
Analyze this plant/leaf image and provide a comprehensive, structured evaluation.

Context Hints (if provided):
- User Plant Category: {plant_hint or 'Unspecified'}
- Observed Issue: {symptom_hint or 'Unspecified'}

You MUST respond strictly with a valid JSON object matching this exact schema:
{{
  "plant_name": "Common Plant Name (e.g. Monstera Deliciosa, Sweet Basil, Roma Tomato)",
  "scientific_name": "Botanical Latin Binomial (e.g. Monstera deliciosa, Ocimum basilicum)",
  "health_status": "Specific Health Assessment (e.g. Healthy & Thriving, Early Nitrogen Chlorosis, Spider Mite Infestation, Powdery Mildew)",
  "health_score": 85,
  "health_summary": "1-2 sentence description of observed leaf tissue and symptoms.",
  "recommendations": [
    "Phase 1 (Immediate 0-24h): Specific immediate action.",
    "Phase 2 (Follow-up 48h): Soil, watering, or pruning adjustment.",
    "Phase 3 (Long-term Prevention): Cultural practice to prevent recurrence."
  ],
  "what_it_gives": {{
    "harvest_uses": "What does this plant yield? (Edible fruits, culinary leaves, herbal tea, medicinal properties, or lush ornamental greenery).",
    "air_purification": "Air purification and oxygen contribution (e.g. filters VOCs like formaldehyde, boosts indoor humidity).",
    "pollinator_ecosystem": "Wildlife value (e.g. flowers attract honeybees, swallowtail butterflies, or provides bird shelter)."
  }},
  "pesticides_needed": {{
    "is_pesticide_required": true,
    "recommended_bio_pesticide": "Exact safe, organic bio-remedy name (e.g. Cold-Pressed Neem Oil Spray, Potassium Bicarbonate Fungicide, Castile Soap Spray, Diatomaceous Earth).",
    "recipe_application": "How to mix and apply it safely without burning leaves (e.g. 1 tsp neem + 0.5 tsp castile soap per quart water at dusk).",
    "synthetic_warning": "Explicit reminder to avoid synthetic chemical pesticides that kill bees, damage soil biology, or poison waterways."
  }},
  "ecosystem_health": {{
    "is_healthy_for_ecosystem": "Highly Beneficial / Balanced / Invasive Alert",
    "biodiversity_role": "How this plant supports ecological balance and living soil microbiomes.",
    "companion_compatibility": "Best companion plants that naturally thrive alongside it."
  }}
}}
Return ONLY the raw JSON object. Do not include markdown preamble.
"""

    candidate_models = [
        "gemini-3.5-flash",
        "gemini-3.1-flash-lite",
        "gemini-3-flash-preview",
    ]

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": b64_data,
                        }
                    },
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 1000,
            "responseMimeType": "application/json",
        },
    }

    last_err = ""
    for model_name in candidate_models:
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key.strip()}"
        try:
            resp = requests.post(api_url, headers=headers, json=payload, timeout=12.0)
            if resp.status_code == 200:
                data = resp.json()
                candidates = data.get("candidates", [])
                if candidates and "content" in candidates[0]:
                    parts = candidates[0]["content"].get("parts", [])
                    if parts and "text" in parts[0]:
                        raw_text = parts[0]["text"].strip()
                        parsed_json = extract_json_from_text(raw_text)
                        if parsed_json and "plant_name" in parsed_json:
                            return True, parsed_json, f"Gemini Vision AI ({model_name})"
            else:
                last_err = f"API Error {resp.status_code}"
        except Exception as e:
            last_err = str(e)
            continue

    return False, {}, last_err or "Gemini Vision unavailable"


def analyze_image_offline(
    image: Image.Image,
    plant_hint: str = "Houseplant",
    symptom_hint: str = "Yellowing leaves",
    screen_time_saver: bool = False,
) -> Tuple[Dict[str, Any], str]:
    """
    100% Offline Edge Computer Vision & Botanical Heuristics.
    Extracts pixel color metrics and maps them to a rich structured ecological diagnosis.
    """
    rgb_img = image.convert("RGB").resize((120, 120))
    pixels = list(rgb_img.getdata())
    total_pixels = len(pixels)

    green_count = 0
    yellow_count = 0
    brown_dark_count = 0
    pale_count = 0

    for r, g, b in pixels:
        if g > r and g > b and g > 60:
            green_count += 1
        elif r > 120 and g > 110 and b < 100:
            yellow_count += 1
        elif (r > g and r > b and g < 100) or (r < 60 and g < 60 and b < 60):
            brown_dark_count += 1
        elif r > 180 and g > 180 and b > 180:
            pale_count += 1

    green_ratio = round((green_count / total_pixels) * 100, 1)
    yellow_ratio = round((yellow_count / total_pixels) * 100, 1)
    brown_ratio = round((brown_dark_count / total_pixels) * 100, 1)
    pale_ratio = round((pale_count / total_pixels) * 100, 1)

    hint_lower = (symptom_hint + " " + plant_hint).lower()

    # Determine Plant Identity Heuristics
    if "monstera" in hint_lower or "philodendron" in hint_lower:
        plant_name = "Monstera Deliciosa (Swiss Cheese Plant)"
        scientific_name = "Monstera deliciosa"
        harvest_uses = "Lush jungle ornamental foliage; increases indoor relative humidity and transpiration."
        air_purification = "High NASA rating for filtering airborne dust, formaldehyde, and volatile hydrocarbons."
        wildlife = "In native tropical rain forests, nocturnal moths pollinate large spathe flowers."
        companions = "Golden Pothos, Snake Plant, Peace Lily."
    elif "tomato" in hint_lower or "nightshade" in hint_lower:
        plant_name = "Garden Tomato (Nightshade Family)"
        scientific_name = "Solanum lycopersicum"
        harvest_uses = "Abundant antioxidant-rich fruit (lycopene), culinary staple, fresh vine-ripened tomatoes."
        air_purification = "Foliage releases natural antimicrobial aromatics and volatile phytoncides."
        wildlife = "Flowers provide buzz-pollination pollen for native bumblebees and solitary bees."
        companions = "Genovese Basil, French Marigolds, Carrots."
    elif "snake" in hint_lower or "succulent" in hint_lower:
        plant_name = "Snake Plant / Mother-in-Law's Tongue"
        scientific_name = "Dracaena trifasciata"
        harvest_uses = "Indestructible indoor oxygen producer; strong natural fiber in historical cultivation."
        air_purification = "Performs Crassulacean Acid Metabolism (CAM), releasing oxygen and absorbing CO2 at night."
        wildlife = "Provides structured habitat for small indoor terrarium geckos; drought resilient."
        companions = "ZZ Plant, Jade Plant, Aloe Vera."
    elif "basil" in hint_lower or "herb" in hint_lower or "mint" in hint_lower:
        plant_name = "Sweet Genovese Basil"
        scientific_name = "Ocimum basilicum"
        harvest_uses = "Aromatic culinary herb, high in eugenol and flavonoids, pest-deterring garden companion."
        air_purification = "Releases fragrant essential oils with natural air-freshening and antimicrobial qualities."
        wildlife = "Prolific nectar source for honeybees, bumblebees, and beneficial hoverflies."
        companions = "Tomatoes, Bell Peppers, Oregano."
    else:
        plant_name = "Botanical Specimen (Foliage Plant)"
        scientific_name = "Plantae / Angiosperm"
        harvest_uses = "Decorative botanical foliage, supports indoor mental well-being and biophilic design."
        air_purification = "Actively absorbs CO2 and replenishes clean indoor oxygen via chlorophyll photosynthesis."
        wildlife = "Supports local micro-fauna and soil fungi in naturalized garden beds."
        companions = "Clover cover crop, Marigolds, Chives."

    # Determine Health, Pesticides & Ecosystem
    if yellow_ratio > 20 or "yellow" in hint_lower:
        health_status = "Chlorosis (Nitrogen Hunger / Overwatering)"
        health_score = max(40, 100 - int(yellow_ratio * 1.5))
        summary = "Foliage exhibits chlorotic yellowing from waterlogged roots or depleted nitrogen reserves."
        recs = [
            "Phase 1 (Immediate): Cease watering; inspect bottom drainage holes and empty standing saucer water.",
            "Phase 2 (48 Hours): Aerate topsoil 2 inches deep with a wooden chopstick to restore root oxygenation.",
            "Phase 3 (Prevention): Top-dress with aged worm castings (vermicompost) for gentle, slow-release nitrogen."
        ]
        pesticide_needed = True
        bio_pest = "Mild Hydrogen Peroxide Soil Oxygenator"
        recipe = "Dilute 1 tbsp 3% food-grade hydrogen peroxide in 1 cup water; drench soil to eliminate anaerobic pathogens."
        eco_health = "Ecologically Restorable"
        eco_role = "Recovers quickly once aerobic soil microbial balance is restored without synthetic chemicals."
    elif brown_ratio > 18 or "crispy" in hint_lower or "dry" in hint_lower:
        health_status = "Thermal Desiccation & Low Humidity Scorch"
        health_score = max(45, 100 - int(brown_ratio * 1.8))
        summary = "Brown crispy tissue margins caused by hot drafts, direct glass radiation, or severe underwatering."
        recs = [
            "Phase 1 (Immediate): Move plant 2-3 feet back from intense midday scorching windows or heaters.",
            "Phase 2 (48 Hours): Bottom-soak the root ball in a lukewarm water basin for 25 minutes until rehydrated.",
            "Phase 3 (Prevention): Group plants together to create a natural humid microclimate and mulch container topsoil."
        ]
        pesticide_needed = False
        bio_pest = "None Required (Physiological Stress)"
        recipe = "No chemical intervention needed. Apply liquid kelp extract (seaweed) to boost cellular recovery."
        eco_health = "Harmless Physiological Stress"
        eco_role = "Non-contagious condition. Dead foliage can be trimmed and safely composted into rich humus."
    elif "web" in hint_lower or "mite" in hint_lower or "pest" in hint_lower:
        health_status = "Sap-Sucking Pest Colony (Spider Mites / Aphids)"
        health_score = 48
        summary = "Observed stippling and micro-webbing indicating sap-sucking pest infestation on tender leaf tissues."
        recs = [
            "Phase 1 (Immediate): Quarantine plant and give a lukewarm shower spray to dislodge active pests.",
            "Phase 2 (48 Hours): Spray undersides of leaves and stem joints thoroughly with cold-pressed neem oil solution.",
            "Phase 3 (Prevention): Wipe leaves weekly with damp microfiber cloth to remove dust and prevent re-infestation."
        ]
        pesticide_needed = True
        bio_pest = "Cold-Pressed Organic Neem Oil & Castile Soap Spray"
        recipe = "Mix 1 tsp cold-pressed organic neem oil + 0.5 tsp gentle castile soap in 1 quart lukewarm water. Spray at dusk every 4 days."
        eco_health = "Pest Pressure (Requires Organic Control)"
        eco_role = "Controlling pests with organic bio-soap preserves ladybugs, lacewings, and beneficial predatory mites."
    else:
        health_status = "Vibrant Foliage (Healthy Specimen)"
        health_score = min(98, max(75, int(green_ratio * 1.1)))
        summary = "Dense green chlorophyll distribution indicates vigorous photosynthesis and balanced cellular hydration."
        recs = [
            "Phase 1 (Immediate): Clean foliage with a damp cloth to optimize solar photon absorption.",
            "Phase 2 (48 Hours): Rotate pot 90 degrees to ensure even growth toward natural light.",
            "Phase 3 (Prevention): Continue finger-tested soil watering and seasonal organic compost top-dressing."
        ]
        pesticide_needed = False
        bio_pest = "Preventative Chamomile Tea Foliar Tonic"
        recipe = "Brew mild chamomile tea (anti-fungal), let cool completely, and mist lightly once a month as an organic protective tonic."
        eco_health = "Thriving Ecological Contributor"
        eco_role = "Active photosynthesis producing clean oxygen and fostering beneficial root mycorrhizal fungi."

    data = {
        "plant_name": plant_name,
        "scientific_name": scientific_name,
        "health_status": health_status,
        "health_score": health_score,
        "health_summary": summary,
        "recommendations": recs,
        "what_it_gives": {
            "harvest_uses": harvest_uses,
            "air_purification": air_purification,
            "pollinator_ecosystem": wildlife,
        },
        "pesticides_needed": {
            "is_pesticide_required": pesticide_needed,
            "recommended_bio_pesticide": bio_pest,
            "recipe_application": recipe,
            "synthetic_warning": "Strictly avoid synthetic chemical neonicotinoids or pyrethroids that exterminate pollinators and sterilize soil biology.",
        },
        "ecosystem_health": {
            "is_healthy_for_ecosystem": eco_health,
            "biodiversity_role": eco_role,
            "companion_compatibility": companions,
        },
        "pixel_metrics": {
            "green_ratio": green_ratio,
            "yellow_ratio": yellow_ratio,
            "brown_ratio": brown_ratio,
            "pale_ratio": pale_ratio,
        },
    }

    return data, "FloraSprout Edge Computer Vision (100% Offline Pixel Spectrum)"
