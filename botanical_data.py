"""
FloraSprout Offline Botanical Knowledge Base & Garden Data Engine
Designed for the "Touch Grass" Open Source Hackathon.
Provides 100% offline data for hardiness zones, frost dates, companion planting,
symptom diagnosis, and fallback botanical knowledge.
"""

from typing import Dict, List, Any, Optional

HARDINESS_ZONES: Dict[str, Dict[str, Any]] = {
    "Zone 3 (-40°F to -30°F / -40°C to -34°C)": {
        "zone_number": 3,
        "last_frost": "May 15 - June 1",
        "first_frost": "Sept 1 - Sept 15",
        "growing_season_days": 105,
        "recommended_crops": ["Kale", "Spinach", "Garlic", "Cabbage", "Carrots", "Radishes", "Peas"],
        "indoor_start": "Late March / Early April",
        "outdoor_direct_sow": "Late May",
        "key_advice": "Focus on ultra cold-hardy greens and short-season root vegetables. Utilize cold frames or cloches early in spring."
    },
    "Zone 4 (-30°F to -20°F / -34°C to -29°C)": {
        "zone_number": 4,
        "last_frost": "May 1 - May 15",
        "first_frost": "Sept 15 - Oct 1",
        "growing_season_days": 125,
        "recommended_crops": ["Beets", "Broccoli", "Potatoes", "Bush Beans", "Onions", "Squash"],
        "indoor_start": "Mid March",
        "outdoor_direct_sow": "Early May",
        "key_advice": "Mulch heavily before winter freeze. Choose short-maturity tomato varieties (e.g., Stupice, Sub-Arctic Plenty)."
    },
    "Zone 5 (-20°F to -10°F / -29°C to -23°C)": {
        "zone_number": 5,
        "last_frost": "April 15 - April 30",
        "first_frost": "Oct 1 - Oct 15",
        "growing_season_days": 150,
        "recommended_crops": ["Tomatoes", "Peppers", "Swiss Chard", "Lettuce", "Cucumbers", "Apples"],
        "indoor_start": "Early March",
        "outdoor_direct_sow": "Late April",
        "key_advice": "Excellent balance for cool-season spring crops followed by warm summer nightshades. Watch out for late April frost snaps."
    },
    "Zone 6 (-10°F to 0°F / -23°C to -18°C)": {
        "zone_number": 6,
        "last_frost": "April 1 - April 15",
        "first_frost": "Oct 15 - Oct 31",
        "growing_season_days": 175,
        "recommended_crops": ["Tomatoes", "Zucchini", "Pole Beans", "Sweet Corn", "Berries", "Herbs"],
        "indoor_start": "Late February",
        "outdoor_direct_sow": "Mid April",
        "key_advice": "Long enough for succession sowing of lettuces, radishes, and bush beans every two to three weeks."
    },
    "Zone 7 (0°F to 10°F / -18°C to -12°C)": {
        "zone_number": 7,
        "last_frost": "March 15 - March 31",
        "first_frost": "Oct 25 - Nov 10",
        "growing_season_days": 200,
        "recommended_crops": ["Eggplant", "Melons", "Sweet Potatoes", "Okra", "Peaches", "Rosemary"],
        "indoor_start": "Mid February",
        "outdoor_direct_sow": "Late March",
        "key_advice": "Double cropping is easily viable: harvest spring brassicas in June, then replant with heat-loving cowpeas or sweet potatoes."
    },
    "Zone 8 (10°F to 20°F / -12°C to -7°C)": {
        "zone_number": 8,
        "last_frost": "March 1 - March 15",
        "first_frost": "Nov 10 - Nov 25",
        "growing_season_days": 230,
        "recommended_crops": ["Figs", "Artichokes", "Hot Peppers", "Watermelon", "Winter Greens", "Citrus"],
        "indoor_start": "Late January / Early February",
        "outdoor_direct_sow": "Mid March",
        "key_advice": "Midsummer heat can bolt cool crops. Use 30% shade cloth for lettuces in July/August and plant for winter harvest."
    },
    "Zone 9 (20°F to 30°F / -7°C to -1°C)": {
        "zone_number": 9,
        "last_frost": "Feb 1 - Feb 15",
        "first_frost": "Dec 1 - Dec 15",
        "growing_season_days": 275,
        "recommended_crops": ["Citrus", "Avocado", "Pomegranates", "Tomatoes (Winter & Spring)", "Guava"],
        "indoor_start": "January",
        "outdoor_direct_sow": "Mid February",
        "key_advice": "Winter is prime cool-season gardening! Shift heat-sensitive brassicas and lettuces entirely to autumn-winter months."
    },
    "Zone 10 (30°F to 40°F / -1°C to +4°C)": {
        "zone_number": 10,
        "last_frost": "Rare / Frost Free (Jan 15 if any)",
        "first_frost": "Rare / Frost Free",
        "growing_season_days": 340,
        "recommended_crops": ["Mango", "Papaya", "Banana", "Ginger", "Turmeric", "Passion Fruit"],
        "indoor_start": "Year-round",
        "outdoor_direct_sow": "Year-round",
        "key_advice": "Prioritize mulch and deep drip irrigation to retain soil moisture under strong solar exposure. Watch for fungal leaf rot in monsoon seasons."
    }
}

