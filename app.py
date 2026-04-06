import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Happy Birthday Nada ❤️", page_icon="🎂", layout="centered")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Custom CSS for the beautiful UI
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif;
    background-color: #fffafb;
}

header {visibility: hidden;}
footer {visibility: hidden;}

.title-font {
    font-family: 'Great Vibes', cursive;
    color: #d81b60;
    text-align: center;
    font-size: 4rem;
    margin-top: -50px;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(216, 27, 96, 0.2);
    animation: fadeInDown 2s ease-in-out;
}

.message-box {
    font-size: 1.15rem;
    line-height: 1.8;
    color: #4a4a4a;
    text-align: justify;
    padding: 30px 40px;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    box-shadow: 0 10px 40px 0 rgba(255, 182, 193, 0.4);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    animation: fadeInUp 2s ease-in-out;
    margin-bottom: 30px;
}

.message-box p {
    margin-bottom: 15px;
}

.signature {
    text-align: right !important;
    font-family: 'Great Vibes', cursive;
    font-size: 2rem;
    color: #d81b60;
    margin-top: 20px;
}

.audio-container {
    text-align: center;
    margin: 20px 0;
    animation: zoomIn 2s ease-in-out;
    padding: 10px;
    background: #ffecf0;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(216, 27, 96, 0.1);
}

audio {
    width: 80%;
    height: 40px;
    outline: none;
}

@keyframes fadeInDown {
    0% { opacity: 0; transform: translateY(-30px); }
    100% { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
}
@keyframes zoomIn {
    0% { opacity: 0; transform: scale(0.9); }
    100% { opacity: 1; transform: scale(1); }
}

/* Floating Hearts */
.hearts-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
    overflow: hidden;
}

.heart {
    position: absolute;
    font-size: 2rem;
    color: rgba(255, 77, 109, 0.6);
    animation: floatUp 8s infinite ease-in;
    bottom: -10vh;
}

@keyframes floatUp {
    0% { transform: translateY(0) scale(0.5) rotate(0deg); opacity: 0; }
    20% { opacity: 1; }
    80% { opacity: 1; }
    100% { transform: translateY(-110vh) scale(1.5) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# Floating hearts HTML
st.markdown("""
<div class="hearts-container">
    <div class="heart" style="left: 10%; animation-duration: 7s; animation-delay: 0s;">❤️</div>
    <div class="heart" style="left: 20%; animation-duration: 9s; animation-delay: 2s; color: #ffb3c1;">🌸</div>
    <div class="heart" style="left: 30%; animation-duration: 8s; animation-delay: 4s;">✨</div>
    <div class="heart" style="left: 40%; animation-duration: 6s; animation-delay: 1s;">💖</div>
    <div class="heart" style="left: 55%; animation-duration: 10s; animation-delay: 3s; font-size: 1.5rem;">🤍</div>
    <div class="heart" style="left: 70%; animation-duration: 7s; animation-delay: 5s;">❤️</div>
    <div class="heart" style="left: 80%; animation-duration: 8s; animation-delay: 2s; color: #ffb3c1;">🌸</div>
    <div class="heart" style="left: 90%; animation-duration: 9s; animation-delay: 1s;">✨</div>
</div>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title-font">Happy Birthday, my beautiful Nada</h1>', unsafe_allow_html=True)

# Display the beautiful birthday image
img_path = Path("assets/couple_picture.jpeg")
if img_path.exists():
    img_base64 = get_base64_of_bin_file(img_path)
    st.markdown(f'''
    <div style="text-align: center; margin-bottom: 30px; animation: zoomIn 2s ease-in-out;">
        <img src="data:image/jpeg;base64,{img_base64}" 
             style="max-width: 100%; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.15);" />
    </div>
    ''', unsafe_allow_html=True)
else:
    st.error("Image not found. Please ensure 'assets/couple_picture.jpeg' exists.")

# Audio player
audio_url = "https://upload.wikimedia.org/wikipedia/commons/4/4b/Happy_Birthday_to_You_%28Piano%29.ogg"
st.markdown(f'''
<div class="audio-container">
    <p style="font-family: 'Montserrat'; font-size: 0.9rem; color: #d81b60; margin-bottom: 5px;">
        🎵 Tap play for a birthday piano melody 🎵
    </p>
    <audio controls loop>
        <source src="{audio_url}" type="audio/ogg">
        Your browser does not support the audio element.
    </audio>
</div>
''', unsafe_allow_html=True)

# The letter
letter_content = """
<div class="message-box">
    <p><b>My dearest Nada ❤️</b></p>
    <p>I don’t even know where to begin, because no words ever feel enough when it comes to you. But today is your day, and I just want you to feel how special you truly are.</p>
    <p>You came into my life in such an unexpected way, and somehow, you became one of the most important parts of it. You didn’t just bring love, you brought warmth, comfort, and a feeling of being understood that I didn’t know I needed this much. Even from miles away, you’ve made a place in my heart that no one else can fill.</p>
    <p>On your birthday, I don’t just wish you happiness for today, I wish you a life full of peace, love, and all the little things that make you smile. I wish your heart always feels safe, your dreams come true one by one, and that you never feel alone, because you have me, always standing with you.</p>
    <p>I wish I could be there with you right now, celebrating, seeing your smile in real life, and making this day even more beautiful for you. But until that day comes, just know that my heart is with you in every moment.</p>
    <p>Thank you for being you. Thank you for loving me. And thank you for staying, even when things weren’t always easy.</p>
    <p>Happy Birthday once again, my beautiful Nada.</p>
    <div class="signature">You mean more to me than I can ever fully explain 🤍</div>
</div>
"""
st.markdown(letter_content, unsafe_allow_html=True)

# Add a little footer
st.markdown('''
<div style="text-align: center; color: #bbb; font-size: 0.8rem; margin-top: 50px;">
    Made with ❤️ for Nada
</div>
''', unsafe_allow_html=True)
