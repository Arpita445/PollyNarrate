import streamlit as st
from pypdf import PdfReader

from utils.polly import text_to_speech


st.set_page_config(
    page_title="PollyNarrate",
    layout="wide"
)


# ================= SIDEBAR + DARK MODE =================

dark_mode = st.sidebar.toggle(
    "🌙 Dark Mode"
)


# ================= CSS =================

base_css = """
<style>

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top:1rem;
}


.stButton > button {

    background-color:#ff69b4;
    color:white;
    border-radius:12px;
    border:none;

}


.stButton > button:hover {

    background-color:#e75480;

}


.stDownloadButton > button {

    background-color:#ff85c1;
    color:white;
    border-radius:12px;

}


.upload-card {

    padding:30px;
    border-radius:20px;
    text-align:center;
    border:2px dashed #ff69b4;
    margin:20px 0;

}

</style>
"""


st.markdown(
    base_css,
    unsafe_allow_html=True
)



# ================= THEME =================


if dark_mode:

    st.markdown(
        """
        <style>

        .stApp {

            background-color:#181818;
            color:white;

        }


        [data-testid="stSidebar"] {

            background-color:#262626;

        }


        p,label,span {

            color:white;

        }


        h1,h2,h3 {

            color:#ff85c1 !important;

        }


        .upload-card {

            background-color:#30202a;
            border-color:#ff85c1;

        }


        .upload-card p {

            color:white;

        }


        textarea {

            background-color:#262626 !important;
            color:white !important;

        }


        div[data-baseweb="select"] > div {

            background-color:#333333;
            color:white;

        }


        [data-testid="stMetricValue"] {

            color:#ff85c1;

        }


        </style>
        """,
        unsafe_allow_html=True
    )


else:

    st.markdown(
        """
        <style>

        .stApp {

            background-color:#fff0f5;

        }


        [data-testid="stSidebar"] {

            background-color:#ffe4ec;

        }


        .upload-card {

            background-color:#ffe4ec;

        }


        </style>
        """,
        unsafe_allow_html=True
    )



# ================= SIDEBAR =================


with st.sidebar:

    st.title("🎙️ PollyNarrate")

    st.write(
        """
        AI-powered document narration
        using Amazon Polly Text-To-Speech.
        """
    )


    st.divider()


    st.write(
        """
        ✨ Features

        📄 PDF Extraction

        🎤 Voice Selection

        🔊 Amazon Polly TTS

        ⬇ MP3 Download
        """
    )



# ================= HERO =================


st.markdown(
    """
    <div style="
    background:linear-gradient(135deg,#ffd6e7,#fff0f5);
    padding:35px;
    border-radius:20px;
    text-align:center;
    ">

    <h1 style="color:#c2185b;font-size:45px;">
    🎙️ PollyNarrate
    </h1>


    <h3 style="color:#7b1fa2;">
    Transform your documents into spoken experiences
    </h3>


    <p style="font-size:18px;">
    AI-powered document narration using Amazon Polly
    Text-To-Speech
    </p>


    </div>
    """,
    unsafe_allow_html=True
)



st.write("")



# ================= VOICES =================


voices = {

    # English
    "Aditi - Indian English 🇮🇳": "Aditi",
    "Raveena - Indian English 🇮🇳": "Raveena",
    "Joanna - US English 🇺🇸": "Joanna",
    "Matthew - US English 🇺🇸": "Matthew",

    # Hindi
    "Kajal - Hindi 🇮🇳": "Kajal",

    # French
    "Lea - French 🇫🇷": "Lea",
    "Mathieu - French 🇫🇷": "Mathieu",

    # Spanish
    "Lucia - Spanish 🇪🇸": "Lucia",
    "Enrique - Spanish 🇪🇸": "Enrique",

    # German
    "Marlene - German 🇩🇪": "Marlene",
    "Hans - German 🇩🇪": "Hans",

    # Italian
    "Bianca - Italian 🇮🇹": "Bianca",

    # Japanese
    "Mizuki - Japanese 🇯🇵": "Mizuki"

}



col1,col2 = st.columns(2)



with col1:

    voice_name = st.selectbox(
        "🎤 Select Voice",
        list(voices.keys())
    )


with col2:

    uploaded_file = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )


voice_id = voices[voice_name]



# ================= UPLOAD CARD =================


st.markdown(
    """
    <div class="upload-card">

    <h3>📄 Upload Your Document</h3>

    <p>
    Drag and drop your PDF file
    <br>
    Convert it into speech using PollyNarrate
    </p>

    </div>
    """,
    unsafe_allow_html=True
)



# ================= PDF =================


if uploaded_file:

    text=""


    pdf=PdfReader(uploaded_file)


    for page in pdf.pages:

        content=page.extract_text()

        if content:

            text+=content



    st.divider()


    st.subheader("📊 Document Information")


    c1,c2,c3=st.columns(3)


    c1.metric(
        "Pages",
        len(pdf.pages)
    )


    c2.metric(
        "Words",
        len(text.split())
    )


    c3.metric(
        "Characters",
        len(text)
    )



    st.divider()


    st.subheader("📖 Extracted Text")


    st.text_area(
        "Preview",
        text,
        height=250
    )



    if st.button("🚀 Generate Speech"):


        with st.spinner(
            "Amazon Polly generating audio..."
        ):


            audio_file=text_to_speech(
                text,
                voice_id
            )



        st.success(
            "Speech generated successfully!"
        )



        with open(audio_file,"rb") as f:

            audio_bytes=f.read()



        st.subheader(
            "🔊 Audio Preview"
        )


        st.audio(
            audio_bytes,
            format="audio/mp3"
        )


        st.download_button(
            "⬇️ Download MP3",
            audio_bytes,
            "PollyNarrate.mp3",
            "audio/mp3"
        )