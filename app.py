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

# -----------------------
# EXTRA FEATURES
# -----------------------

st.markdown("---")

# 1. REFRESH BUTTON
if st.button("🎁 Inspire Me Again"):
    st.rerun()

# -----------------------
# NEW ART REFERENCE (drawable style)
# -----------------------

st.markdown("---")
st.subheader("🖼️ Art Reference (Aesthetic Drawing Images)")

art_refs = [
    "https://i.pinimg.com/originals/bf/49/f5/bf49f598ca63628cebdb935739eebc8b.jpg",
    "https://i.pinimg.com/736x/f3/28/04/f328048f1665a9088e11ceb64f99c6ea.jpg",
    "https://i.pinimg.com/736x/e5/d7/e2/e5d7e2aebab8db8cf232c981aedd9702.jpg",
    "https://i.pinimg.com/736x/b5/86/9c/b5869c3dfbc99a5135bb6b727efbb70d.jpg",
    "https://i.pinimg.com/736x/4b/fd/79/4bfd79de26d171cdc301875aad72dd18.jpg"
]

st.image(random.choice(art_refs), use_column_width=True)

# -----------------------
# ADVANCED SKETCHPAD WITH COLOR PALETTE
# -----------------------

st.markdown("---")
st.subheader("✏️ Sketchpad")

# Make palette interactive
custom_color_palette = [
    "#000000", "#FFFFFF", "#FF0000", "#FFA500", "#FFFF00",
    "#008000", "#00FFFF", "#0000FF", "#800080", "#FFC0CB",
    "#8B4513", "#4B0082", "#A52A2A", "#00FF00"
]

# Color selection buttons
selected_color = st.radio(
    "Choose your drawing color:",
    options=custom_color_palette,
    index=0,
    horizontal=True,
    format_func=lambda x: ""
)

# display colored boxes
color_boxes = st.columns(len(custom_color_palette))
for idx, col in enumerate(color_boxes):
    with col:
        st.markdown(
            f"""
            <div style='width:25px;height:25px;background:{custom_color_palette[idx]};
            border:2px solid {"#FFF" if custom_color_palette[idx] == selected_color else "#000"};
            border-radius:5px;margin-bottom:-10px'></div>
            """,
            unsafe_allow_html=True
        )

# SKETCHPAD (bigger)
try:
    from streamlit_drawable_canvas import st_canvas

    canvas = st_canvas(
        stroke_width=4,
        stroke_color=selected_color,
        background_color="#FFFFFF",
        width=700,
        height=500,
        drawing_mode="freedraw",
        key="canvas_big"
    )

    if canvas.image_data is not None:
        st.download_button(
            "📥 Download Your Art",
            canvas.image_data.tobytes(),
            "my_sketch.png",
            "image/png"
        )

except Exception as e:
    st.warning("Sketchpad requires 'streamlit-drawable-canvas'. Add to requirements.txt")
    st.code("streamlit-drawable-canvas")

