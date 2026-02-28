import streamlit as st
from rembg import remove
from PIL import Image
import io
from gtts import gTTS
import os

# Dashboard ki settings
st.set_page_config(page_title="AI Super App", layout="wide")

# Sidebar Menu (Isse Dashboard wapis aa jayega)
st.sidebar.title("🤖 AI Super App")
choice = st.sidebar.radio("Tool Select Karein:", ["🏠 Home", "🖼️ Image: BG Remover", "🎵 AI Voice Generator"])

# --- 1. HOME PAGE ---
if choice == "🏠 Home":
    st.title("🌟 Welcome to Your AI Dashboard")
    st.info("Side menu se koi bhi tool select karein!")

# --- 2. IMAGE TOOL ---
elif choice == "🖼️ Image: BG Remover":
    st.title("🎨 AI Background Remover")
    uploaded_file = st.file_uploader("Photo upload karein...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        if st.button("Hatao Background"):
            output = remove(img)
            st.image(output)
            # Download button
            buf = io.BytesIO()
            output.save(buf, format="PNG")
            st.download_button("📥 Download", buf.getvalue(), "result.png")

# --- 3. VOICE TOOL (Yahan Error aa raha tha) ---
elif choice == "🎵 AI Voice Generator":
    st.title("🎵 AI Voice Generator")
    text = st.text_area("AI se kya bulwana hai?", "Namaste! Ye mera project hai.")
    if st.button("Generate Voice"):
        with st.spinner("AI awaz bana raha hai..."):
            tts = gTTS(text=text, lang='hi')
            tts.save("voice.mp3")
            st.audio("voice.mp3")
            st.success("Hogaya!")