COMPANION_PLANTS: List[Dict[str, Any]] = [
    {
        "plant": "Tomato",
        "best_friends": ["Basil", "Marigolds", "Carrots", "Borage"],
        "avoid": ["Potatoes", "Fennel", "Cabbage / Brassicas", "Corn"],
        "benefit": "Basil repels hornworms and enhances flavor; Marigolds deter root-knot nematodes with natural alpha-terthienyl secretion."
    },
    {
        "plant": "Carrot",
        "best_friends": ["Rosemary", "Leeks", "Lettuce", "Chives"],
        "avoid": ["Dill", "Parsnips", "Fennel"],
        "benefit": "Leeks and Rosemary disguise carrot scent, deterring the destructive carrot rust fly."
    },
    {
        "plant": "Lettuce & Greens",
        "best_friends": ["Chives", "Radishes", "Strawberries", "Cucumbers"],
        "avoid": ["Celery", "Parsley"],
        "benefit": "Radishes act as a trap crop for flea beetles; tall cucumbers provide partial afternoon shade against bolting."
    },
    {
        "plant": "Beans (Legumes)",
        "best_friends": ["Corn", "Squash (Three Sisters)", "Cucumbers", "Summer Savory"],
        "avoid": ["Onions", "Garlic", "Shallots", "Leeks"],
        "benefit": "Fixes atmospheric nitrogen into root nodules with Rhizobia bacteria, feeding neighboring heavy nitrogen feeders."
    },
    {
        "plant": "Cucumbers",
        "best_friends": ["Nasturtiums", "Radishes", "Sunflowers", "Dill"],
        "avoid": ["Aromatic herbs (Sage)", "Potatoes"],
        "benefit": "Nasturtiums attract beneficial predatory insects and repel cucumber beetles; Sunflowers serve as living climbing trellises."
    },
    {
        "plant": "Brassicas (Broccoli, Kale, Cabbage)",
        "best_friends": ["Mint", "Thyme", "Chamomile", "Beets"],
        "avoid": ["Tomatoes", "Strawberries", "Mustard"],
        "benefit": "Aromatic thyme and mint mask the scent of brassicas, confusing cabbage white moths."
    }
]

