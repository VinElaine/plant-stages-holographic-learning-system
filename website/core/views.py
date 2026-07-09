from django.shortcuts import render

STAGES = {
    1: {
        "icon": "🌰",
        "title": "Seed",
        "description": "A sunflower begins as a tiny seed. Inside the seed is a small baby plant waiting for the right conditions to grow.",
        "fun_fact": "Sunflower seeds can stay alive for a long time before they begin to grow.",
        "duration": "1–3 days",
        "needs": "Moist soil and water",
        "sunlight": "Not required yet",
    },
    2: {
        "icon": "🌱",
        "title": "Germination",
        "description": "During germination, the seed absorbs water. A tiny root grows downward while a shoot begins to grow upward.",
        "fun_fact": "The first root helps the young plant take in water from the soil.",
        "duration": "3–7 days",
        "needs": "Water, air, and warm soil",
        "sunlight": "Low sunlight",
    },
    3: {
        "icon": "🌿",
        "title": "Seedling",
        "description": "The sunflower becomes a seedling. Small leaves appear and the young plant starts making its own food.",
        "fun_fact": "Leaves help the plant make food using sunlight.",
        "duration": "1–2 weeks",
        "needs": "Water and healthy soil",
        "sunlight": "Partial sunlight",
    },
    4: {
        "icon": "🌻",
        "title": "Mature Plant",
        "description": "The sunflower grows taller and stronger. Its stem becomes firm and more leaves develop.",
        "fun_fact": "Some sunflowers can grow taller than a person.",
        "duration": "Several weeks",
        "needs": "Water, soil nutrients, and space",
        "sunlight": "Full sunlight",
    },
    5: {
        "icon": "🌼",
        "title": "Flowering",
        "description": "The sunflower blooms. Bright petals appear and the flower head becomes visible.",
        "fun_fact": "A sunflower head is made up of many tiny flowers.",
        "duration": "Final growth stage",
        "needs": "Water and sunlight",
        "sunlight": "Full sunlight",
    },
}

def home(request):
    return render(request, "home.html")

def stages(request):
    return render(request, "stages.html")

def viewer(request, stage_id):
    stage = STAGES.get(stage_id, STAGES[1])
    return render(request, "viewer.html", {
        "stage_id": stage_id,
        "stage": stage,
    })

def hologram(request, stage_id):
    stage = STAGES.get(stage_id, STAGES[1])
    return render(request, "hologram.html", {
        "stage_id": stage_id,
        "stage": stage,
    })