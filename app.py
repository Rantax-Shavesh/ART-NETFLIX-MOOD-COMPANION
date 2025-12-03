import streamlit as st
import random

# -----------------------
# ART PROMPTS
# -----------------------
art_prompts = [
    "Sketch a girl sitting under soft sunset light with a sketchbook.",
    "Draw a rainy window scene with reflections of city lights.",
    "Create a character holding floating lanterns at night.",
    "Sketch a peaceful bedroom workspace with plants and warm lighting.",
    "Draw someone lost in music with swirling patterns around them."
]

# -----------------------
# COLOR PALETTES
# -----------------------
color_palettes = [
    ["#FFC8DD", "#FFAFCC", "#BDE0FE", "#A2D2FF"],
    ["#F7EDE2", "#F5CAC3", "#84A59D", "#F28482"],
    ["#EDE7F6", "#D1C4E9", "#9575CD", "#673AB7"],
    ["#F1FAEE", "#A8DADC", "#457B9D", "#1D3557"],
    ["#FAF3DD", "#C8D5B9", "#8FC0A9", "#68B0AB"]
]

# -----------------------
# NETFLIX MOOD SUGGESTIONS
# -----------------------
netflix_recs = {
    "Chill": [
        ("Atypical", "Heartwarming and funny."),
        ("The Good Place", "Light comedy with a smart twist."),
        ("Our Planet", "Calm visuals and narration.")
    ],
    "Romantic": [
        ("Heartstopper", "Cute, soft, wholesome."),
        ("To All the Boys I’ve Loved Before", "Feel-good romance."),
        ("Your Name", "Emotional, aesthetic masterpiece.")
    ],
    "Action": [
        ("Extraction", "Fast, intense, full action."),
        ("Money Heist", "Tense and dramatic heist story."),
        ("The Witcher", "Action mixed with fantasy.")
    ],
    "Mystery": [
        ("Dark", "Mind-bending and gripping."),
        ("Stranger Things", "Thrilling and atmospheric."),
        ("Enola Holmes", "Light detective energy.")
    ],
    "Potato Mode": [
        ("Minions", "Chaotic yellow creatures."),
        ("Boss Baby", "Zero braincells required."),
        ("The Emoji Movie", "Why not suffer together?")
    ]
}

# -----------------------
# STREAMLIT UI
# -----------------------

st.set_page_config(page_title="Art + Netflix Mood Companion", page_icon="🎨", layout="centered")

st.title("🎨 Art + Netflix Mood Companion")
st.write("Your daily dose of creativity and comfort shows.")

st.subheader("✨ Art Prompt")
prompt = random.choice(art_prompts)
st.info(prompt)

st.subheader("🎨 Color Palette")
palette = random.choice(color_palettes)

cols = st.columns(len(palette))
for i, col in enumerate(cols):
    with col:
        st.markdown(
            f"""
            <div style='width:80px;height:80px;background:{palette[i]};border-radius:10px;margin-bottom:5px;'></div>
            <p style='text-align:center'>{palette[i]}</p>
            """,
            unsafe_allow_html=True
        )

st.subheader("🍿 Netflix Mood Picker")
mood = st.selectbox("Choose your vibe:", list(netflix_recs.keys()))

if st.button("Suggest Something"):
    name, desc = random.choice(netflix_recs[mood])
    st.success(f"**{name}** — {desc}")