DIAGNOSTIC_CASES: List[Dict[str, Any]] = [
    {
        "id": "overwatering",
        "title": "Waterlogged Roots / Overwatering",
        "symptoms": ["Yellowing lower leaves", "Soft mushy stem base", "Soil stays wet for over 7 days", "Fungus gnats"],
        "urgency": "High",
        "step1_immediate": "Halt watering immediately. Remove nursery pot saucer to drain standing water. Inspect drainage holes.",
        "step2_followup": "Within 48 hours: Poke aeration holes in topsoil using a chopstick. If soil smells sour/rotting, gently inspect roots and trim brown mushy tips.",
        "step3_prevention": "Allow top 2 inches (5 cm) of soil to dry before watering again. Switch to a terracotta pot with high aeration.",
        "diy_remedy": "Dilute 3% food-grade hydrogen peroxide (1 tbsp per cup water) to drench soil and oxygenate roots while inhibiting anaerobic root rot."
    },
    {
        "id": "underwatering",
        "title": "Severe Dehydration / Underwatering",
        "symptoms": ["Dry crispy leaf tips", "Drooping leaves that feel paper-thin", "Soil pulling away from pot edges", "Lightweight pot"],
        "urgency": "Medium",
        "step1_immediate": "Bottom-water: Place pot in a sink or basin with 2-3 inches of lukewarm water for 30 minutes until surface soil feels moist.",
        "step2_followup": "Drain thoroughly for 15 minutes before returning to decorative pot. Remove completely dry, brittle brown leaves.",
        "step3_prevention": "Set a tactile soil-check routine: lift pot weight or touch soil moisture twice a week instead of calendar-bound watering.",
        "diy_remedy": "Top-dress with a 0.5-inch layer of coconut coir or compost mulch to reduce surface evaporation."
    },
    {
        "id": "spider_mites",
        "title": "Spider Mite Infestation",
        "symptoms": ["Fine silky webbing underneath leaves", "Stippled speckled pale spots on leaf surface", "Dull dusty appearance"],
        "urgency": "High",
        "step1_immediate": "Quarantine plant immediately from neighboring plants. Wash leaves thoroughly under a lukewarm shower or hose spray to dislodge mites.",
        "step2_followup": "Spray entire plant (especially undersides of leaves and leaf nodes) with organic insecticidal soap or neem oil spray.",
        "step3_prevention": "Spider mites flourish in dry, arid indoor air. Increase ambient humidity to 55%+ and wipe leaves weekly with a damp microfiber cloth.",
        "diy_remedy": "Mix 1 tsp pure organic neem oil + 0.5 tsp gentle castile soap in 1 quart (1 liter) lukewarm water. Shake well and spray every 4 days for 2 weeks."
    },
    {
        "id": "powdery_mildew",
        "title": "Powdery Mildew Fungal Infection",
        "symptoms": ["White talcum powder-like patches on leaves", "Distorted new growth", "Curling leaves", "Occurs in humid, stagnant air"],
        "urgency": "Medium",
        "step1_immediate": "Prune off heavily infected leaves with sterilized shears. Disinfect blades with rubbing alcohol between cuts.",
        "step2_followup": "Increase air circulation by spacing plants apart or using an oscillating fan. Water strictly at soil level, avoiding wet foliage.",
        "step3_prevention": "Ensure morning sunlight reaches plant to dry nocturnal dew quickly. Avoid high-nitrogen fertilizers that create weak, succulent tissues.",
        "diy_remedy": "Mix 1 tbsp baking soda + 0.5 tsp liquid castile soap in 1 gallon water. Spray foliage in early morning to raise leaf pH and inhibit spores."
    },
    {
        "id": "nitrogen_deficiency",
        "title": "Nitrogen / Nutrient Depletion (Chlorosis)",
        "symptoms": ["General pale yellowing starting from oldest lower leaves", "Stunted vegetative growth", "Thin spindly stems"],
        "urgency": "Low",
        "step1_immediate": "Apply a mild, quick-release organic foliar feed or liquid seaweed/kelp extract.",
        "step2_followup": "Top-dress soil with well-aged compost, worm castings (vermicompost), or organic alfalfa meal.",
        "step3_prevention": "Establish a seasonal soil replenishment habit. Plant nitrogen-fixing legumes (clover, peas) as living cover crops.",
        "diy_remedy": "Brew compost tea: Steep 2 cups aged worm castings in a 5-gallon bucket of aerated water for 24 hours. Drench root zone."
    },
    {
        "id": "sun_scorch",
        "title": "Sun Scorch / Thermal Stress",
        "symptoms": ["Bleached white or tan scorched patches on leaves facing window/sun", "Crispy brittle centers on foliage", "Rapid moisture loss"],
        "urgency": "Medium",
        "step1_immediate": "Move plant 2-4 feet back from harsh direct midday light or draw a sheer curtain.",
        "step2_followup": "Mist air around the plant (not direct hot leaves) to reduce transpiration stress. Ensure deep hydration.",
        "step3_prevention": "Acclimate plants gradually over 10-14 days before transitioning them outdoors or into brighter exposures.",
        "diy_remedy": "Apply a light kelp extract drench to boost cellular heat-shock proteins and support tissue recovery."
    }
]

