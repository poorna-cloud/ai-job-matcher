import streamlit as st


def load_css():

    st.markdown("""
    <style>
    

    /* Main Background */
    .stApp{
        background:#f8fafc;
    }

    /* Upload Box */
    div[data-testid="stFileUploader"]{
        background:white;
        padding:20px;
        border-radius:18px;
        border:2px dashed #2563eb;
        box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    }

    /* Text Area */
    div[data-testid="stTextArea"] textarea{
        border-radius:15px !important;
        border:2px solid #dbeafe !important;
        font-size:16px;
    }

    /* Buttons */
    .stButton>button{
        width:100%;
        height:52px;
        background:linear-gradient(135deg,#2563eb,#1d4ed8);
        color:white;
        border:none;
        border-radius:14px;
        font-size:17px;
        font-weight:bold;
        transition:0.3s;
    }

    .stButton>button:hover{
        transform:translateY(-2px);
        box-shadow:0px 8px 20px rgba(37,99,235,.35);
    }

    /* Progress Bar */
    .stProgress>div>div>div{
        background:#2563eb;
    }

    /* Metric Cards */
    div[data-testid="stMetric"]{
        background:white;
        padding:18px;
        border-radius:18px;
        border:1px solid #e2e8f0;
        box-shadow:0px 5px 15px rgba(0,0,0,.08);
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background:#0f172a;
    }

    section[data-testid="stSidebar"] *{
        color:white;
    }

    h1,h2,h3{
        color:#1e3a8a;
    }

    </style>
    """, unsafe_allow_html=True)


def hero_section():

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#2563eb,#1e3a8a);
    padding:40px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
    margin-bottom:30px;
    ">

    <h1 style="font-size:42px;color:white;">
    🤖 AI Resume Analyzer
    </h1>

    <h3 style="color:#dbeafe;">
    AI Powered Career Assistant
    </h3>

    <p style="font-size:18px;color:white;">
    Upload • Analyze • Improve • Get Hired 🚀
    </p>

    </div>
    """, unsafe_allow_html=True)
    st.caption("🚀 Analyze your Resume • Improve ATS Score • Get Interview Ready")

def sidebar():

    with st.sidebar:

        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=90
        )

        st.title("AI Resume Analyzer")

        st.markdown("---")

        st.success("🚀 AI Powered")

        st.info("💼 Career Assistant")

        st.markdown("## Features")

        st.markdown("""
- 📄 Resume Upload
- 🎯 ATS Match Score
- 📊 Dashboard
- 📈 Charts
- 🤖 AI Resume Review
- ✨ Resume Rewriter
- 💌 Cover Letter
- 🎤 Interview Questions
- 📚 Learning Roadmap
""")

        st.markdown("---")

        st.caption("👨‍💻 Developed by Poorna Chandu")
def footer():

    st.markdown("---")

    st.markdown("""
    <div style="
    text-align:center;
    padding:20px;
    color:#64748b;
    font-size:15px;
    ">

    <b>🤖 AI Resume Analyzer</b><br>

    Built with ❤️ using Python • Streamlit • Gemini AI

    <br><br>

    © 2026 Poorna Chandu

    </div>
    """, unsafe_allow_html=True)