FALLBACK_KNOWLEDGE_BASE: Dict[str, Dict[str, str]] = {
    "monstera": {
        "full": """**Monstera Deliciosa Care Guide:**
- **Light:** Medium to bright indirect sunlight. Avoid direct scorching rays which cause bleached brown leaf spots.
- **Watering:** Water thoroughly when top 2-3 inches of soil dry out. Ensure drainage pot hole is clear.
- **Humidity & Soil:** Thrives in 60%+ humidity. Prefers chunky, aroid mix (orchid bark, perlite, peat, peat-moss/coco coir).
- **Pro-Tip:** Wipe leaves monthly with a soft damp cloth to clean dust and optimize chlorophyll sunlight absorption.""",
        "screen_saver": """- **Water:** Soak only when top 2" soil dries out completely.
- **Light:** Bright indirect light; protect from midday direct sun.
- **Action:** Wipe broad leaves with damp cloth, then head outside!"""
    },
    "snake plant": {
        "full": """**Snake Plant (Sansevieria / Dracaena trifasciata) Care:**
- **Light:** Adapts from low shade to bright sunny windows. Truly indestructible.
- **Watering:** Minimalist plant. Water every 2-4 weeks only when soil is 100% bone dry. Overwatering is the only real danger.
- **Soil:** Fast-draining succulent or cactus mix.
- **Action:** Put it in your room, forget about watering for 3 weeks, and enjoy fresh indoor air while you touch grass outside!""",
        "screen_saver": """- **Water:** Once every 3-4 weeks; only when bone dry.
- **Light:** Thrives in any light from shade to sunshine.
- **Action:** Neglect is best—step away from screens and enjoy nature!"""
    },
    "yellow leaves": {
        "full": """**Yellow Leaves Triage Protocol:**
1. **Oldest lower leaves yellowing?** Natural shedding or mild nitrogen hunger.
2. **Soft, yellow leaves with soggy soil?** Classic overwatering. Stop watering immediately and check drainage.
3. **Yellowing with dry, crispy tips?** Underwatering or low humidity. Deep soak pot in sink.
4. **Yellow patches with fine webs?** Spider mites. Rinse plant under shower and apply organic neem spray.""",
        "screen_saver": """- **Check Moisture:** Feel soil 2" deep—soggy means overwatered, dry means thirsty.
- **Inspect:** Look under yellow leaves for web mites or pests.
- **Action:** Adjust watering, clip dead foliage, and take a garden walk!"""
    },
    "tomato": {
        "full": """**Tomato Organic Master Care:**
- **Sun:** 6-8+ hours of direct unfiltered outdoor sunshine.
- **Watering:** Deep, consistent watering at the soil base (not on leaves) to prevent blossom end rot and fungal blight.
- **Support & Prune:** Stake or cage early. Pinch out non-flowering suckers between main stem and branches.
- **Companion Plant:** Plant fragrant Genovese basil next to tomatoes to deter hornworms and improve vigor.""",
        "screen_saver": """- **Sun & Base Water:** 6+ hours sun; water soil only, never foliage.
- **Prune:** Pinch leaf suckers at 45° angles for bigger yields.
- **Action:** Mulch root zone with straw, then spend the afternoon outside!"""
    },
    "pests": {
        "full": """**Natural Garden Pest Management:**
- **Aphids & Spider Mites:** Spray with solution of 1 quart water + 1 tsp mild castile soap + 1 tsp cold-pressed neem oil.
- **Slugs & Snails:** Scatter coarse crushed eggshells, coarse sand, or shallow beer saucer traps near vulnerable seedlings.
- **Fungus Gnats:** Let topsoil dry out completely. Sprinkle ground cinnamon on topsoil as a natural fungicide against gnat larvae.""",
        "screen_saver": """- **Soap Spray:** 1 tsp castile soap in 1 qt water for aphids/mites.
- **Soil Barrier:** Dust cinnamon on topsoil against gnats and fungus.
- **Action:** Check garden manually, hand-pick pests, and enjoy the soil!"""
    },
    "compost": {
        "full": """**Quick Backyard Compost Recipe (Touch Grass Style):**
- **Ratio:** 3 parts Brown carbon materials (dry leaves, cardboard, straw) to 1 part Green nitrogen materials (kitchen scraps, fresh grass clippings, coffee grounds).
- **Moisture:** Keep pile damp like a wrung-out kitchen sponge.
- **Air:** Turn pile with a pitchfork once every 10 days to aerate beneficial aerobic microbes.""",
        "screen_saver": """- **Balance:** 3 parts dry brown carbon : 1 part fresh green scraps.
- **Moisture:** Keep damp like a wrung-out sponge; turn bi-weekly.
- **Action:** Turn compost with a fork today for a quick physical workout!"""
    }
}


def get_offline_botanical_answer(query: str, screen_time_saver: bool = False) -> str:
    """
    Intelligent offline rule-based knowledge fallback engine.
    Activated when local Gemma/Ollama server is unavailable or when running completely standalone.
    """
    q = query.lower().strip()
    
    # Check keyword matches
    for key, data in FALLBACK_KNOWLEDGE_BASE.items():
        if key in q:
            return data["screen_saver"] if screen_time_saver else data["full"]
            
    # Generic intelligent response if query has no specific keyword
    if screen_time_saver:
        return (
            "- **Diagnose First:** Inspect soil moisture 2 inches deep with your finger.\n"
            "- **Light & Air:** Move to bright indirect light and improve fresh airflow.\n"
            "- **Touch Grass Action:** Take 5 minutes to aerate soil, then get outside!"
        )
    else:
        return (
            "### 🌿 FloraSprout Offline Botanical Advisory\n\n"
            "**General Field Guidelines for Plant Health:**\n"
            "1. **Moisture Inspection:** Over 70% of plant issues stem from overwatering. Insert your finger 2 inches into soil; only water if completely dry.\n"
            "2. **Light Exposure:** Ensure appropriate light. Yellowing/stretching indicates light starvation; crispy scorched patches indicate sunburn.\n"
            "3. **Airflow & Soil Health:** Stagnant air breeds powdery mildew and fungal gnats. Ensure pots have drainage holes and healthy organic structure.\n"
            "4. **Organic Remedy:** For mysterious leaf distress, spray diluted cold-pressed neem oil (1 tsp per quart water with mild castile soap) in the evening.\n\n"
            "*(💡 Note: Connect local Gemma via Ollama to generate free-form custom AI answers for any rare species!)*"
        )
